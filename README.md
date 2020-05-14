# AutoInsta

1. Tenha o banco MySQL instalado.

2. Crie uma base de dados:
Ex: CREATE DATABASE `AUTOINSTA` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */

3. Crie as tabelas necessárias para registro de likes, comentários e atividade de login:
Ex: CREATE TABLE `tbl_like_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `data_like` datetime NOT NULL,
  `comment` varchar(10000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `hashtag` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_login` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

Ex: CREATE TABLE `tbl_login_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `data_login` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

4. Insira a senha da sua conta na primeira linha do arquivo 'passwd.key'

5. Substitua os textos dos comentários ao seu gosto no arquivo 'comments.txt'. (Um comentário por linha)

6. Subistitua as palavras chaves (hashtags) na linha 69 do arquivo 'AutoInsta.py' pelas que você deseja.

7. Dê permissões de execução ao arquivo 'AutoInsta.py':
Ex: $ sudo chmod +x AutoInsta.py

8. Rode o script:
Ex: ./AutoInsta.py