conda info --envs | grep -w "myenv" > /dev/null

if [ $? -eq 0 ]; then
   echo "Activating Conda environment myenv"
   conda activate myenv
else
   echo "Creating and activating new Conda environment $ENV_NAME with Python 3.8"
   conda create -n myenv python=3.8
   conda activate myenv
fi