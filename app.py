from flask import Flask
from rdkit import Chem
from rdkit.Chem import Draw

app = Flask(__name__)

@app.route("/")
def drawMolecule():
	return "Hello Molecula!"

if __name__ == "__main__":
	app.run(debug=True)