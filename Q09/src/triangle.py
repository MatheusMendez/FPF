from selenium import webdriver
from selenium.webdriver.common.by import By

def triangle(v1:int,v2:int,v3:int):

    driver = webdriver.Chrome()
    driver.get('http://www.vanilton.net/triangulo/.')

    input_1 = driver.find_element(By.NAME, 'V1')
    input_1.clear()
    input_1.send_keys(v1)

    input_v2 = driver.find_element(By.NAME, 'V2')
    input_v2.clear()
    input_v2.send_keys(v2)

    input_v3 = driver.find_element(By.NAME, 'V3')
    input_v3.clear()
    input_v3.send_keys(v3)
    
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()

    div = driver.find_elements(By.TAG_NAME, 'div')
    res = div[-1].text

    driver.quit()

    return(res)

if __name__ == '__main__':
    print(triangle(5,5,5))
