# vscode extension
jupyter, python extension 

conda create -n nipa-google python=3.12
conda env list
conda env remove -n “nipa-google”
conda activate nipa-google
conda deactivate

brew install python3.11
python -m pip install --upgrade pip
python3.11 -m venv .venv
source .venv/bin/activate
pip3.11 install "tensorflow==2.17.*" "tensorflow-metal==1.1.0" 
pip3.11 install "tensorboard==2.17.*"
pip3.11 install scikit-learn
pip3.11 install pandas
pip3.11 install matplotlib
pip3.11 install gensim

pip install "tensorflow==2.17.*" "tensorflow-metal==1.1.0"