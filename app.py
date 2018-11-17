from flask import Flask, render_template
from rdkit import Chem
from rdkit.Chem import Draw
import base64
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello! Put your SMILES in URL so we can draw your molecule :). EXAMPLE: localhost:5000/CCOCCNSC=O"

@app.route("/<SMILES>")
def drawMolecule(SMILES):
	# Generates molecular image from SMILES
	Img = Draw.MolToImage(Chem.MolFromSmiles(SMILES))
	# Converts generated image to base64 encoding
	file = BytesIO()
	Img.save(file, format="JPEG")
	file.seek(0)
	Img64 = base64.encodestring(file.read()).decode()
	# Outputs image to HTML
	return render_template("molecule.html", image=Img64)

if __name__ == "__main__":
	app.run()