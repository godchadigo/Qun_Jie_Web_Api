from flask import Flask, json,request,jsonify
from flask_cors import CORS

from datetime import datetime as dt
from datetime import timedelta 
from datetime import timezone
from datetime import time

from flask_jwt_extended import (
    JWTManager, jwt_required,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    get_jwt
)

import pymysql as PYM
import json as Json
import uuid as Uuid
import jwt as JWT

# 資料庫參數設定
db_settings = Json.load(open('E:\\Web\\api\\config\\mysql.json'))

#My Api Secret
secret = Json.load(open('E:\\Web\\api\\config\\secret.json'))['Secret']

#USER Table Name
user_table = "user"
company_table = "company"
device_group_table = "devicegroup"
device_table = "device"

app = Flask(__name__)
CORS(app)

jwt = JWTManager()
app.config['JWT_SECRET_KEY'] = secret
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)
app.config['PROPAGATE_EXCEPTIONS'] = True

jwt.init_app(app)

@app.route('/')
def index():
    return 'Test'

#創建公司
@app.route('/api/CreateCompany' , methods=['POST'])
@jwt_required()
def create_company():
        uuid = str(Uuid.uuid4())
        connect = PYM.connect(**db_settings)
        company_name = request.json.get("CompanyName",None)
        number = request.json.get("Number",None)

        with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `company` WHERE `CompanyName` = '{company_name}'"
            cursor.execute(find_cmd)
            result = cursor.fetchall()
            if (any(result) == False):
                create_cmd = f"INSERT INTO `company`(`Uuid`, `CompanyName`, `Number`) VALUES ('{uuid}','{company_name}','{number}')"
                cursor.execute(create_cmd)
                connect.commit()
                return jsonify([{'Result' : "創建成功!"}])
            else:
                return jsonify([{'Result' : "公司已存在!"}])
        
#刪除公司
@app.route('/api/DeleteCompany' , methods=['DELETE'])
@jwt_required()
def delete_company():
        connect = PYM.connect(**db_settings)
        uuid = request.json.get("Uuid",None)

        with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `company` WHERE `Uuid` = '{uuid}'"
            cursor.execute(find_cmd)
            result = cursor.fetchall()
            if (any(result) == True):
                delete_cmd = f"DELETE FROM `company` WHERE `Uuid` = '{uuid}'"
                cursor.execute(delete_cmd)
                connect.commit()
                return jsonify([{'Result' : "刪除成功!"}])
            else:
                return jsonify([{'Result' : "公司不存在!"}])

#得取全部公司
@app.route('/api/GetAllCompany' , methods=['GET'])
def get_all_company():
        connect = PYM.connect(**db_settings)

        with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `company`"
            cursor.execute(find_cmd)
            result = cursor.fetchall()
            if (any(result) == True):
                data = []
                for row in result:
                    data.append({
                                 "Uuid" : row[0],
                                 "Company" : row[1],
                                 "Number" : row[2]
                                })
                return jsonify(data)
            else:
                return jsonify([{'Result' : "查無公司列表!"}])

#創建設備群組
@app.route('/api/CreateDeviceGroup' , methods=['POST'])
@jwt_required()
def create_device_group():
        connect = PYM.connect(**db_settings)

        device_group_name = request.json.get("DeviceGroupName",None)
        uuid = str(Uuid.uuid4())

        with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `devcicegroup` WHERE `GroupName` = '{device_group_name}'"
            cursor.execute(find_cmd)
            result = cursor.fetchall()
            if (any(result) == False):
                create_cmd = f"INSERT INTO `devcicegroup`(`Uuid`, `GroupName`) VALUES ('{uuid}','{device_group_name}')"
                cursor.execute(create_cmd)
                connect.commit()
                return jsonify([{'Result' : "創建成功!"}])
            else:
                return jsonify([{'Result' : "設備列表已存在!"}])

#刪除設備群組
@app.route('/api/DeleteDeviceGroup' , methods=['DELETE'])
@jwt_required()
def delete_device_group():
        connect = PYM.connect(**db_settings)

        uuid = request.json.get("Uuid",None)
        

        with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `devcicegroup` WHERE `Uuid` = '{uuid}'"
            cursor.execute(find_cmd)
            result = cursor.fetchall()
            if (any(result) == True):
                delete_cmd = f"DELETE FROM `devcicegroup` WHERE `Uuid` = '{uuid}'"
                cursor.execute(delete_cmd)
                connect.commit()
                return jsonify([{'Result' : "刪除成功!"}])
            else:
                return jsonify([{'Result' : "設備列表不存在!"}])

