# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

#!/bin/sh
#mkdir data
#wget https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.$1.vec -P data
#wget https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.$2.vec -P data
#wget https://dl.fbaipublicfiles.com/arrival/dictionaries/$1-$2.5000-6500.txt -P data
#wget https://dl.fbaipublicfiles.com/arrival/dictionaries/$2-$1.5000-6500.txt -P data

wget https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.$2.vec -P data
wget https://dl.fbaipublicfiles.com/arrival/dictionaries/$1-$2.5000-6500.txt -P data
wget https://dl.fbaipublicfiles.com/arrival/dictionaries/$2-$1.5000-6500.txt -P data