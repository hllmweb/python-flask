import cx_Oracle


dsn_tns = cx_Oracle.makedsn('10.228.20.18', '1521', service_name='bdiseculo.seculomanaus.com.br') 
conn = cx_Oracle.connect('rm', 'rm', dsn_tns,'UTF-8')
print(conn.version)
conn.close()



# conn = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)

#print(os.environ['path'])
#con = cx_Oracle.connect('rm/rm@10.228.20.18:1521/orc1')
#print(con.version)
#con.close()

# conn = cx_Oracle.connect("rm/rm@bdiseculo.seculomanaus.com.br:1521/orc1")
# conn = cx_Oracle.connect("USER/pass@server/SERVICE")
# conn = cx_Oracle.connect("rm/rm@10.228.20.18:1521/bdiseculo.seculomanaus.com.br")
# cur = conn.cursor()
# cur.execute('SELECT * FROM BD_PDV.CATEGORIAS')
# for line in cur:
#     print(line)
# cur.close()
# conn.close()

# connection = cx_Oracle.connect("rm", "rm", "10.228.20.18/bdiseculo.seculomanaus.com.br/orclpdb1")
# cursor = connection.cursor()
# cursor.execute("SELECT 'TESTE' AS MENSAGEM FROM DUAL")

# for fname, lname in cursor:
#     print("Values:", fname, lname)

# 
# dsn = cx_Oracle.makedsn(
#     '10.228.20.18/bdiseculo.seculomanaus.com.br',
#     '1521',
#     service_name='orc1'
# )

# conn = cx_Oracle.connect(
#     user='rm',
#     password='rm',
#     dsn=dsn
# )

# c = conn.cursor()
# c.execuite("SELECT 'TESTE' AS MENSAGEM FROM DUAL")
# for row in c: print(row)