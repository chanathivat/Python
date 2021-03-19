import sqlite3
import sqlite3
conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
c = conn.cursor()

c.execute('DROP TABLE marathon ')