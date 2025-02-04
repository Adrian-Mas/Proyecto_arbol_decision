from flask import Flask, request, render_template
from pickle import load 

app = Flask(__name__)

model = load(open(/workspaces/Proyecto_arbol_decision/src/decision_tree_clasiffier_diabetes), "rb")