#得取全部設備群組
@app.route('/api/GetAllDeviceGroup' , methods=['GET'])
def get_all_device_group():
        connect = PYM.connect(**db_settings)

        with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `devcicegroup`"
            cursor.execute(find_cmd)
            result = cursor.fetchall()
            if (any(result) == True):
                data = []
                for row in result:
                    data.append({
                                 "Uuid" : row[0],
                                 "GroupName" : row[1]
                                })
                return jsonify(data)
            else:
                return jsonify([{'Result' : "查無設備列表!"}])

#創建設備
@app.route('/api/CreateDevice' , methods=['POST'])
@jwt_required()
def create_device():
        connect = PYM.connect(**db_settings)

        device_id = request.json.get("DeviceId",None)
        device_name = request.json.get("DeviceName",None)
        device_group_id = request.json.get("DevciceGroupId",None)
        company_id = request.json.get("CompanyId",None)

        uuid = str(Uuid.uuid4())

        with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `device` WHERE `DeviceName` = '{device_name}'"
            cursor.execute(find_cmd)
            result = cursor.fetchall()
            if (any(result) == False):
                create_cmd = f"INSERT INTO `device`(`Uuid`, `DeviceId`, `DeviceName`, `DevciceGroupId`, `CompanyId`) VALUES ('{uuid}','{device_id}','{device_name}','{device_group_id}','{company_id}')"
                cursor.execute(create_cmd)
                connect.commit()   
                return jsonify([{'Result' : "創建成功!"}])
            else:
                return jsonify([{'Result' : "設備已存在!"}])

#刪除設備
@app.route('/api/DeleteDevice' , methods=['DELETE'])
@jwt_required()
def delete_device():
    connect = PYM.connect(**db_settings)
    uuid = request.json.get("Uuid",None)
    
    with connect.cursor() as cursor:
        find_cmd = f"SELECT * FROM `device` WHERE `Uuid` = '{uuid}'"
        cursor.execute(find_cmd)
        result = cursor.fetchall()
        if (any(result) == True):
            delete_cmd = f"DELETE FROM `device` WHERE `Uuid` = '{uuid}'"
            cursor.execute(delete_cmd)
            connect.commit()
            return jsonify([{'Result' : "刪除成功!"}])
        else:
            return jsonify([{'Result' : "設備不存在!"}])

#得取全部設備
@app.route('/api/GetAllDevice' , methods=['GET'])
def get_all_device():
        connect = PYM.connect(**db_settings)

        with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `device`"
            cursor.execute(find_cmd)
            result = cursor.fetchall()
            if (any(result) == True):
                data = []
                for row in result:
                    data.append({
                                 "Uuid" : row[0],
                                 "DeviceId" : row[1],
                                 "DeviceName" : row[2],
                                 "DevciceGroupId" : row[3],
                                 "CompanyId" : row[4],
                                })
                return jsonify(data)
            else:
                return jsonify([{'Result' : "查無設備!"}])

#Token驗證
@app.route('/api/Protected', methods=['GET', 'POST'])
@jwt_required()
def protected(): 
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

#註冊使用者
@app.route('/api/Register',methods = ['POST'])
def register():
    try:
        username = request.json.get("Username",None)
        password = request.json.get("Password",None)
        email = request.json.get("Email",None)
        uuid = str(Uuid.uuid4())
        date = str(dt.now())
        print(date)
        token = create_access_token(identity=uuid)  

        if (len(username) == 0 or len(password) == 0 or len(email) == 0 ):
            msg = [{'Result' : "缺少參數，請檢查!"}]
            return msg

        connect = PYM.connect(**db_settings)

        with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `{user_table}` WHERE `Username` = '{username}' or `Email` = '{email}'"
            cursor.execute(find_cmd)
            result = cursor.fetchall()

            if (any(result)):
                msg = [{'Result' : "此帳號或Email已被使用過!"}]
                return jsonify(msg)

            reg_cmd = f"INSERT INTO `{user_table}`(`Uuid`, `Username`, `Password`, `Email`, `Permission`, `Createtime`, `Token`) VALUES ('{uuid}','{username}','{password}','{email}','0','{date}','{token}')"
            cursor.execute(reg_cmd)
            connect.commit()
            connect.close()
            
            return jsonify([{'Result' : "註冊成功!"}])
            
    except Exception as ex:
        print(ex)
        return "Error"

