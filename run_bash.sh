#!/bin/bash

if ! conda info --envs | grep -q "Phishpedia"; then
  echo "The Phishpedia Conda environment does not exist."
  exit 1
fi

source activate Phishpedia
python ./phishpedia/test.py
