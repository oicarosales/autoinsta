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

# DADOS LOGIN DATABASE
MYDB = mysql.connector.connect(
    host='',
    user='',
    passwd='',
    database=''
)
# FIM DADOS LOGIN DATABASE

# POPULA TBL_LOGIN_LOG
MYCURSOR = MYDB.cursor()
SQL = 'INSERT INTO tbl_login_log (user, data_login) VALUES (CURRENT_USER(), now())'
MYCURSOR.execute(SQL)
MYDB.commit()
# FIM POPULA TBL_LOGIN_LOG

# ABRE INSTAGRAM.COM
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

# AUTENTICAÇÃO
print('Inserindo login e senha.')
LOGIN = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
USER = input('Login: ')  # Ponha seu login aqui
LOGIN.send_keys(USER)

# RECEBE SENHA
PASSWORD = getpass.getpass('Password: ')
PASS_BOX = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
PASS_BOX.send_keys(PASSWORD)

# BOTÃO DE LOGIN
BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()

time.sleep(4)

# HASHTAGS QUE SERÃO BUSCADAS - MODIFIQUE OU ADICIONE LIVREMENTE NO ARQUIVO HASHTAGS.txt
HASHTAGS = open('/home/icaro/Projetos/autoinsta/hashtags.txt', 'r').readlines()

# Randomização do TEMPO de espera entre as ações
TEMPO = [8, 9, 10]

# LÊ ARQUIVO DE COMENTÁRIOS - MODIFIQUE INSERINDO UM COMENTÁRIO POR LINHA
COMMENTS = open('/home/icaro/Projetos/autoinsta/comments.txt', 'r').readlines()

# LOOP INFINITO
while 0 < 1:
    # ESCOLHA RANDOMICA DA HASHTAG
    HASHTAG = random.choice(HASHTAGS)
    DRIVER.get('https://www.instagram.com/explore/tags/' + HASHTAG + '/')
    print(str(HASHTAG))

    DRIVER.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    DRIVER.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(random.choice(TEMPO))

    # ESCOLHA RANDOMICA DO COMENTÁRIO
    TEXT = random.choice(COMMENTS)

    # SELECIONA PUBLICAÇÕES MAIS RECENTES 
    BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[1]/div/div/div[2]/div[1]/a/div').click()

    time.sleep(random.choice(TEMPO))

    # CHECA NO BANCO DE DADOS SE A PUBLICAÇÃO ATUAL JÁ FOI CURTIDA
    URL = DRIVER.current_url
    SQL = "SELECT url FROM tbl_like_log where url =" + "'" + \
        str(URL)+"'" + " and user_login = " + "'"+str(USER)+"'" + ""
    MYCURSOR.execute(SQL)
    LIKES = MYCURSOR.fetchall()
    print(str(LIKES))

    # IF - SE A PUBLICAÇÃO JÁ FOI CURTIDA, AVANÇA PARA PRÓXIMA. SE NÃO DÁ LIKE
    if str(URL) in str(LIKES):
        print(str(URL)+' Já curtimos esta publicação!')
        BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
            '/html/body/div[5]/div[1]/div/div/a').click()
    else:
        BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
        print('Liked!')

    time.sleep(random.choice(TEMPO))

    # SELECIONA CAMPO DE COMENTÁRIO
    BUTTON_ELEMENT = DRIVER.find_element_by_css_selector(
        '.Ypffh').click()

    time.sleep(2)
    BUTTON_ELEMENT = DRIVER.find_element_by_css_selector(
        '.Ypffh')
    time.sleep(2)
    # FAZ COMENTARIO ESCOLIDO RANDOMICAMENTE NO ARQUIVO comments.txt
    BUTTON_ELEMENT.send_keys(TEXT)

    time.sleep(2)

    # CLICA BOTÃO PUBLISH
    BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
        '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]').click()

    time.sleep(random.choice(TEMPO))

    # POPULA TBL_LIKE_LOG NO BANCO DE DADOS
    SQL = 'INSERT INTO tbl_like_log (URL, data_like, comment, hashtag, user_login) VALUES (%s, now(), %s, %s,%s)'
    VAL = (str(URL), str(TEXT), str(HASHTAG), str(USER))
    MYCURSOR.execute(SQL, VAL)
    MYDB.commit()

    # AVANÇA PARA PROXIMA PUBLICAÇÃO
    BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
        '/html/body/div[5]/div[1]/div/div/a[2]').click()
