
# coding: utf-8

# In[21]:


#Upload using HTML templates
import os
from flask import Flask, render_template, request, flash, url_for, send_from_directory
app = Flask(__name__)
UPLOAD_FOLDER = 'C:\\Users\\mnatarajan\\Desktop\\Flask_API'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# In[22]:


@app.route('/')
def index():
    return render_template('upload.html')


# In[23]:


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        target = os.path.join(app.config['UPLOAD_FOLDER'], 'templates/')
        print(target)
        
        if not os.path.isdir(target):
            os.mkdir(target)
        else:
            print('[ERROR]: Could not create Upload Folder: {}'.format(target))
        print(request.files.getlist("file"))
        
        for upload in request.files.getlist("file"):
            print(upload)
            print("{} is the file name".format(upload.filename))
            filename = upload.filename
            # This is to verify files are supported
            ext = os.path.splitext(filename)[1]
            if (ext == ".jpg") or (ext == ".png"):
                print("File supported moving on...")
            else:
                render_template("Error.html", message="Files uploaded are not supported...")
            destination = "/".join([target, 'screen.jpg'])
            print("Accept incoming file:", filename)
            print("Save it to:", destination)
            upload.save(destination)
    
    return render_template("complete.html", image_name=filename)


# In[24]:


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


# In[25]:


@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('./images')
    print(image_names)
    return render_template("gallery.html", image_names=image_names)

