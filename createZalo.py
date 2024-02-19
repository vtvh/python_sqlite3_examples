import uuid
import sqlite3
con = sqlite3.connect("db/zalo.db")
cur = con.cursor()

# Create tables
def createTable():
    cur.execute("CREATE TABLE clientAccount (uuid,displayName,phone,purpose)")
    cur.execute("CREATE TABLE guiKetBan(uuid,timeStamp,clientAccount,zaloAccount,status)")
    cur.execute("CREATE TABLE zaloAccount(uuid,name,phone,bio,dob,sex,avatar,cover,tag,status,lastUpdate)")
    cur.execute("CREATE TABLE tag(uuid,name,description)")

# Create tags
def createTags():
    data = [
        (str(uuid.uuid4()), 'myContacts', 'My contacts from Google Contacts'),
        (str(uuid.uuid4()), 'muaNgoai', 'Mua từ trên FB'),
        (str(uuid.uuid4()), 'taiXe', 'Tài xế nội bộ GLS'),
    ]
    cur.executemany("INSERT INTO tag VALUES(?, ?, ?)", data)


# Read 'mysdt' line by line and insert into table zaloAccount column 'phone' and tag: 'myContacts'
def insertZaloAccount():
    with open('mysdt') as f:
        for line in f:
            data = [(str(uuid.uuid4()), line.strip(), '20b7462a-bdab-43ae-a380-64b6ee73f239')]
            cur.executemany("INSERT INTO zaloAccount (uuid,phone,tag) VALUES(?, ?, ?)", data)

# Read 'taixe.psv' line by line and insert into table zaloAccount column 'phone' and tag: 'taiXe'
def insertZaloAccount1():
    with open('taiXe.psv') as f:
        # skip the first line
        next(f)
        for line in f:
            sdt = line.split('|')[1]
            sdt = '84'+sdt
            name= line.split('|')[0]
            data = [(str(uuid.uuid4()), sdt.strip(), '308601d8-74b3-4a47-bcd4-3a45899846c8',name.strip())]
            print(data)
            cur.executemany("INSERT INTO zaloAccount (uuid,phone,tag,realName) VALUES(?, ?, ?, ?)", data)



if __name__ == '__main__':
    insertZaloAccount1()
    print('Done')


# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

