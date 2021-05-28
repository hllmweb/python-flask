import cx_Oracle

dsn_tns = cx_Oracle.makedsn('10.228.20.18', '1521', service_name='bdiseculo.seculomanaus.com.br') 
conn = cx_Oracle.connect(user=r'rm', password='rm', dsn=dsn_tns)
print(conn.version)


# c = conn.cursor()
# c.execute('select * from database.table') 
# for row in c:
    # print (row[0], '-', row[1]) 
#conn.close()