from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_myLogin():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://www.google.com")
    print("Page Title is "+driver.title)
    print("Page url is "+driver.current_url)
    assert driver.title == "Mukesh"
    driver.find_element(By.NAME,"q").send_keys("Mukesh Otwani")
    driver.quit()