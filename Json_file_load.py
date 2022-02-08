import json
 
# Data to be written
Data_BMI ={
    "Gender" : ["Male","Male","Male","Female","Female","Female","Female"],
    "HeightCm" : [171,161,180,166,150,167],
    "WeightKg" : [96,85,77,62,70,82] 
}
  
# Serializing json 
json_object = json.dumps(dictionary, indent = 4)
  
# Writing to sample.json
with open("Data_BMI.json", "w") as outfile:
    outfile.write(json_object)
    
