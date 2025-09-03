import sqlite3

# 连接到数据库
conn = sqlite3.connect('xbrl.db')
c = conn.cursor()

# 查看微软公司文件
c.execute("SELECT * FROM xbrl_files WHERE company_name LIKE '%MICROSOFT%'")
results = c.fetchall()
print('微软公司文件:')
for row in results:
    print(row)

conn.close()
