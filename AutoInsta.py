#!/usr/bin/env python3

import random
import time
from selenium import webdriver
import mysql.connector
import logging

logging.basicConfig(filename=('log.log'),
                    level=logging.info, format=' %(asctime)s - %(levelname)s - %(message)s')

# DADOS LOGIN DATABASE
MYDB = mysql.connector.connect(
    host='',
    user='',
    passwd='',
    database=''
)
# FIM DADOS LOGIN DATABASE
logging.info(MYDB)

# POPULA TBL_LOGIN_LOG
MYCURSOR = MYDB.cursor()
logging.info(MYCURSOR)
SQL = 'INSERT INTO tbl_login_log (user, data_login) VALUES (CURRENT_USER(), now())'
logging.info(SQL)
MYCURSOR.execute(SQL)
MYDB.commit()
# FIM POPULA TBL_LOGIN_LOG

# ABRE INSTAGRAM.COM
DRIVER = webdriver.Firefox()
print('Abrindo instagram.com.')
DRIVER.get('https://www.instagram.com/')
logging.info(DRIVER)

time.sleep(8)

# AUTENTICAÇÃO
print('Inserindo login e senha.')
LOGIN = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
USER = ''  # Ponha seu login aqui
LOGIN.send_keys(USER)
logging.info(LOGIN)
logging.info(USER)

time.sleep(1)

# LÊ ARQUIVO DE SENHA
F = open('passwd.key', 'r')
logging.info(F)
LINES = F.readlines()
logging.info(LINES)
PASSWORD = LINES[0]
logging.info(PASSWORD)
PASS_BOX = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
logging.info(PASS_BOX)
PASS_BOX.send_keys(PASSWORD)
F.close()

time.sleep(1)
# BOTÃO DE LOGIN
BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
logging.info(BUTTON_ELEMENT)
BUTTON_ELEMENT.click()

time.sleep(15)
# BOTÃO NOT NOW
BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/div/div/div/button')
logging.info(BUTTON_ELEMENT)
BUTTON_ELEMENT.click()

time.sleep(1)

# HASHTAGS QUE SERÃO BUSCADAS - MODIFIQUE OU ADICIONE LIVREMENTE NO ARQUIVO HASHTAGS.txt
HASHTAGS_FILE = open('hashtags.txt', 'r')
logging.info(HASHTAGS_FILE)
HASHTAGS = HASHTAGS_FILE.readlines()
logging.info(HASHTAGS)

# Randomização do TEMPO de espera entre as ações
TEMPO = [8, 9, 10]
logging.info(TEMPO)

# LÊ ARQUIVO DE COMENTÁRIOS - MODIFIQUE INSERINDO UM COMENTÁRIO POR LINHA
F = open('comments.txt', 'r')
logging.info(F)
COMMENTS = F.readlines()
logging.info(COMMENTS)

# CATEGORIZA OS POSTS EM POPULARES OU RECENTES
POP_OR_RECENT = ['/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div',
                 '/html/body/div[1]/section/main/article/div[1]/div/div/div[2]/div[1]/a/div']
logging.info(POP_OR_RECENT)

# LOOP INFINITO
while 0 < 1:
    # ESCOLHA RANDOMICA DA HASHTAG
    HASHTAG = random.choice(HASHTAGS)
    logging.info(HASHTAG)
    DRIVER.get('https://www.instagram.com/explore/tags/' + HASHTAG + '/')
    print(str(HASHTAG))

    DRIVER.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    DRIVER.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(random.choice(TEMPO))

    # ESCOLHA RANDOMICA DO COMENTÁRIO
    TEXT = random.choice(COMMENTS)
    logging.info(TEXT)

    # ESCOLHA RANDOMICA DA CATEGORIA
    BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[1]/div/div/div[2]/div[1]/a/div')
    logging.info(BUTTON_ELEMENT)
    BUTTON_ELEMENT.click()

    time.sleep(random.choice(TEMPO))

    # CHECA NO BANCO DE DADOS SE A PUBLICAÇÃO ATUAL JÁ FOI CURTIDA
    URL = DRIVER.current_url
    logging.info(URL)
    SQL = "SELECT url FROM tbl_like_log where url =" + "'" + \
        str(URL)+"'" + " and user_login = " + "'"+str(USER)+"'" + ""
    logging.info(SQL)
    MYCURSOR.execute(SQL)
    LIKES = MYCURSOR.fetchall()
    logging.info(LIKES)

    # IF - SE A PUBLICAÇÃO JÁ FOI CURTIDA, AVANÇA PARA PRÓXIMA. SE NÃO DÁ LIKE
    if str(URL) in str(LIKES):
        print(str(URL)+' Já curtimos esta publicação!')
        BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
            '/html/body/div[5]/div[1]/div/div/a[2]')
        logging.info(BUTTON_ELEMENT)
        BUTTON_ELEMENT.click()
    else:
        BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        logging.info(BUTTON_ELEMENT)
    BUTTON_ELEMENT.click()
    print('Like!')

    time.sleep(random.choice(TEMPO))

    # SELECIONA CAMPO DE COMENTÁRIO
    BUTTON_ELEMENT = DRIVER.find_element_by_css_selector(
        '.Ypffh')
    logging.info(BUTTON_ELEMENT)
    BUTTON_ELEMENT.click()
    time.sleep(2)
    BUTTON_ELEMENT = DRIVER.find_element_by_css_selector(
        '.Ypffh')
    logging.info(BUTTON_ELEMENT)
    time.sleep(2)
    # FAZ COMENTARIO ESCOLIDO RANDOMICAMENTE NA LINHA 92
    BUTTON_ELEMENT.send_keys(TEXT)

    time.sleep(2)

    # CLICA BOTÃO PUBLISH
    BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
        '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]')
    logging.info(BUTTON_ELEMENT)
    BUTTON_ELEMENT.click()

    time.sleep(random.choice(TEMPO))

    # POPULA TBL_LIKE_LOG NO BANCO DE DADOS
    SQL = 'INSERT INTO tbl_like_log (URL, data_like, comment, hashtag, user_login) VALUES (%s, now(), %s, %s,%s)'
    logging.info(SQL)
    VAL = (str(URL), str(TEXT), str(HASHTAG), str(USER))
    logging.info(VAL)
    MYCURSOR.execute(SQL, VAL)
    MYDB.commit()

    # AVANÇA PARA PROXIMA PUBLICAÇÃO
    BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
        '/html/body/div[5]/div[1]/div/div/a[2]')
    logging.info(BUTTON_ELEMENT)
    BUTTON_ELEMENT.click()
