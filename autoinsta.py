#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import mysql.connector
import getpass

# put here you database login info
MYDB = mysql.connector.connect(
    host='',
    user='',
    passwd=getpass.getpass('Db Password: '),
    database=''
)

MYCURSOR = MYDB.cursor()
SQL = 'INSERT INTO tbl_login_log (user, data_login) VALUES (CURRENT_USER(), now())'
MYCURSOR.execute(SQL)
MYDB.commit()

DRIVER = webdriver.Firefox()
print('Abrindo instagram.com.')
DRIVER.get('https://www.instagram.com/')
try:
    element = WebDriverWait(DRIVER, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input'))
    )
finally:
    DRIVER.quit

print('Inserindo login e senha.')
LOGIN = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
USER = input('Login: ') 
LOGIN.send_keys(USER)

PASSWORD = getpass.getpass('Password: ')
PASS_BOX = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
PASS_BOX.send_keys(PASSWORD)

# logon button
BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()

time.sleep(4)

# tags file path - change to your
HASHTAGS = open('/home/icaro/MEGA/projetos/autoinsta/hashtags.txt', 'r').readlines()

TIME = [5,6,7]

# comments file path - change to your
COMMENTS = open('/home/icaro/MEGA/projetos/autoinsta/comments.txt', 'r').readlines()

# while to chose picture
while 0 < 1:
    # chose tag
    HASHTAG = random.choice(HASHTAGS)
    DRIVER.get('https://www.instagram.com/explore/tags/' + HASHTAG + '/')
    print(str(HASHTAG))

    DRIVER.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    DRIVER.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(random.choice(TIME))

    # chose comment
    TEXT = random.choice(COMMENTS)

    BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[1]/div/div/div[2]/div[1]/a/div').click()

    time.sleep(random.choice(TIME))

    # checks if the publication has already been liked
    URL = DRIVER.current_url
    SQL = "SELECT url FROM tbl_like_log where url =" + "'" + \
        str(URL)+"'" + " and user_login = " + "'"+str(USER)+"'" + ""
    MYCURSOR.execute(SQL)
    LIKES = MYCURSOR.fetchall()
    print(str(LIKES))

    if str(URL) in str(LIKES):
        print(str(URL)+' Já curtimos esta publicação!')
        BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
            '/html/body/div[5]/div[1]/div/div/a').click()
    else:
        BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
        print('Liked!')

    time.sleep(random.choice(TIME))

    try:
        BUTTON_ELEMENT = DRIVER.find_element_by_css_selector(
            '.Ypffh').click()
    except Exception:
        pass

    time.sleep(2)
    try:
        BUTTON_ELEMENT = DRIVER.find_element_by_css_selector(
            '.Ypffh')
    except Exception:
        pass
    time.sleep(2)

    try:
        BUTTON_ELEMENT.send_keys(TEXT)
    except Exception:
        pass

    time.sleep(2)

    try:
        BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]').click()
    except Exception:
        pass

    time.sleep(random.choice(TIME))

    # insert interation data on database
    SQL = 'INSERT INTO tbl_like_log (URL, data_like, comment, hashtag, user_login) VALUES (%s, now(), %s, %s,%s)'
    VAL = (str(URL), str(TEXT), str(HASHTAG), str(USER))
    MYCURSOR.execute(SQL, VAL)
    MYDB.commit()

    # go to next
    BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
        '/html/body/div[5]/div[1]/div/div/a[2]').click()
