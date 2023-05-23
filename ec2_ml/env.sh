#! bin/bash/

sudo yum install git
git clone https://github.com/Tatsuki-Oike/aws.git

python3 -m venv venv
source venv/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
python3 -m pip install jupyterlab