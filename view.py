from flask import Flask, redirect, url_for, request,render_template,session
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = "C:\\git\\cavisson\\automation\stub\\testcases"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
check=os.path.isdir(UPLOAD_FOLDER)
if not check:
    os.makedirs(UPLOAD_FOLDER)
      
@app.route("/",methods=['GET', 'POST'])
def index():
      
      if request.method == 'POST':
            
            if 'file' not in request.files:
                  flash('No file part')
                  return redirect(request.url)      
            file = request.files['file']
            if file.filename == '':
                  flash('No selected file')
                  return redirect(request.url)
            if file :
                  filename = secure_filename(file.filename)
                  file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      listoffiles=os.listdir(UPLOAD_FOLDER)

      return render_template('index.html',listoffiles=listoffiles,check=check)


if __name__ == '__main__':
   app.secret_key = 'aloukik'
   app.run(debug = True)