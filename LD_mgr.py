from DBconnection import DBconnection
from LoginDetails import LoginDetails
import hashlib, secrets

class LD_mgr:
    def create_user(self, user:LoginDetails):
        db = DBconnection()
        strquery = f"insert into LoginDetails (UUID, Username, Password) values('{user.getuuid()}','{user.getusername()}','{user.getpassword()}')"
        kq = db.Execute(strquery)
        strquery = f"insert into SaltTable (UUID, Salt) values('{user.getuuid()}','{user.getsalt()}')"
        kq2 = db.Execute(strquery)
        strquery = f"insert into DataTable (UUID, Data) values('{user.getuuid()}','{user.getdata()}')"
        kq3 = db.Execute(strquery)
        if kq == True and kq2 == True and kq3 == True:
            print("them thanh cong")
        else:
            print("them khong thanh cong")
            
    def Check_user_return_data(self, tmpname, tmppass):
        try:
            db = DBconnection()
            strquery = f"SELECT UUID FROM LoginDetails WHERE Username = '{tmpname}'"
            User = db.Return(strquery)
            tmpu = str(User[0])
            strquery = f"SELECT Password FROM LoginDetails WHERE UUID = '{tmpu}'"
            Pass = db.Return(strquery)
            tmpp = str(Pass[0])
            strquery = f"SELECT Salt FROM SaltTable WHERE UUID = '{tmpu}'"
            Salt = db.Return(strquery)
            tmps = str(Salt[0])
            tmp = tmppass + tmps
            if secrets.compare_digest(tmpp, hashlib.sha3_512(tmp.encode()).hexdigest()):
                strquery = f"SELECT Data FROM DataTable WHERE UUID = '{tmpu}'"
                Data = db.Return(strquery)
                return str(Data[0])
            else:
                return "thong tin sai"
        except Exception:
            return "thong tin sai"