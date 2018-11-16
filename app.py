from flask import Flask, render_template
from rdkit import Chem
from rdkit.Chem import Draw

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello! Put your SMILES in URL so we can draw your molecule :)."

@app.route("/<SMILES>")
def drawMolecule(SMILES):
	Img = Draw.MolToImage(Chem.MolFromSmiles(SMILES))
	Img.save("static/" + SMILES + ".jpg")
	return render_template("molecule.html", smiles=SMILES)

if __name__ == "__main__":
	app.run(debug=True)	