#使用者登入
@app.route('/api/Login' , methods = ['POST'])
def login():
    username = request.json.get('Username',None)
    password = request.json.get('Password',None)
    uuid = str(Uuid.uuid4())

    connect = PYM.connect(**db_settings)

    with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `{user_table}` WHERE `Username` = '{username}' AND `Password` = '{password}'"
            cursor.execute(find_cmd)
            result = cursor.fetchall()

            #mysqlcommand("SELECT * FROM xxx WHERE username=%name", "")

            if (any(result) == False):
                msg = [{'Result' : "帳號密碼輸入錯誤!"}]
                return jsonify(msg)
            else:
                try:
                    msg = [ 
                            {'Result' : "登入成功!",
                            'Uuid' : result[0][0],
                            'Name' : result[0][1],
                            'Token' : result[0][6]
                            } 
                          ]
                    
                    Decoded = JWT.decode(result[0][6],secret, algorithms=["HS256"])
                    
                    exp_time = Decoded['exp']
                    now_time = dt.now().timestamp()
                    diff = now_time - exp_time 
                    
                    if (diff >= 0):
                        token = create_access_token(identity=uuid)
                        msg = [ {'Result' : "登入成功，Token已過期，Token已經自動更新!",
                                'Uuid' : result[0][0],
                                'Name' : result[0][1],
                                'Token' : token} 
                              ]
                        update_cmd = f"UPDATE `{user_table}` SET `Token`='{token}' WHERE `Uuid` = '{result[0][0]}'"
                        cursor.execute(update_cmd)
                        connect.commit()
                        return jsonify(msg)

                    return jsonify(msg)
                        
                except JWT.InvalidSignatureError:
                    msg = {'Result' : '簽證驗證失敗，你是不是想壞壞?'}
                    return jsonify(msg)

#得取當前Token使用者資訊
@app.route('/api/GetProfile', methods=['POST'])
@jwt_required()
def getporfile():
    connect = PYM.connect(**db_settings)
    uuid = get_jwt_identity()
    with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `{user_table}` WHERE `Uuid` = '{uuid}'"
            cursor.execute(find_cmd)
            result = cursor.fetchall()
            
            if (any(result) == False):
                return jsonify([{"Result" : "查無使用者!"}])
            msg = {"Uuid" : result[0][0],
                    "Username" : result[0][1],
                    "Email" : result[0][3],
                    "Permission" : result[0][4],
                    "Token" : result[0][6]
                }
    return jsonify(msg)

#刪除使用者
@app.route('/api/DeleteProfile', methods=['Delete'])
@jwt_required()
def deleteprofile():
    connect = PYM.connect(**db_settings)
    user = get_jwt_identity()
    uuid = request.json.get('Uuid',None)
    print(uuid)
    with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `{user_table}` WHERE `Uuid` = '{user}'"
            cursor.execute(find_cmd)
            result = cursor.fetchall()
            permissions = result[0][4]
            if (permissions == 1):
                delete_cmd = f"Delete FROM `{user_table}` WHERE `Uuid` = '{uuid}'"
                cursor.execute(delete_cmd)
                connect.commit()
                return jsonify({"Result" : "刪除成功!"})
            else:
                return jsonify({"Result" : "無權限!"})

#得取全部人資訊
@app.route('/api/GetAllProfile', methods=['GET' , 'POST'])
@jwt_required()
def getallporfile():
    connect = PYM.connect(**db_settings)
    uuid = get_jwt_identity()
    with connect.cursor() as cursor:
            find_cmd = f"SELECT * FROM `{user_table}` WHERE `Uuid` = '{uuid}'"
            cursor.execute(find_cmd)
            result = cursor.fetchall()
            permissions = result[0][4]
            if (permissions == 1):
                find_user_cmd = f"SELECT * FROM `{user_table}`"
                cursor.execute(find_user_cmd)
                result = cursor.fetchall()
                msg = []
                for row in result:
                    
                    msg.append({"Uuid" : row[0],
                            "Username" : row[1],
                            "Password" : row[2],
                            "Email" : row[3],
                            "Permission" : row[4],
                            "Token" : row[6],
                            "Createtime" : row[5]
                            })
                    
                return jsonify(msg)
            else:
                return jsonify({"Result" : "無權限!"})




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)