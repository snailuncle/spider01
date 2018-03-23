# path="D:\mongodb\bin\mongo.exe"
# "D:\mongodb\bin\mongo.exe"
# D:\mongodb\data\db
#设置mongo存储数据的文件夹  
# D:\mongodb\bin
# $ mongod --dbpath D:\mongodb\data\db
#浏览器输入验证mongo能否使用
# localhost:27017
# cd到bin目录,输入mongo开始使用mongo
# 插入数据  db.test.insert({'a':'b'})
# 日志路径  D:\mongodb\data\logs\mongo.log
# D:\mongodb\bin
# $ mongod --bind_ip 0.0.0.0 --logpath D:\mongodb\data\logs\mongo.log --logappend --dbpath D:\mongodb\data\db --port 27017 --serviceName "MongoDB" --serviceDisplayName "MongoDB" --install
# 所有IP都能访问  日志路径    追加模式    数据库路径  端口    服务名称    显示名称


# 显示数据库 show dbs
# 指定使用数据库 use db_name
# 插入数据      db.table_name.insert({'key':'value'})


