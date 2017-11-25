import requests
import json
import re
from bs4 import BeautifulSoup
request = requests.get('http://www.1188.lv/каталог')
soup = BeautifulSoup(request.content)



#text formatter
def text_formatter(text):
    final_text = []
    for i in text:
        if(i=='\t' or i == '\n' or i == '?' or i=='-' or i=="\\" or i=="\n"):
            pass
        else: 
            final_text.append(i)
    final_text.pop(0)    
    return ''.join(final_text)




scrapped_data = list()



count = 0
url_list = []
category_list = []
for i in soup.find('div',{'class':'letter-content'}).findAll('a'):
    url_list.append(i['href'])
    count+=1
#print(count)
#print(len(url_list))

for i in soup.find('div',{'class':'letter-content'}).findAll('li'):
    category_list.append(text_formatter(i.text))

print("length:",len(category_list))

with open('category.json', 'a') as fp:
            json.dump(category_list, fp, ensure_ascii=False)


initial_url = url_list
len_count = 0

catogery_count  = 0
for i in initial_url[catogery_count:]:
    print('*'*100)
    
    page_data = requests.get('http://www.1188.lv'+i)
    page_data_soup = BeautifulSoup(page_data.content)
    
    final_page_url_list = []
    
    for i in page_data_soup.find('div',{'class':'items'}).findAll('a',{'class':'title'}):
        final_page_url_list.append(i['href'])
    
    if page_data_soup.find('a',{'class':'btn big'}):

        new_url = page_data_soup.find('a',{'class':'btn big'})['href']
        #print(new_url)
        temp_list = []
        list_data = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'
        '21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40'
        '41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62']
        
        url_list = []
        total_url_list = [] 
        
        for i,j in enumerate(new_url):
            if j=='2':
                pos = i
            temp_list.append(j)
        for i in list_data:
            temp_list[pos] = i
            url_list.append(''.join(temp_list))
        #print(url_list)

        for i in url_list:
            new_page = requests.get('http://www.1188.lv'+i)
            new_page_soup = BeautifulSoup(new_page.content)
        #print(new_page_soup.prettify())        
            if new_page_soup.find('div',{'class':'items'})!=None:
                for i in new_page_soup.find('div',{'class':'items'}).findAll('a',{'class':'title'}):
    #.findAll('a',{'class':'title'}):
                    final_page_url_list.append(i['href'])
        
        # final_page_url_list.append(i['href'])
        print(len(final_page_url_list))
    
    #else:
    #    for i in page_data_soup.find('div',{'class':'items'}).findAll('a',{'class':'title'}):
    #        final_page_url_list.append(i['href'])

    

    if catogery_count>0: 
        url_count = 0
    else:
        url_count = 0

    for i in final_page_url_list[url_count:]:
        final_detail = dict()
        final_page = requests.get('http://www.1188.lv'+i)
        final_page_data = BeautifulSoup(final_page.content)
        if final_page_data.find('h1',{'class':'title'})!=None:
        
            for i in final_page_data.find('h1',{'class':'title'}).findAll('span'):
                final_detail['Company Name'] = text_formatter(i.text)
        
        if final_page_data.find('div',{'class':'address'})!=None:
            first_address = re.sub('\s+',' ',final_page_data.find('div',{'class':'address'}).text)
            #print('first address',first_address)
            
            
            company_address = first_address[:len(first_address)-len("Как туда попасть?")-1] 
            #print('Company Addrerss',company_address)
            
            final_detail['Company Address'] = company_address
        else:
            final_detail['Company Address'] = first_address
        data_list = []
        
        if final_page_data.find('ul',{'class':'items left'}) !=None:    
            for i in final_page_data.find('ul',{'class':'items left'}).find_all('li'):  
                data_list.append(str(i))

        
        number_list = []
        number_title_list=[]

        final_detail['Phone Number'] = list()
        final_detail['Phone Type'] = list()
        final_detail['email'] =" "
        final_detail['website'] = " "
        final_detail['Product'] = " "
        final_detail['Registration number'] = " "
        final_detail['Legal address'] = " "
        
        
        for i in data_list:
            data_list_soup = BeautifulSoup(i)
            
            if data_list_soup.find('span',{'class':'label'})!=None:
                
                if data_list_soup.find('span',{'class':'label'}).text == "Телефон:":
                
                    for i in data_list_soup.findAll('a',{'class':'number'}):
                        number_list.append(i.text)
                    for i in data_list_soup.findAll('span',{'class':'number-title'}):
                        number_title_list.append(i.text)
                
            if data_list_soup.find('span',{'class':'label'})!=None:

                if data_list_soup.find('span',{'class':'label'}).text == "Е-почта:":
                    email = data_list_soup.find('a').text
                    final_detail['email'] = email
            
            if data_list_soup.find('span',{'class':'label'})!=None:

                if data_list_soup.find('span',{'class':'label'}).text == "Веб-страница:":
                    website = data_list_soup.find('a').text
                    final_detail['website'] = website    
            


        for i in number_list:
            final_detail['Phone Number'].append(i) 
            
        for i in number_title_list:
            final_detail['Phone Type'].append(text_formatter(i))

        
        '''
        if(len(data_list)==6):
            data_list.pop()
            final_data_list = data_list[1:]
            final_data_str = ''.join(final_data_list)

        elif(len(data_list)==5):
            data_list.pop()
            final_data_list = data_list[1:]
            final_data_str = ''.join(final_data_list)
        
        elif(len(data_list)==2):
            data_list.pop(0)
            final_data_list = data_list
            final_data_str = ''.join(final_data_list)

        final_soup = BeautifulSoup(final_data_str,'html.parser')
        
        final_detail['Phone Number'] = list()
        final_detail['Phone Type'] = list()
        
        #print(data_list)
        #print(len(data_list))

        if(len(data_list)==1):
            final_detail['Phone Number'].append(final_soup.find('a',{'class':'number'}).text)
                
        elif(len(data_list)==4):
            final_detail['Phone Number'].append(final_soup.find('a',{'class':'number'}).text)
            if final_soup.find('span',{'class':'number-title'}) != None:

                final_detail['Phone Type'].append(text_formatter(final_soup.find('span',{'class':'number-title'}).text))
            else:
                final_detail['Phone Type'] = ''
            web_email_list = []

            temp_soup = BeautifulSoup(''.join(data_list[2:]),'html.parser')

            for i in temp_soup.findAll('a'):
                web_email_list.append(i.text)
                            
            if(len(web_email_list)==2):   
                final_detail['email'] = web_email_list[0]
                final_detail['website'] = web_email_list[1]
            else:
                final_detail['email'] = web_email_list[0]
                

        elif(len(data_list)==5):
            number_list = []
            type_list = []
            for i in  final_soup.findAll('a',{'class':'number'}):
                number_list.append(i.text)
            print(number_list)
            for i in number_list:
                final_detail['Phone Number'].append(i)
            
            
            
            for i in  final_soup.findAll('span',{'class':'number-title'}):
                if(i.text == None):
                    pass
                else:
                    type_list.append(i.text)
            for i in type_list:
                final_detail['Phone Type'].append(text_formatter(i))

            web_email_list = []

            temp_soup = BeautifulSoup(''.join(data_list[3:]),'html.parser')

            for i in temp_soup.findAll('a'):
                web_email_list.append(i.text)
                            

            final_detail['email'] = web_email_list[0]
            final_detail['website'] = web_email_list[1]
        
        #final_detail['Phone Number'] = list()
        #for i in final_page_data.findAll('a',{'class':'number'}):
            #final_detail['Phone Number'].append(i.text) 
        
        #final_detail['Phone Type'] = list()

        #if final_page_data.find('span',{'class':'number-title'}) != None :
            #final_detail['Phone Type'] = text_formatter(final_page_data.find('span',{'class':'number-title'}).text)
        #else:
            #final_detail['Phone Type'] = ''
        #temp_details = final_page_data.find('ul',{'class':'items left'}).find_all('a')
        #if(len(final_detail['Phone Number'])==1):

            #final_detail['Email'] = temp_details[1].text 
            #final_detail['Website'] = temp_details[2].text
        #elif(len(final_detail['Phone Number'])==2):
            #final_detail['Email'] = temp_details[2].text 
            #final_detail['Website'] = temp_details[3].text
        '''

        if final_page_data.find('p',{'class':'short'})!=None:

            product = final_page_data.find('p',{'class':'short'}).text
            final_detail['Product'] = product    
        else:
            final_detail['Product'] = ""

        if final_page_data.find('a',{'id':'Lursoft-Tab'}) != None:

            product_page_url = final_page_data.find('a',{'id':'Lursoft-Tab'})['href']
            product_page_request = requests.get('http://www.1188.lv'+product_page_url)

            final_product_soup = BeautifulSoup(product_page_request.content)
        
            bottom_details = []

            if final_product_soup.find('div',{'class':'items left'})!=None:

                for i in final_product_soup.find('div',{'class':'items left'}).findAll('li'):
                    bottom_details.append(str(i))

                for i in bottom_details:
                    data_list_soup = BeautifulSoup(i)
                        
                    if data_list_soup.find('span',{'class':'label'})!=None:

                        if data_list_soup.find('span',{'class':'label'}).text == "Регистрационный номер:":
                            reg = data_list_soup.find('div',{'class':'data'}).text
                            final_detail['Registration number'] = reg
                    
                    #if data_list_soup.find('span',{'class':'label'})!=None:

                        if data_list_soup.find('span',{'class':'label'}).text == "Юридический адрес:":
                            leg_add = data_list_soup.find('div',{'class':'data'}).text
                            final_detail['Legal address'] = leg_add        
                
                
                #if data_list_soup.find('span',{'class':'label'})!=None:
            
                
        final_detail['Url_no']=url_count
        final_detail['Category_Count'] = catogery_count
                

        
        '''    
        bottom_details_str = ''.join(bottom_details[3:])

        bottom_soup =  BeautifulSoup(bottom_details_str,'html.parser')

        final_bottom_data = []
        for i in bottom_soup.findAll('div',{'class':'data'}):
            final_bottom_data.append(i.text)
        
        
        
        
        final_detail['Products'] = final_bottom_data[0]
        final_detail['Registration number'] = final_bottom_data[1]
        final_detail['Legal address'] = final_bottom_data[2]
        '''
        #final_detail['Products'] = final_page_data.find('li',{"class":'keywords'}).find('p',{'class':'short'}).text

        #temp_x_details = final_page_data.find('div',{'class':'items left'}).findAll('div',{'class':'data'})
        #final_detail['Registration number'] = temp_x_details[3].text
        #final_detail['Legal address'] = temp_x_details[5].text
        with open('temp.json', 'a') as fp:
            json.dump(final_detail, fp, ensure_ascii=False, indent=2)


        #scrapped_data.append(final_detail)
        print('category_count',catogery_count)
        print('url_count',url_count)
        url_count+=1
        
    catogery_count+=1
#with open(scrapped.txt, 'wb') as f:
    #pickle.dump(my_list, f)
