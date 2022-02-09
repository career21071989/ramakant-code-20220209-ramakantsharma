# Packages Required
# pip install pywebio

# importing modules
from pywebio.input import *
from pywebio.output import *
import sys, os
import json

# Update working directory to the path where Json file is placed in the local folder
os.chdir('A:/Vamstar/data')

def BMI_Main():
 
# Function for BMI Imputation
    def BMI_Imputation():
        # Load Json Data from the local directry
        with open('BMI.json', 'r') as c:
            params = json.load(c)   
        # Here I have taken the low value as 0 and for max evaluation as 50 but it will not impact the results
        BMI_Limit={0:[0,18.5],1:[18.5,24.9],2:[25,29.9],3:[30,34.9],4:[35,39.9],5:[40,50]}
        Health_Risk=["Malnutrition risk","Low risk","Enhanced risk","Medium risk","High risk","Very high risk"]
        BMI_Class=["Underweight","Normal weight","Overweight","Moderately obese","Severely obese","Very severely obese"]
        # Final Result will store here
        End_Result={}
        i=1
    
        for Item in params:
            BMI=Item["WeightKg"]/(Item["HeightCm"]/100)**2 
            for key in BMI_Limit:
                if key==5:
                    End_Result[i]=[BMI,Health_Risk[key],BMI_Class[key]]
                    break
                if BMI >= BMI_Limit[key][0] and BMI < BMI_Limit[key+1][0]:
                    End_Result[i]=[BMI,Health_Risk[key],BMI_Class[key]]
                    break
            i+=1

        return End_Result

    if __name__=='__main__':
        # Total Number of Overweighted person in the Data
        End_Result=BMI_Imputation()
        Overall_OverWgt_Count=0
        for key in End_Result:
            if "Overweight" in End_Result[key]:
                Overall_OverWgt_Count+=1
        print(End_Result)
        print(f"Total Number of Overweighted person {Overall_OverWgt_Count}")
    
        # Total Number of Moderately obese person in the Data
        End_Result1=BMI_Imputation()
        Overall_MO_Count=0
        for key in End_Result:
            if "Moderately obese" in End_Result[key]:
                Overall_MO_Count+=1
        #print(Final_Result1)
        print(f"Total Number of Moderately obese person {Overall_MO_Count}")
    
        # Total Number of Severely obese person in the Data
        End_Result2=BMI_Imputation()
        Overall_SO_Count=0
        for key in End_Result:
            if "Severely obese" in End_Result[key]:
                Overall_SO_Count+=1
        #print(Final_Result1)
        print(f"Total Number of Severely obese person {Overall_SO_Count}")
    
        # Total Number of Very severely obese person in the Data
        End_Result3=BMI_Imputation()
        Overall_VSO_Count=0
        for key in End_Result:
            if "Very severely obese" in End_Result[key]:
                Overall_VSO_Count+=1
        #print(Final_Result1)
        print(f"Total Number of Very severely obese person {Overall_VSO_Count}")
    
        # Total Number of Underweight person in the Data
        End_Result4=BMI_Imputation()
        Overall_UnderWgt_Count=0
        for key in End_Result:
            if "Underweight" in End_Result[key]:
                Overall_UnderWgt_Count+=1
        #print(Final_Result1)
        print(f"Total Number of Underweight person {Overall_UnderWgt_Count}")
    
        # Total Number of Normal weight person in the Data
        End_Result5=BMI_Imputation()
        Overall_NormalWgt_Count=0
        for key in End_Result:
            if "Normal weight" in End_Result[key]:
                Overall_NormalWgt_Count+=1
        #print(Final_Result1)
        print(f"Total Number of Normal weight person {Overall_NormalWgt_Count}")
    
    
    
############ Web Page Implementation Start #########################

    # classify person
    class calc:
  
        # defining method
        def BMI_Imputation1(Hgt, Wgt):
  
            for x, y in [(16, 'severely underweight'),
                           (18.5, 'underweight'),
                           (25, 'normal'),
                           (30, 'overweight'),
                           (35, 'moderately obese'),
                           (float('inf'), 'severely obese')]:
                if BMI <= x:
                    put_text('Your BMI is', BMI, 'and you are :', y)
                    break
  
    # classify and compute BMI
    class calc:
  
        # BMI Imputation function starts
        def BMI_Imputation1(self, Hgt, Wgt):
  
            # Calculate BMI
            BMI = round((Wgt)/(Hgt*Hgt),2)
  
            # Segregate
            for x, y in [(16, 'severely underweight'),
                           (18.5, 'underweight'),
                           (25, 'normal'), (30, 'overweight'),
                           (35, 'moderately obese'),
                           (float('inf'), 'severely obese')]:
  
                if BMI <= x:
                    put_text('Your BMI is', BMI, 'and you are :', y)
                    put_text('Total Number of Overweighted person in the Json File:', Overall_OverWgt_Count)
                    put_text('Total Number of Moderately obese person in the Json File:', Overall_MO_Count)
                    put_text('Total Number of Severely obese person in the Json File:', Overall_SO_Count)
                    put_text('Total Number of Very severely obese person in the Json File:', Overall_VSO_Count)
                    put_text('Total Number of Underweight person in the Json File:', Overall_UnderWgt_Count)
                    put_text('Total Number of Normal_weight person in the Json File:', Overall_NormalWgt_Count)
                    break
  
  
    # height input
    Hgt = input("Please enter height in meters(m)", type=FLOAT)
  
    # Weight input
    Wgt = input("Please enter Weight in Kilograms(Kg)", type=FLOAT)
  
    obj = calc()
    obj.BMI_Imputation1(Hgt, Wgt)

# Execute the BMI_Main function
BMI_Main()
