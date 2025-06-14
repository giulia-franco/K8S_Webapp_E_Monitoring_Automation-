# Importa il modulo flask
from flask import Flask

# Creazione istanza app falsk
app = Flask(__name__)

# Definizione rotta
# La funzione hello() viene eseguita quando un utente visita la home page
@app.route('/')
def site():
    return "Questo è un progetto DevOps completo con K8s, Helm, Jenkins, e monitoring!!" 

# Avviare il server solo se si sta eseguendo questo file 
# Server accessibile da qualsiasi indirizzo IP sulla porta 8000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)