import pymysql
import json
import io
import requests
import json
import re
from bs4 import BeautifulSoup
request = requests.get('http://www.1188.lv/каталог')
soup = BeautifulSoup(request.content,"html.parser")

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='test', charset='utf8')
json_data=io.open('data.json', encoding='utf-8').read()
data_dict = json.loads(json_data)
cur = conn.cursor()
i = 0

def text_formatter(text):
    final_text = []
    for i in text:
        if(i=='\t' or i == '\n' or i == '?' or i=='-' or i=="\\" or i=="\n"):
            pass
        else: 
            final_text.append(i)
    final_text.pop(0)    
    return ''.join(final_text)

category_list = []
for i in soup.find('div',{'class':'letter-content'}).findAll('li'):
    category_list.append(text_formatter(i.text))


for j in range(len(category_list)):
        for item in data_dict:
                i=+1
                category_id = i
                name=item["Company Name"]
                address=item["Company Address"]
                email=item["email"]
                reg_number = item["Registration number"]
                legal_address=item["Legal address"]

                if item["Category_Count"] == j:
                        categories = category_list[j]

                cur.execute("insert into company(category_id,email,registration_no,company_address,company_name,legal_address) values(%s,%s,%s,%s,%s,%s)",(category_id,email,reg_number,address,name,legal_address))
                c_id = conn.insert_id()
                print(c_id)
                cur.execute("insert into categories(category_id,category_name) values (%s,%s)",(category_id,categories))
                phone_type=item["Phone Type"]
                phone_no=item["Phone Number"]
                
                products=item["Product"]
                product_list = products.split(", ")
                for product in product_list:
                        cur.execute("insert into products(product_name) values (%s)",(product))
                        product_id = conn.insert_id()
                        cur.execute("insert into products_companies(company_id,product_id) values (%s,%s)",(c_id,product_id))
                j=0
                for ph_no in phone_no:
                        j=+1
                        ph_type = ""
                        if phone_type[j]:
                                ph_type = phone_type[j]
                        else:
                                ph_type = ""
                        cur.execute("insert into phones(company_id,number,phonetype) values (%s,%s,%s)",(c_id,ph_no, ph_type))
                print(reg_number)
        conn.commit()
cur.close()
conn.close()
                                
                                
