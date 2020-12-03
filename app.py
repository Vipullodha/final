from flask import Flask,render_template,request
import pickle
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        val1=int(request.form["val1"])
        val2=int(request.form["val2"])
        val3=int(request.form["val3"])
        val4=int(request.form["val4"])
        val5=int(request.form["val5"])
        val6=int(request.form["val6"])
        val7=int(request.form["val7"])
        val8=int(request.form["val8"])
        val9=int(request.form["val9"])
        val10=int(request.form["val10"])
        val11=int(request.form["val11"])
        with open('my_model','rb') as f:
          model = pickle.load(f)


        result = model.predict([[val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11]])
        return str(result[0])


           

       
    else :
        return "somrthing went wrong"
app.run(host='0.0.0.0',debug= True)