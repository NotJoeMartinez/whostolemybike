import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

urls = [
    'https://www.depts.ttu.edu/ttpd/daily/2017/TTU_Main/index.php',
    'https://www.depts.ttu.edu/ttpd/daily/2018/TTU_Main/index.php',
    'https://www.depts.ttu.edu/ttpd/daily/2019/TTU_Main/index.php',
    'https://www.depts.ttu.edu/ttpd/daily/2020/TTU_Main/index.php',
    ]


for x in urls:
    url = x 

    #If there is no such folder, the script will create one automatically
    folder_location = r'pdfs'
    if not os.path.exists(folder_location):os.mkdir(folder_location)

    response = requests.get(url)
    soup= BeautifulSoup(response.text, "html.parser")     


    for link in soup.select("a[href$='.pdf']"):
        #Name the pdf files using the last portion of each link which are unique in this case
        filename = os.path.join(folder_location,link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,link['href'])).content)