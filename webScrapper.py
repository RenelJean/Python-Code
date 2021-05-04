import requests 
from bs4 import BeautifulSoup

URL = ‘https://www.amazon.in/Veirdo-Mens-Cotton-T-shirt-G4_BSR_BLACK_L_Black_Large/dp/B01MSTXWBS/ref=bbp_bb_d33a38_st_pbyk_w_0?psc=1&smid=APT08BGG6TKYO’

headers={“User-Agent”:’Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36′}
page = requests.get(URL,headers=headers)
soup=BeautifulSoup(page.content,’html.parser’)
title = soup.find(id=”productTitle”).get_text()
price=soup.find(id=”priceblock_saleprice”).get_text()
print(title.strip())

print(price.strip())

