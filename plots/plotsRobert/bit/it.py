# Standard imports
import numpy as np
import copy
import cProfile
import operator 
import time

from Analysis.Tools.helpers import chunk

class Node:
    def __init__( self, features, weights, FI_func, max_depth, min_size, depth=0):

        ## basic BDT configuration
        self.max_depth  = max_depth
        self.min_size   = min_size

        # data set
        self.features   = features
        self.weights    = weights
       
        # FI func
        self.FI_func    = FI_func
 
        assert len(self.features) == len(self.weights), "Unequal length!"

        self.size       = len(self.features)

        # keep track of recursion depth
        self.depth      = depth

        self.split(depth=depth)

    # compute the total FI from a set of booleans defining the 'left' box and (by negation) the 'right' box
    def FI_from_group( self, group):
        ''' Calculate FI for selection
        '''
        sum_    =  sum(self.weights[group])
        if type(sum_)==int and sum_==0: return 0 # the case where we get a list of False
        return self.FI_func(sum_)

    # convinience for debugging
    def FI_threshold_lower( self, i_feature, value):
        feature_values = self.features[:,i_feature]
        # get column & loop over all values
        group = feature_values<value
        return self.FI_from_group( group )

    # convinience for debugging
    def FI_threshold_higher( self, i_feature, value):
        feature_values = self.features[:,i_feature]
        # get column & loop over all values
        group = feature_values>=value
        return self.FI_from_group( group )
         
    def get_split( self ):
        ''' determine where to split the features
        '''

        # loop over the features ... assume the features consists of rows with [x1, x2, ...., xN]
        self.split_i_feature, self.split_value, self.split_score, self.split_left_group = None, float('nan'), 0, None

        # loop over features
        for i_feature in range(len(self.features[0])):
            feature_values = self.features[:,i_feature]
            # get column & loop over all values
            for value in feature_values:
                left_group = feature_values<value
                DFI =  self.FI_from_group(  left_group )
                DFI += self.FI_from_group( ~left_group )
                if DFI > self.split_score:
                    self.split_i_feature = i_feature
                    self.split_value     = value
                    self.split_score     = DFI
                    self.split_left_group= left_group

        #print ("final:get_split", self.split_i_feature, self.split_value)
        #return {'split_i_feature':split_i_feature, 'split_value':split_value, 'split_score':split_score, 'split_left_group':split_left_group}

    def get_split_fast( self ):
        ''' determine where to split the features
        '''

        # loop over the features ... assume the features consists of rows with [x1, x2, ...., xN]
        self.split_i_feature, self.split_value, self.split_score, self.split_left_group = None, float('nan'), 0, None

        # loop over features
        for i_feature in range(len(self.features[0])):
            feature_values = self.features[:,i_feature]

            weight_sum = np.zeros(len(self.weights[0]))
            weight_sums= []
            for position, value in sorted(enumerate(feature_values), key=operator.itemgetter(1)):
                weight_sum = weight_sum+self.weights[position]
                weight_sums.append( (value,  weight_sum) )

            total_weights = weight_sums[-1][1]
            for value, weight_sum in weight_sums:
                #print weight_sum, total_weights-weight_sum
                score = self.FI_func(weight_sum) + self.FI_func( total_weights-weight_sum )
                if score > self.split_score: 
                    self.split_i_feature = i_feature
                    self.split_value     = value
                    self.split_score     = score

        self.split_left_group = self.features[:,i_feature]<=self.split_value
 

    # Create child splits for a node or make terminal
    def split(self, depth):

        # Find the best split
        #tic = time.time()
        #self.get_split()
        self.get_split_fast()
        #toc = time.time()

        #print("get_split in {time:0.4f} seconds".format(time=toc-tic))


        # check for max depth or a 'no' split
        if  self.max_depth <= depth+1 or (not any(self.split_left_group)) or all(self.split_left_group): # Jason Brownlee starts counting depth at 1, we start counting at 0, hence the +1
            #print ("Choice2", depth, self.FI_from_group(self.split_left_group), self.FI_from_group(~self.split_left_group) )
            # The split was good, but we stop splitting further. Put the result of the split in the left/right boxes.
            self.left, self.right = ResultNode(self.FI_from_group(self.split_left_group)), ResultNode(self.FI_from_group(~self.split_left_group))
            return
        # process left child
        if np.count_nonzero(self.split_left_group) <= min_size:
            #print ("Choice3", depth, self.FI_from_group(self.split_left_group) )
            # Too few events in the left box. We stop.
            self.left             = ResultNode(self.FI_from_group(self.split_left_group))
        else:
            #print ("Choice4", depth )
            # Continue splitting left box. 
            self.left             = Node(self.features[self.split_left_group], self.weights[self.split_left_group], FI_func=self.FI_func, max_depth=self.max_depth, min_size=self.min_size, depth=self.depth+1 )
        # process right child
        if np.count_nonzero(~self.split_left_group) <= min_size:
            #print ("Choice5", depth, self.FI_from_group(~self.split_left_group) )
            # Too few events in the right box. We stop.
            self.right            = ResultNode(self.FI_from_group(~self.split_left_group))
        else:
            #print ("Choice6", depth  )
            # Continue splitting right box. 
            self.right            = Node(self.features[~self.split_left_group], self.weights[~self.split_left_group], FI_func=self.FI_func, max_depth=self.max_depth, min_size=self.min_size, depth=self.depth+1 )

