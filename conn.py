import cx_Oracle
# host = '10.228.20.18'
# port = '1521'
# service_name = 'bdiseculo.seculomanaus.com.br'
# user = 'rm'
# pwd  = 'rm'


# dsn_tns = cx_Oracle.makedsn(host,port,service_name)
# connection = cx_Oracle.connect(user,pwd,dsn_tns)


con = cx_Oracle.connect("rm","rm","10.228.20.18:1521/bdiseculo.seculomanaus.com.br")  
print(con.version)