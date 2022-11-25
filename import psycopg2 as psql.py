import psycopg2 as psql

pdb = psql.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = '010203'
)
#### mijozlar buyurtmasi chastotasini hisoblovchi funksiya
cursor = pdb.cursor()
def buyurtma_chastota_soni():
    cursor.execute("SELECT COUNT(customernumber),customernumber FROM orders GROUP BY customernumber")
    print(cursor.fetchall())

#### bitta istemolchidan aylanmani hisoblash
def aylanmani_hisoblash():
    cursor.execute("SELECT SUM(amount),customernumber FROM payments GROUP BY customernumber")
    print(cursor.fetchall())

#### to'lov turi buyicha aylanma . MEN CHECKNUMBER NI TURLI XIL TULOV TURLARI BUYICHA QABUL QILDIM 
def tulov_turi_buyicha_aylanma():
    cursor.execute("SELECT SUM(amount),checknumber FROM payments GROUP BY checknumber")
    print(cursor.fetchall())


#buyurtma_chastota_soni()
#aylanmani_hisoblash()
tulov_turi_buyicha_aylanma()