
# coding: utf-8

# In[11]:


from flask import Flask
app = Flask(__name__)


# In[12]:


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

