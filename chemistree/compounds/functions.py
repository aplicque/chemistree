from .models import *
import json
import requests
import ast
    #makes strings into dictionaries

def addcomp(ik):
    name = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/" + ik + "/property/IUPACname/txt")
    mf = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/" + ik + "/property/MolecularFormula/txt")
    mw = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/" + ik + "/property/MolecularWeight/txt")
    mfu = "g/mol"
    m = Molecule(name=name.text, formula=mf.text, molecular_weight=mw.text, mw_unit=mfu, inchikey=ik)
    m.save()

def addelem():
    per_table = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/JSON/?response_type=display")
    dict = ast.literal_eval(per_table.text)
    row_list = dict["Table"]["Row"]



    for element in row_list:
        name = element["Cell"][2]
        symbol = element["Cell"][1]
        am = element["Cell"][3]
        amu = "u"
        e = Element(name=name, symbol=symbol, atomic_mass=am, am_unit=amu)
        e.save()

