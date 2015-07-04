from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Credentials
 
engine = create_engine('sqlite:///peedith.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

def queryEntry(un):
    try:
        query =session.query(Credentials).filter(Credentials.userName == un).one()
        return query
    except:
        return False
    
def addEntry(un, pwd):
    if queryEntry(un) is False:
        new_credential = Credentials(userName=un, password=pwd)
        session.add(new_credential)
        session.commit()
        return True
    else:
        return False

def showAllusers():
    query =session.query(Credentials).all()
    users = []
    for i in query:
        users.append(str(i.userName))
    return users
    
def delUser(un):
    query = queryEntry(un)
    if query is not False:
        session.delete(query)
        session.commit()
        return True
    else:
        return False

def validatePassword(query, pwd):
    if pwd == str(query.password):
        return True
    else:
        return False

def changePassword(un, pwd):
    query=queryEntry(un)
    if query is not False:
        if pwd == str(query.password):
            newPwd = raw_input(" Enter New password : ")
            newPwdCheck = raw_input(" Enter password again to verify : ")
            if newPwd.rstrip('\n')==newPwdCheck.rstrip('\n'):
                query.password = newPwd.rstrip('\n')
                return True
            else:
                print "Type properly dumbo"
                return False
        else:
            print "Wrong password"
            return False
    else:
        print "U dont belong here with this name"
        return False

if __name__ == "__main__":
    query = queryEntry("judo")
    if query is not False:
        if validatePassword(query, "ipedu") is True:
            print "Access Granted"
        else:
            print "Access Denied! :p"
            reply = raw_input("I can tell you the password if you want! What you say? Yay or Nay?" )
            if reply.rstrip('\n') == "yay":
                print query.password
            else:
                print "Poda naye!"
    else:
        print "Username Incorrect!"