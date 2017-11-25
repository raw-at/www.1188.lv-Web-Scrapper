# www.1188.lv-Web-Scrapper

## Description:
Web scraping is data scraping used for extracting data from websites. Here we are extracting complete website data and create a new database
for some other website.First we take down all the categorial links and then scrap data from each page and finally store it in mysql
database.

## Technologies Used
* Python 3.5
* BeautifulSoup
* request
* json
* mysql-database 
* mysql-workbench

## Scraped data Example (JSON format):

{
  "Registration number": "40003820858",
  "Url_no": 0,
  "Phone Type": [
    "Мобильный телефон"
  ],
  "Company Name": "Akvai Rores Ciet Tehniskais kanalizācijas dienests\" SIA, avārijas dienests",
  "Legal address": "Rīga, Ezera iela 11 - 29, LV-1034",
  "email": "akvairoresciet@inbox.lv",
  "Phone Number": [
    "29364656"
  ],
  "Category_Count": 0,
  "Product": "Аварийная служба, авария канализации, круглосуточная аварийная служба, ликвидация аварии, ликвидация засора, чистка канализации, очистка (ремонт) стояков, сантехник, санитарно – технические работы, сантехнические работы, ассенизация, чистка канализационных колодцев, очистка канализационных отстойников, чистка септиков, очистка биологических туалетов, очистка тары для жира, очистка разделителей, вывоз канализации и ассенизации, вывоз канализации, вывоз ассенизации, канализационная аварийная служба, полоскание высоким давлением, полоскание внутренних и наружных сетей, промывка канализационных труб, промывка канализационных колодцев, промывка дренажа, полоскание поля инфильтрации, техническая очистка канализационных трубопроводов, очистка сточных труб, ТВ инспекция, CCTV видео инспекция, обследование канализационной системы, диагностика, диагностика внутренней части канализационного трубопровода, выяснение дефектов, поиск с помощью зонда поврежденного места в трубопроводе канализационной трассы, бестраншейный ремонт, устранение повреждений после демонтажа и откапывания, обслуживание, хозяйствование, выезды по всем Латвийским городам, Ak vai rores ir ciet, Akvairoresirciet.",
  "website": "www.akvairoresciet.lv",
  "Company Address": " Rīga, LV-1000 "
}

## Website Screenshot:
