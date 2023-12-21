echo "所有参数: $@"
if [ -z "Phishpedia" ]; then
  echo "Package Phishpedia not found in the Conda environment myenv."
  exit 1
else
  # 判断是否存在第一个参数，此处仅判断有无缓存，存在参数则表示有缓存
  if [ -z "$1" ]; then
    echo "Going to the directory of package Phishpedia in Conda environment myenv."
    mkdir -p "phishpedia/src/detectron2_pedia/output/rcnn_2"
    cd "phishpedia/src/detectron2_pedia/output/rcnn_2" || exit 1
    pip install gdown
    download_file_1=$(gdown --id 1tE2Mu5WC8uqCxei3XqAd7AWaP5JTmVWH)
    check_string_contains_error "$download_file_1" 1
    mkdir -p "phishpedia/src/siamese_pedia/"
    cd "phishpedia/src/siamese_pedia/" || exit 1

    download_file_2=$(gdown --id 1H0Q_DbdKPLFcZee8I14K62qV7TTy7xvS)
    check_string_contains_error "$download_file_2" 2

    download_file_3=$(gdown --id 1fr5ZxBKyDiNZ_1B6rRAfZbAHBBoUjZ7I)
    check_string_contains_error "$download_file_3" 3

    download_file_4=$(gdown --id 1qSdkSSoCYUkZMKs44Rup_1DPBxHnEKl1)
    check_string_contains_error "$download_file_4" 4
  else
    echo "Cache loaded, no need to download files from google drive"
  fi
fi