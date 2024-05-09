from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
import pickle 


def home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Logout(request):
    logout(request)
    return redirect('login')

def prediction(request):
    if request.method == 'GET':
        print("inside if")
        return render(request, 'home.html')
    else:
        
        print("inside else")
        val1 = float(request.POST.get('age'))
        val2 = float(request.POST.get('sex'))
        val3 = float(request.POST.get('cp'))
        val4 = float(request.POST.get('trestbps'))
        val5 = float(request.POST.get('chol'))
        val6 = float(request.POST.get('fbs'))
        val7 = float(request.POST.get('restecg'))
        val8 = float(request.POST.get('thalach'))
        val9 = float(request.POST.get('exang'))
        val10 = float(request.POST.get('oldpeak'))
        val11 = float(request.POST.get('slope'))
        val12 = float(request.POST.get('ca'))
        val13 = float(request.POST.get('thal'))
        


        # Create a DataFrame from user input
        input_data = {
            "age": [val1],
            'sex': [val2],
            'cp': [val3],
            'trestbps': [val4],
            "chol": [val5],
            "fbs": [val6],
            "restecg": [val7],
            "thalach": [val8],
            "exang": [val9],
            "oldpeak": [val10],
            "slope": [val11],
            "ca": [val12],
            "thal": [val13],
        }

        input_df = pd.DataFrame(input_data)

        # Load the model
        # model = joblib.load("C:\Users\joshi\PycharmProjects\Cervical cancer prediction\CervicalCancer\CervicalCancer\model.sav")
        model=pickle.load(open(r"D:\HeartDisease\HeartDisease\HeartDisease\model5.sav", 'rb')) 

        # Make prediction
        prediction = model.predict(input_df)
        print("predict :::   ",prediction[0])

        if prediction[0] == 1:
          result1 = "Positive"
        else:
          result1 = "Negative"
        return render(request, 'home.html', {"result2": result1})