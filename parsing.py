import pandas as pd
from Parsing_yvkurse import Parsing

parsing=Parsing('https://vk.com/@yvkurse')

title=parsing.parse_title()
text=parsing.parse_text()
images_url=parsing.parse_images()

table=pd.DataFrame({ 'Заголовок' :title ,'Текст статьи' : text,'ImageURL':images_url},)
table.to_csv('data_yvkurse.csv')
