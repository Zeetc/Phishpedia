#!/bin/bash
FILEDIR=$(pwd)
CONDA_BASE=$(conda info --base)
source "$CONDA_BASE/etc/profile.d/conda.sh"

if ! conda info --envs | grep -q "Phishpedia"; then
  echo "The Phishpedia Conda environment does not exist."
  exit 1
fi

conda activate Phishpedia
python ./phishpedia/test.py
