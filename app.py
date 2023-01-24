from flask import Flask,jsonify,request
import pandas as pd
import numpy as np                 # Numerical Python package 
import re
import json
import pdfx,pikepdf
import operator as op
import sys
from bsr_copy import bank_statement_read
from werkzeug.utils import secure_filename
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore") 
app = Flask(__name__)
@app.route("/test")
def indiment():
    return jsonify({"Message":"Hellow User, API is Wornking."})

	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
    api_file = "working_file.pdf"
    api_file_pass= "working_pass_file.pdf"
    bank_name = request.form["bank_name"]
    password = request.form["password"]
    password=str(password)
    f = request.files['file']
    f.save(secure_filename(api_file))
    try:
        if len(password) > 3:
            with pikepdf.open(api_file,password=password) as pdf:
                pdf.save(secure_filename(api_file_pass))
    except:
        resp = jsonify({'message' : 'Incorrect PDF PassWord'})
        resp.status_code = 400
        return resp 

    if len(password) < 3:
        bank_data=bank_statement_read(api_file, bank_name)
    else:
        bank_data=bank_statement_read(api_file_pass, bank_name)
    return bank_data
   else:
    resp = jsonify({'message' : 'Allowed file types are pdf'})
    resp.status_code = 400
    return resp 


if __name__ == "__main__":
    app.run(debug= True)