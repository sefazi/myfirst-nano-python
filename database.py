from service.proto import getlist_pb2 as getlist_pb2
from service.proto import getlist_pb2_grpc as getlist_pb2_grpc
import mysql.connector

def GetList(self, request, context):
    mydb = mysql.connector.connect(
        host="localhost",
        user="bebek",
        password="P@ssw0rd",
        database="python"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT name, address, age FROM users WHERE name =%s", (request.Name,))
    myresult = mycursor.fetchone()
    response = getlist_pb2.GetListResponse()
    
    if myresult is None:
        return response
    else:
        response = getlist_pb2.GetListResponse(
            Name    = myresult[0],
            Address = myresult[1],
            Age     = myresult[2]
        )
        return response