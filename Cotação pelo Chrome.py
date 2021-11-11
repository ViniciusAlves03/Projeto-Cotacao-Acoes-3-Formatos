from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

acao = input('informe o simbolo da ação:')
browser = webdriver.Chrome()

browser.get('http://www.google.com')
assert 'Google' in browser.title

element = browser.find_element(By.NAME, 'q')  # Find the search box
element.send_keys(str(acao) + Keys.RETURN)