from flask import *
import os,time
from tabula import read_pdf,convert_into
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("upload.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        if (str(f.filename)[-4:]).upper() =='.PDF':
            output_name=str(f.filename)[:-4]+str(time.time())+".csv"
            convert_into(f,output_name,output_format="csv",pages="all")
            
            return send_from_directory(directory=os.getcwd(),filename=output_name,as_attachment=True)
        else:
            return "<h1> Upload PDF files only!!</h1>"

  
if __name__ == '__main__':  
    app.run(debug = True)  
