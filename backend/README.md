Opcion 1:

Ve a la carpeta del backend:

cd ~/deleitate-app/backend
Ejecuta:

sudo docker build -t deleitate-backend .
sudo docker run -p 5000:5000 deleitate-backend



Opcion 2:

Ve a la carpeta del backend:

cd ~/deleitate-app/backend
Activa tu entorno virtual:


source ../env/bin/activate


⚠️ Si no existe el entorno, créalo así:


python3 -m venv ../env
source ../env/bin/activate
pip install -r requirements.txt
Corre el servidor Flask:


python app.py