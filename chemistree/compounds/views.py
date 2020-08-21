from django.shortcuts import render
import requests
# Create your views here.
from .functions import *
from .models import *


def home(request):
    message = "Welcome to Chemistree! Click a link at the top to go to a page"

    content = {"message":message,}
    return render(request, "home.html", content)

def compounds(request):
    message = "Welcome to the Compounds page!"
    molecules = Molecule.objects.all()
    if request.method == "POST":
        inchikey = request.POST.get('inchikey')
        addcomp(inchikey)

    content = {"message": message, "molecules": molecules, }
    return render(request, "compounds/compounds.html", content)

def compinspect(request, compid):
    message = "Inspect"
    molecule = Molecule.objects.get(id=compid)
    m_e = molecule.elements.all()
    content = {"message": message, "molecule": molecule, "m_e":m_e }
    return render(request, "compounds/compinspect.html", content)

def elements(request):
    message = "Welcome to the Elements page!"
    elements = Element.objects.all()
    content = {"message": message, "elements": elements}
    return render(request, "compounds/elements.html", content)

def eleminspect(request, elemid):
    message = "Elements!"
    element = Element.objects.get(id=elemid)
    content = {"message": message, "element": element, }
    return render(request, "compounds/eleminspect.html", content)
