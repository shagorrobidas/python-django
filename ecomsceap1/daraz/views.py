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
from .models import TestProduct


# Create your views here.
def show(request):
    # # return HttpResponse("Welcome TO daraz home page")
    # driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get("https://perfumancebd.com/product-category/perfume/calm-and-cool/")

    # total_product = (3*4)-1
    # product_list = []
    # product_price = []
    # image_src_list = []
    
    # for product in range(1, total_product+1):
    #     x_path = '//*[@id="rig-adpr"]/div['+str(product)+']/p[1]'
    #     product = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path)))
    #     product_list.append(product.text)

    # for product in range(1, total_product+1):
    #     price_xpath = '//*[@id="rig-adpr"]/div['+str(product)+']/p[2]'
    #     product_pric = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, price_xpath)))
    #     product_price.append(product_pric.text)



    # for product in range(1, total_product+1):
    
    #     img_xpath = '//*[@id="rig-adpr"]/div['+str(product)+']/a/img'

    #     product_img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, img_xpath)))
    #     image = product_img.get_attribute('src')
    #     image_src_list.append(image)
          
    # # product_img.screenshot('E:\pythone\Europian_it\10th_class'+ query +'('+str(product)+').png')

    # scrape = {"title":product_list,"price":product_price, "image":image_src_list}
    # return HttpResponse(scrape)
    
    
    return render(request, 'Daraz/from.html', )

