#!/usr/bin/env python3

import random
import time
from selenium import webdriver
import mysql.connector
import logging

logging.basicConfig(filename=('log.log'),
                    level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# DADOS LOGIN DATABASE
MYDB = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='dig0n4o.',
    database='INSTA_BOT'
)
# FIM DADOS LOGIN DATABASE
logging.debug(MYDB)

# POPULA TBL_LOGIN_LOG
MYCURSOR = MYDB.cursor()
logging.debug(MYCURSOR)
SQL = 'INSERT INTO tbl_login_log (user, data_login) VALUES (CURRENT_USER(), now())'
logging.debug(SQL)
MYCURSOR.execute(SQL)
MYDB.commit()
# FIM POPULA TBL_LOGIN_LOG

# ABRE INSTAGRAM.COM
DRIVER = webdriver.Firefox()
print('Abrindo instagram.com.')
DRIVER.get('https://www.instagram.com/')
logging.debug(DRIVER)

time.sleep(8)

# AUTENTICAÇÃO
print('Inserindo login e senha.')
LOGIN = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
USER = ''  # Ponha seu login aqui
LOGIN.send_keys(USER)
logging.debug(LOGIN)
logging.debug(USER)

time.sleep(1)

# LÊ ARQUIVO DE SENHA
F = open('passwd.key', 'r')
logging.debug(F)
LINES = F.readlines()
logging.debug(LINES)
PASSWORD = LINES[0]
logging.debug(PASSWORD)
PASS_BOX = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
logging.debug(PASS_BOX)
PASS_BOX.send_keys(PASSWORD)
F.close()

time.sleep(1)
# BOTÃO DE LOGIN
BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
logging.debug(BUTTON_ELEMENT)
BUTTON_ELEMENT.click()

time.sleep(15)
# BOTÃO NOT NOW
BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
    '/html/body/div[4]/div/div/div[3]/button[2]')
logging.debug(BUTTON_ELEMENT)
BUTTON_ELEMENT.click()

time.sleep(1)

# HASHTAGS QUE SERÃO BUSCADAS - MODIFIQUE OU ADICIONE LIVREMENTE NO ARQUIVO HASHTAGS.txt
HASHTAGS_FILE = open('hashtags.txt', 'r')
logging.debug(HASHTAGS_FILE)
HASHTAGS = HASHTAGS_FILE.readlines()
logging.debug(HASHTAGS)

# Randomização do TEMPO de espera entre as ações
TEMPO = [8, 9, 10, 11, 12, 13, 15, 16, 18, 20, 30, 60, 120]
logging.debug(TEMPO)

# LÊ ARQUIVO DE COMENTÁRIOS - MODIFIQUE INSERINDO UM COMENTÁRIO POR LINHA
F = open('comments.txt', 'r')
logging.debug(F)
COMMENTS = F.readlines()
logging.debug(COMMENTS)

# CATEGORIZA OS POSTS EM POPULARES OU RECENTES
POP_OR_RECENT = ['/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div',
                 '/html/body/div[1]/section/main/article/div[1]/div/div/div[2]/div[1]/a/div']
logging.debug(POP_OR_RECENT)

# LOOP INFINITO
while 0 < 1:
    # ESCOLHA RANDOMICA DA HASHTAG
    HASHTAG = random.choice(HASHTAGS)
    logging.debug(HASHTAG)
    DRIVER.get('https://www.instagram.com/explore/tags/' + HASHTAG + '/')
    print(str(HASHTAG))

    DRIVER.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    DRIVER.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(random.choice(TEMPO))

    # ESCOLHA RANDOMICA DO COMENTÁRIO
    TEXT = random.choice(COMMENTS)
    logging.debug(TEXT)

    # ESCOLHA RANDOMICA DA CATEGORIA
    BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[1]/div/div/div[2]/div[1]/a/div')
    logging.debug(BUTTON_ELEMENT)
    BUTTON_ELEMENT.click()

    time.sleep(random.choice(TEMPO))

    # CHECA NO BANCO DE DADOS SE A PUBLICAÇÃO ATUAL JÁ FOI CURTIDA
    URL = DRIVER.current_url
    logging.debug(URL)
    SQL = "SELECT url FROM tbl_like_log where url =" + "'" + \
        str(URL)+"'" + " and user_login = " + "'"+str(USER)+"'" + ""
    logging.debug(SQL)
    MYCURSOR.execute(SQL)
    LIKES = MYCURSOR.fetchall()
    logging.debug(LIKES)

    # IF - SE A PUBLICAÇÃO JÁ FOI CURTIDA, AVANÇA PARA PRÓXIMA. SE NÃO DÁ LIKE
    if str(URL) in str(LIKES):
        print(str(URL)+' Já curtimos esta publicação!')
        BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
            '/html/body/div[4]/div[1]/div/div/a')
        logging.debug(BUTTON_ELEMENT)
        BUTTON_ELEMENT.click()
    else:
        BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
        logging.debug(BUTTON_ELEMENT)
    BUTTON_ELEMENT.click()
    print('Like!')

    time.sleep(random.choice(TEMPO))

    # SELECIONA CAMPO DE COMENTÁRIO
    BUTTON_ELEMENT = DRIVER.find_element_by_css_selector(
        '.Ypffh')
    logging.debug(BUTTON_ELEMENT)
    BUTTON_ELEMENT.click()
    time.sleep(2)
    BUTTON_ELEMENT = DRIVER.find_element_by_css_selector(
        '.Ypffh')
    logging.debug(BUTTON_ELEMENT)
    time.sleep(2)
    # FAZ COMENTARIO ESCOLIDO RANDOMICAMENTE NA LINHA 92
    BUTTON_ELEMENT.send_keys(TEXT)

    time.sleep(2)

    # CLICA BOTÃO PUBLISH
    BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
        '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button')
    logging.debug(BUTTON_ELEMENT)
    BUTTON_ELEMENT.click()

    time.sleep(random.choice(TEMPO))

    # POPULA TBL_LIKE_LOG NO BANCO DE DADOS
    SQL = 'INSERT INTO tbl_like_log (URL, data_like, comment, hashtag, user_login) VALUES (%s, now(), %s, %s,%s)'
    logging.debug(SQL)
    VAL = (str(URL), str(TEXT), str(HASHTAG), str(USER))
    logging.debug(VAL)
    MYCURSOR.execute(SQL, VAL)
    MYDB.commit()

    # AVANÇA PARA PROXIMA PUBLICAÇÃO
    BUTTON_ELEMENT = DRIVER.find_element_by_xpath(
        '/html/body/div[4]/div[1]/div/div/a')
    logging.debug(BUTTON_ELEMENT)
    BUTTON_ELEMENT.click()
