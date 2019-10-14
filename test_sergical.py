import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('test_sergical.xlsx')

list1=['service category', 'categoryid', 'catid', 'subcatid', 'svcgroupid',
       'codeid', 'description', 'category']
print("Column headings:")
print(df.columns)
for i in df.index:
    cpt_code=df[list1[5]][i]
    category_id=df[list1[1]][i]
    sub_category_id=df[list1[3]][i]
    group_id=df[list1[3]][i]
    group_desc=df[list1[4]][i]
    service_category=df[list1[0]][i]
    string_format = f'"{cpt_code}":[{{"svcCategoryId":"{category_id}", "svcSubcategoryId":"{sub_category_id}", "svcGroupId": "{group_id}","svcgroup":"{service_category}"}}]'
    print(string_format)
    f = open("data1.txt", "a")
    f.write("{}\n".format(string_format))
f.close()



