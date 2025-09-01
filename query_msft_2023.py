import sqlite3

# 连接到数据库
conn = sqlite3.connect('xbrl.db')
c = conn.cursor()

# 查询微软2025财年的财务数据（数据库中只有这一年的数据）
query = """
SELECT ft.tag_name, ff.value, c.context_id
FROM financial_facts ff 
JOIN financial_tags ft ON ff.tag_id = ft.id 
JOIN contexts c ON ff.context_id = c.id
JOIN xbrl_files xf ON ff.xbrl_file_id = xf.id 
WHERE xf.company_name = 'MICROSOFT CORPORATION' AND xf.fiscal_year = 2023
"""

c.execute(query)
results = c.fetchall()

print('微软2025财年财务数据:')
print('标签名称'.ljust(50) + '数值'.ljust(20) + '上下文ID')
print('-' * 100)
for row in results:
    print(row[0].ljust(50) + str(row[1]).ljust(20) + row[2])

conn.close()