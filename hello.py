
# coding: utf-8

# In[1]:


from flask import Flask
app = Flask(__name__)


# In[2]:


@app.route('/')
def hello_world():
    return 'Hello, World!'

