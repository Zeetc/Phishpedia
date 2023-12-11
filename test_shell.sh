if command -v nvcc || command -v nvidia-smi &> /dev/null; then
  echo "CUDA is detected, installing GPU-supported PyTorch and torchvision."
fi
package_location=$(pip show phishpedia | grep Location | awk '{print $2}')

cd "$package_location/phishpedia/src/detectron2_pedia/output/rcnn_2" || exit
pip install gdown
gdown --id 1tE2Mu5WC8uqCxei3XqAd7AWaP5JTmVWH
cd "$package_location/phishpedia/src/siamese_pedia/" || exit
gdown --id 1H0Q_DbdKPLFcZee8I14K62qV7TTy7xvS
gdown --id 1fr5ZxBKyDiNZ_1B6rRAfZbAHBBoUjZ7I
gdown --id 1qSdkSSoCYUkZMKs44Rup_1DPBxHnEKl1