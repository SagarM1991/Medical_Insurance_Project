from flask import Flask,jsonify,request,render_template
import config

from project.utils import MedicalInsurance

app = Flask(__name__)

##########################################################################################
#########################    HOME API     ###############################################
##########################################################################################
@app.route('/') # HOme API
def my_fun():
    return render_template("home.html")


@app.route("/predict_charges", methods= ["post"])

def get_insurance_charges():
    data = request.form
    print("Data Is :",data)

    age = eval(data['age'])  
    sex = data['gender']
    bmi = eval(data['bmi'])
    children = eval(data['children'])
    smoker = data['smoker']
    region = data['region']

    print("age,sex,bmi,children,smoker,region >>",age,sex,bmi,children,smoker,region)

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges  = med_ins.get_predict_chagres()
    # return jsonify({"Result" : f"Predicted Medical insurance Charges are {charges}"})
    return render_template("view_result.html", charges=charges)



app.run(port = config.PORT_NUMBER,debug = True ) # Server Start