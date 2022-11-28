from django.shortcuts import render

from django.shortcuts import HttpResponse


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .models import product_ebay
# Create your views here.
def show(request):
    
    

    # ditels ={"title":product_title, "Image":product_image,}
    # # return render(request, 'ebay/from.html', context= ditels)
    return render(request, 'ebay/from.html')
def add(request):
    if (request.method == "POST"):
        
        url = request.POST.get('w_url')
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        
        t_count = request.POST.get('t_count')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.ebay.com/sch/i.html?_fsrp=1&_sacat=177&_trkparms=pageci%3A6ffd6c04-5f43-11ed-a7ae-02622c48d4c0%7Cparentrq%3A5675df551840ab8e2cb17955fff59ee6%7Ciid%3A1&_dmd=2&_pgn=1')
        driver.get(url)
        
        product_titlelist = []

        for product in range(4, int(t_count)+1):
            loop_div = x1+"div["+str(product)+"]"+x2
            title_xpath = loop_div
            product_title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, title_xpath)))
            # product_titlelist.append(product_title)
            print(product_title)

        # print(product_titlelist)
        time.sleep(20)
        driver.quit()

        return HttpResponse(t_count)

    
        # return render(request, 'ebay/from.html')
    else:
        return HttpResponse("this is not a post method")
