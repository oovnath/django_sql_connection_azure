import mysql.connector
import json
from mysql.connector import Error

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import responses
from rest_framework.parsers import JSONParser
from rest_framework import status

from django.conf import settings
from django.http import JsonResponse

host = 'mysql-166197-0.cloudclusters.net',
port = '19999',
user = 'admin',
password = 'RR7ediWs',
database  = 'любовь' 
table_names = ["sa_01","sa_02","sa_03","sa_04","sa_05","sa_06","sa_07","sa_08","sa_09","sa_10","sa_11","sa_12","sa_13","sa_14","sa_15","sa_16","sa_17","sa_18","sa_19","sa_20","sa_21","sa_22","sa_23","sa_24","sa_25","sa_26","sa_27","sa_28","sa_29","sa_30","sa_31","sa_32","sa_33","sa_34","sa_35","sa_36","sa_37","sa_38","sa_39","sa_40","sa_41","sa_42","sa_43","sa_44","sa_45"]
# mobile_num = "3330504649"
# mobile_num = "0"
# CNIC_num = "000001446"

mydb = mysql.connector.connect(
                host = 'mysql-166197-0.cloudclusters.net',
                port = '19999',
                user = 'admin',
                password = 'RR7ediWs',
                database  = 'любовь' 
            )
print("MySQL Database connection successful"),    
cursor = mydb.cursor()
data_json ={}

@api_view(['POST'])
def get_data(request):
    try:
            row={}
            if request.method == 'POST':
                print('POST')
                print(request)
                request_data = JSONParser().parse(request)
                print(request_data)
                mobile_input = request_data["mobile_number"]
                cicn_input = request_data["cicn_number"]
                
                # print(input)
                for table in table_names:
                    if mobile_input == "":
                        sql = f' SELECT * FROM `{table}` WHERE `CNIC` = {cicn_input} ;'
                    elif  cicn_input == "":
                      sql = f' SELECT * FROM `{table}` WHERE  `Mobile` = {mobile_input};'
                    else:
                      sql = f' SELECT * FROM `{table}` WHERE  `Mobile`={mobile_input} and `CNIC` = {mobile_input};'
                    
                    print(sql)
                    cursor.execute(sql)
                    print('courser execute')
                    result  = cursor.fetchone() 
                    print('data fetch')     
                    print(f"{table}: {result}")
                    # print(err)
                    if result is not None:
                        field_name = [field[0] for field in cursor.description]
                        row = dict(zip(field_name, result))
                        print(row)
                        
                        return JsonResponse({"result": row}, status = status.HTTP_200_OK)
                        # break

                if  result is None:  
                    return JsonResponse({"result": 'No data found'}, status = status.HTTP_200_OK) 

    except Error as err:
                print(f"Error: '{err}'")
                return JsonResponse({"result": err}, status = status.HTTP_400_BAD_REQUEST)

