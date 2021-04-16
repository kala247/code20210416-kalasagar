

import json

def BMI_calc(data):
    
    for i in data:
        BMI = round(i["WeightKg"]/(i['HeightCm']/100)**2,2)
        if BMI <= 18.5:
            
            i['BMI'] = BMI
            i['BMICategory']="Underweight"
            i['HealthRisk']='Malnutrition risk'
            
        elif BMI<=24.9 :
            i['BMI'] = BMI
            i['BMICategory']="Normal weight"
            i['HealthRisk']='Low risk'
            
        elif BMI<=29.9  :
            i['BMI'] = BMI
            i['BMICategory']="Overweight"
            i['HealthRisk']='Enhanced risk'
            
        elif BMI<=34.9 :
            i['BMI'] = BMI
            i['BMICategory']="Moderately obese"
            i['HealthRisk']='Medium Risk'
        elif BMI<= 39.9 :
            i['BMI'] = BMI
            i['BMICategory']="Severely obese"
            i['HealthRisk']='High Risk'
            
        else:
            i['BMI'] = BMI
            i['BMICategory']="Very Severely obese"
            i['HealthRisk']='Very High Risk'

    return data
    
if __name__=="__main__":

    f = open ("testdata.json",'r')
    pdata =  json.load(f)
    data = pdata["data"]
    data = BMI_calc(data)
    print(data)
    overwt_person_count=0
    for j in data:
        if 29.9 >= j["BMI"] >=25:
            overwt_person_count+=1
    print("Overweight Persons Count : ",overwt_person_count)


