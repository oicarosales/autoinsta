#!/usr/bin/env python3

import random
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import mysql.connector
import numpy as np

# DADOS LOGIN DATABASE
mydb = mysql.connector.connect(
    host='',
    user='',
    passwd='',
    database=''
)
# FIM DADOS LOGIN DATABASE

# POPULA TBL_LOGIN_LOG
mycursor = mydb.cursor()
sql = 'INSERT INTO tbl_login_log (user, data_login) VALUES (CURRENT_USER(), now())'
mycursor.execute(sql)
mydb.commit()
# FIM POPULA TBL_LOGIN_LOG

# ABRE INSTAGRAM.COM
driver = webdriver.Firefox()
print('Abrindo instagram.com.')
# driver.set_window_size(800, 800)
# driver.set_window_position(600, 0)
driver.get('https://www.instagram.com/')

time.sleep(8)

# AUTENTICAÇÃO
print('Inserindo login e senha.')
login = driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
user = ''  # Ponha seu login aqui
login.send_keys(user)

time.sleep(1)

# LÊ ARQUIVO DE SENHA
f = open('passwd.key', 'r')
lines = f.readlines()
password = lines[0]
pass_box = driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
pass_box.send_keys(password)
f.close()

time.sleep(1)
# BOTÃO DE LOGIN
button_element = driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
button_element.click()

time.sleep(15)
# BOTÃO NOT NOW
button_element = driver.find_element_by_xpath(
    '/html/body/div[4]/div/div/div[3]/button[2]')
button_element.click()

time.sleep(1)

# HASHTAGS QUE SERÃO BUSCADAS - MODIFIQUE OU ADICIONE LIVREMENTE
print('Buscando hashtags para dar like.')
hashtags = ['minimalsetups', 'designyourworkspace',
            'officeinspiration', 'designoffice', 'productivespaces']


tempo = [8, 9, 10, 11, 12, 13, 15, 16, 18, 20, 30, 60, 120]

# LÊ ARQUIVO DE COMENTÁRIOS - MODIFIQUE INSERINDO UM COMENTÁRIO POR LINHA
f = open('comments.txt', 'r')
lines = f.readlines()
comments = lines

# CATEGORIZA OS POSTS EM POPULARES OU RECENTES
pop_or_recent = ['/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div',
                 '/html/body/div[1]/section/main/article/div[1]/div/div/div[2]/div[1]/a/div']

# LOOP INFINITO
while 0 < 1:
    # ESCOLHA RANDOMICA DA HASHTAG
    hashtag = random.choice(hashtags)
    driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
    print(str(hashtag))

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(random.choice(tempo))

    # ESCOLHA RANDOMICA DO COMENTÁRIO
    text = random.choice(comments)

    # ESCOLHA RANDOMICA DA CATEGORIA
    button_element = driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[1]/div/div/div[2]/div[1]/a/div')
    button_element.click()

    time.sleep(random.choice(tempo))

    # CHECA NO BANCO DE DADOS SE A PUBLICAÇÃO ATUAL JÁ FOI CURTIDA
    url = driver.current_url
    sql = "SELECT url FROM tbl_like_log where url =" + "'" + \
        str(url)+"'" + " and user_login = " + "'"+str(user)+"'" + ""
    mycursor.execute(sql)
    likes = mycursor.fetchall()

    # IF - SE A PUBLICAÇÃO JÁ FOI CURTIDA, AVANÇA PARA PRÓXIMA. SE NÃO DÁ LIKE
    if str(url) in str(likes):
        print(str(url)+' Já curtimos esta publicação!')
        button_element = driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/div/div/a')
        button_element.click()
    else:
        button_element = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
    button_element.click()
    print('Like!')

    time.sleep(random.choice(tempo))

    # SELECIONA CAMPO DE COMENTÁRIO
    button_element = driver.find_element_by_css_selector(
        '.Ypffh')
    button_element.click()
    time.sleep(2)
    button_element = driver.find_element_by_css_selector(
        '.Ypffh')
    time.sleep(2)
    # FAZ COMENTARIO ESCOLIDO RANDOMICAMENTE NA LINHA 92
    button_element.send_keys(text)

    time.sleep(2)

    # CLICA BOTÃO PUBLISH
    button_element = driver.find_element_by_xpath(
        '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button')
    button_element.click()

    time.sleep(random.choice(tempo))

    # POPULA TBL_LIKE_LOG NO BANCO DE DADOS
    sql = 'INSERT INTO tbl_like_log (url, data_like, comment, hashtag, user_login) VALUES (%s, now(), %s, %s,%s)'
    val = (str(url), str(text), str(hashtag), str(user))
    mycursor.execute(sql, val)
    mydb.commit()

    # AVANÇA PARA PROXIMA PUBLICAÇÃO
    button_element = driver.find_element_by_xpath(
        '/html/body/div[4]/div[1]/div/div/a')
    button_element.click()
