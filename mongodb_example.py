import pymongo
from random import randint

def get_choise():

  d = {
    0 : "admin",
    1 : "student",
    2 : "moderator"
  }
  return d[randint(0,2)]

def write_data():

  all_users = []
  for e in range(25):
    all_users.append({"login":"user"+str(e), "previlige": get_choise()})
  mycol.insert_many(all_users)

def get_data(db):

  cursor = db.find({"previlige": "student"})
  for student in cursor:
    print(student["login"], student["previlige"])
  
if __name__ == "__main__":

  myclient = pymongo.MongoClient("mongodb://root:example@127.0.0.1:27017/")
  mydb = myclient['check_db']
  mycol = mydb["users"]

  #write_data(mycol)
  get_data(mycol)