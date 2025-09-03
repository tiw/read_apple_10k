import sqlite3

# 连接到数据库
conn = sqlite3.connect('xbrl.db')
c = conn.cursor()

# 查看financial_facts表结构
c.execute('PRAGMA table_info(financial_facts)')
print('financial_facts表结构:')
for row in c.fetchall():
    print(row)

# 查看xbrl_files表结构
c.execute('PRAGMA table_info(xbrl_files)')
print('\nxbrl_files表结构:')
for row in c.fetchall():
    print(row)

conn.close()
