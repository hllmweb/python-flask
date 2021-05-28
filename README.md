#https://www.youtube.com/watch?v=xIgPMguqyws
#https://www.youtube.com/watch?v=wD_Qu6qtx1g
#https://www.youtube.com/watch?v=GMppyAPbLYk

#https://stackoverflow.com/questions/22259847/application-not-picking-up-css-file-flask-python
#https://pythonhow.com/add-css-to-flask-website/



https://www.youtube.com/watch?v=LSnAs2WbLiA




pip install cx_Oracle

import cx_Oracle

connection = cx_Oracle.connect("hr/hr@localhost:1521/orc1")
dsn = cx_Oracle.makedsn(
    'localhost',
    '1521',
    service_name='orc1'
)

conn = cx_Oracle.connect(
    user='hr',
    password='hr',
    dsn=dsn
)


c = conn.cursor()
c.execuite('SELECT * FROM table where ROWNUM <= 10')
for row in c: print(row)