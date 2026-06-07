git clone https://github.com/lucianoVillanuevaR/Clasificacion-Flores.git
cd Clasificacion-Flores

git checkout develop

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python3 main.py
