#!/bin/sh

python genPostProcessing.py --delphesEra RunII --targetDir v8 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ttZ01j #SPLIT600
python genPostProcessing.py --delphesEra RunII --targetDir v8 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WZTo3L1Nu #SPLIT600
python genPostProcessing.py --delphesEra RunII --targetDir v8 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ZZ #SPLIT600

#python genPostProcessing.py --targetDir v6 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ttG_noFullyHad_test #SPLIT10
#python genPostProcessing.py --targetDir v6 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ttg_noFullyHad_test2 #SPLIT10

#python genPostProcessing.py --targetDir v7 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ttG_noFullyHad #SPLIT200
#python genPostProcessing.py --targetDir v7 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ttW01j #SPLIT200
#python genPostProcessing.py --targetDir v7 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ttZ01j #SPLIT200
#python genPostProcessing.py --targetDir v7 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WGToLNu #SPLIT200
#python genPostProcessing.py --targetDir v7 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ZGTo2L #SPLIT200
#python genPostProcessing.py --targetDir v7 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WZTo3L1Nu #SPLIT200
#python genPostProcessing.py --targetDir v7 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WW #SPLIT200
#python genPostProcessing.py --targetDir v7 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ZZ #SPLIT200

#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ttg_noFullyHad #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ttZ01j #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ttW01j #SPLIT200
#
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WW #SPLIT100
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WZ #SPLIT100
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ZZ #SPLIT100
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WA #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WA_LO #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WAjj #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WWjj_OS #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WWjj_SS #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WZjj #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ZA #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ZAjj #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ZZjj #SPLIT200
#
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WWW #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WWZ #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample WZZ #SPLIT200
#python genPostProcessing.py --targetDir v4 --overwrite --addReweights --logLevel INFO --interpolationOrder 2  --sample ZZZ #SPLIT200
