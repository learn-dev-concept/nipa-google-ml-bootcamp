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
pip install tensorflow tensorflow-metal tensorboard scikit-learn pandas matplotlib gensim transformers tf_keras 'transformers[torch]'