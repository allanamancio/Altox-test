from flask import Flask
from rdkit import Chem
from rdkit.Chem import Draw

app = Flask(__name__)

@app.route("/")
def drawMolecule():
	SMILES = 'CCOCCNSC=O'
	Img = Draw.MolToImage(Chem.MolFromSmiles(SMILES))
	Img.show()
	return "Hello, molecula."

if __name__ == "__main__":
	app.run(debug=True)