#    # Prediction    
#    def predict( self, row ):
#        ''' obtain the result by recursively descending down the tree
#        '''
#        node = self.left if row[self.split_i_feature]<self.split_value else self.right
#        if isinstance(node, ResultNode):
#            return node.return_value
#        else:
#            return node.predict(row)

    # Print a decision tree
    def print_tree(self, depth=0):
        print('%s[X%d <= %.3f]' % ((self.depth*' ', self.split_i_feature, self.split_value)))
        for node in [self.left, self.right]:
            node.print_tree(depth+1)

    def total_FI(self):
        result = 0
        for node in [self.left, self.right]:
            result += node.return_value if isinstance(node, ResultNode) else node.total_FI()
        return result

class ResultNode:
    ''' Simple helper class to store result value.
    '''
    def __init__( self, return_value ):
        self.return_value   = return_value
    def print_tree(self, depth=0):
        print('%s[%s]' % (((depth)*' ', self.return_value)))

import uproot
import awkward
import numpy as np
import pandas as pd

input_file  = "/eos/vbc/user/robert.schoefbeck/TMB/bit/MVA-training/ttG_WG_small/WGToLNu_fast/WGToLNu_fast.root"
upfile      = uproot.open( input_file )
tree        = upfile["Events"]
n_events    = len( upfile["Events"] )
n_events    = min(10000, n_events)
entrystart, entrystop = 0, n_events 

# Load features
branches    = [ "mva_photon_pt", ]#"mva_photon_eta", "mva_photonJetdR", "mva_photonLepdR", "mva_mT" ]
df          = tree.pandas.df(branches = branches, entrystart=entrystart, entrystop=entrystop)
features    = df.values

# Load weights
from Analysis.Tools.WeightInfo import WeightInfo
w = WeightInfo("/eos/vbc/user/robert.schoefbeck/gridpacks/v6/WGToLNu_reweight_card.pkl")
w.set_order(2)

# Load all weights and reshape the array according to ndof from weightInfo
weights     = tree.pandas.df(branches = ["p_C"], entrystart=entrystart, entrystop=entrystop).values.reshape((-1,w.nid))

min_size = 50

assert len(features)==len(weights), "Need equal length for weights and features."

FI_func = lambda coeffs: w.get_fisherInformation_matrix( coeffs, variables = ['cWWW'], cWWW=1)[1][0][0]

#node       = Node( features, weights, FI_func=FI_func, max_depth=1, min_size=min_size )

for max_depth in range(1,5):
    node       = Node( features, weights, FI_func=FI_func, max_depth=max_depth, min_size=min_size )
    print "max_depth", max_depth
    print 
    node.print_tree()
    print 
    print "Total FI", node.total_FI() 
    print 
    print 
