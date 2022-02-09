# Unit Testing Document

# Total data points
[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

# Test cases
#Enter the below input in the Web page
1. {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }

BMI = 96/(1.71*1.71)
BMI = 32.83

30 < BMI < 34.9

'Moderately obese'

#Enter the below input in the Web page
2. {"Gender": "Male", "HeightCm": 161, "WeightKg": 85 }

BMI = 85/(1.61*1.61)
BMI = 32.79

30 < BMI < 34.9

'Moderately obese'

#Enter the below input in the Web page
3. {"Gender": "Male", "HeightCm": 180, "WeightKg": 77  }

BMI = 77/(1.80*1.80)
BMI = 23.77

18.5 < BMI < 24.9 

'Normal weight'


#Enter the below input in the Web page
4. {"Gender": "Female", "HeightCm": 166, "WeightKg": 62 }

BMI = 62/(1.66*1.66)
BMI = 22.5

18.5 < BMI < 24.9 

'Normal weight

#Enter the below input in the Web page
5. {"Gender": "Female", "HeightCm": 150, "WeightKg": 70 }

BMI = 70/(1.5*1.5)
BMI = 31.11

30 < BMI < 34.9

'Moderately obese'

#Enter the below input in the Web page
6. {"Gender": "Female", "HeightCm": 167, "WeightKg": 82 }

BMI = 82/(1.67*1.67)
BMI = 29.4

25 < BMI < 29.9 

'Overweight'


# Total Counts - match it with the dashboard numbers

'Moderately obese count' = [1,2,5] = 3
'Normal weight count' = [3,4] = 2
'Overweight count' = [6] = 1
'Underweight count' = 0
'Severely obese count' = 0
'Very Severely obese count' = 0


