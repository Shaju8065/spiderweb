import pymysql
from pymongo import MongoClient

class EmpOperations:
    def addnewemployee(self,custId,carType,custName,carName, cityName):
        status=None
        try:
            con=pymysql.connect(host='bwhi9tgmciqdnqidftqa-mysql.services.clever-cloud.com',user='ua76mfassmwczyly',password='Ydvss4Uh9wudTv7RCasm',database='bwhi9tgmciqdnqidftqa')
            curs=con.cursor()
            curs.execute("insert into employee(cstId,car,cstNm,carNm, cityNm) values('%.2f','%s','%s','%s', '%s')" %(custId, carType, custName, carName, cityName))
            con.commit()
            con.close()
            status='success'
        except:
            status='error'
        
        return status
    
    def getreportdata(self):
        con=pymysql.connect(host='b7ynlwm9vi4twzsxsu9f-mysql.services.clever-cloud.com',user='udsypi8l3ys4ac0q',password='A4qUKkNz34O2aiQ46dk6',database='b7ynlwm9vi4twzsxsu9f')
        curs=con.cursor()
        curs.execute("select * from employee")
        data=curs.fetchall()
        return data
    

    def addnewworker(self,id,nm,dp,ps,lo,sl):
        status=None
        try:
            client=MongoClient("mongodb+srv://sharayu:mongodb913@ethancluster.npsn31t.mongodb.net/?retryWrites=true&w=majority")
            db=client["praffulldb"]
            coll=db["workers"]
            dic={}
            dic['_id']=id
            dic['name']=nm
            dic['dept']=dp
            dic['post']=ps
            dic['location']=lo
            dic['salary']=sl

            coll.insert_one(dic)
            status='success'
        except Exception as err:
            print(err)
            status='error'
        
        return status

    def allworkers(self):
        client=MongoClient("mongodb+srv://sharayu:mongodb913@ethancluster.npsn31t.mongodb.net/?retryWrites=true&w=majority")
        db=client["praffulldb"]
        coll=db["students"]
        dic={}
        dic['data']=coll.find()
        return dic
