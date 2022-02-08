import json

class BMI:
    bmi_class ={ 'U-W' :'Underweight',
                    'N-W': 'Normal Weight',
                    'O-W': 'Over Weight',
                    'M-O': 'Moderately obese',
                    'S-O': 'Severly obese',
                    'V-SO': 'Very Severly obese',
                   }

    health_risk = {
                    'M-R':'Malnutrition Risk',
                    'L-R': 'Low Risk',
                    'E-R': 'Enhanced Risk',
                    'M-RS': 'Medium Risk',
                    'H-R': 'High Risk',
                    'V-HR': 'Very High Risk',
    }


# New
def dataload():
    row_index = []
    with open('BMI_Data.json') as file:
        allrecords = json.reader(file)
        for row in allrecords:
            row_index.append(row)
        return row_index


def data_bmi(TotalData):
    record_compute = 0
    Incorrect_data = []
    correct_data = []
    for row in TotalData:
        if record_compute == 0:
            record_compute = 1
        elif row[0].isalpha() == True and row[1].isnumeric() == True and row[2].isnumeric() == True :
            bmi = Measure_Bmi(row)
            correct_data.append(row+bmi)
            record_compute +=1
        else:
            Incorrect_data.append(row)
            record_compute +=1 
    return correct_data


def Measure_Bmi(data):
    BMI_class= None
    Health_risk= None
    BMI_limit = None
    a =int(data[1])
    b = int(data[2])
    bmi = b/((a/100)**2)
    if bmi <= 18.4 :
        BMI_class = BMI.bmi_class.get('U-W')
        BMI_limit = bmi
        Health_risk = BMI.health_risk.get('M-R')
    elif bmi >=18.5 and bmi <= 24.9:
        BMI_class = BMI.bmi_class.get('N-W')
        BMI_limit = bmi
        Health_risk = BMI.health_risk.get('L-R')
    elif bmi >=25 and bmi <= 29.9:
        BMI_categoty = BMI.bmi_class.get("O-W")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('E-R')
    elif bmi >=30 and bmi <= 34.9:
        BMI_categoty = BMI.bmi_class.get("M-O")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('M-RS')
    elif bmi >= 35 and bmi <= 39.9:
        BMI_categoty = BMI.bmi_class.get("S-O")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('H-R')
    elif bmi > 40:
        BMI_categoty = BMI.bmi_class.get("V-SO")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('V-HR')
    bmi_Index =[BMI_class,BMI_limit,Health_risk]
    return bmi_Index


def write_json(data):
    with open('BMI_Output_Height_Weight.json', 'w',newline='') as file:
        json_data = json.writer(file, delimiter=',')
        json_data.writerow(['Gender', 'Height', 'Weight', 'BMI_class', 'BMI_limit', 'Health_risk'])
        for row in data: 
            json_data.writerows([row])
    return 'json file Complete'


if __name__ == '__main__':
    ImportData = dataload()
    # print(result)
    Maindata = data_bmi(ImportData) 
    EndResult = write_json(Maindata)
    print(EndResult)
