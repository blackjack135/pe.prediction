#!/usr/bin/env python
# coding: utf-8

# In[16]:


from flask import Flask,request,render_template


# In[17]:


import joblib


# In[18]:


app = Flask(__name__)


# In[19]:


@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        beta = float(request.form.get("beta"))
        print(beta)
        model1 = joblib.load("regression")
        r1 = model1.predict([[beta]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[beta]])
        return(render_template("index.html",result1=r1,result2=r2))
    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))


# In[ ]:


if __name__ ==  "__main__":
    app.run()


# In[ ]:




