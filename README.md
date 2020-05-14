<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/gPnZgt8.png" alt="Project logo"></a>
</p>

<h3 align="center">AutoInsta</h3>

<div align="center">

<!-- [![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE) -->

</div>

---

<p align="center"> Automatically manage Instagram accounts with likes and comments guided by hashtags.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
<!-- - [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
 -->
 - [Authors](#authors)
 
## 🧐 About <a name = "about"></a>

The intention is to automate business account interactions with your customers, redirecting them to support or sales emails.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Python3

```

### Installing

```
1. Have the MySQL database installed
```

```
2. Create a data base to project:
Ex:
CREATE DATABASE AUTOINSTA /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */

```

```
3. Create the necessary tables to record likes, comments and login activity:
Ex: 
CREATE TABLE tbl_like_log ( id int(11) NOT NULL AUTO_INCREMENT
	, url varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
	, data_like datetime NOT NULL
	, comment varchar(10000) COLLATE utf8mb4_unicode_ci DEFAULT NULL
	, hashtag varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL
	, user_login varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL
	, PRIMARY KEY (id) ) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

CREATE TABLE tbl_login_log ( id int(11) NOT NULL AUTO_INCREMENT
	, user varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
	, data_login datetime NOT NULL
	, PRIMARY KEY (id) ) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

```

```
4. Enter your account password on the first line of the 'passwd.key' file.
```
```
5. Replace the text of the comments to your liking in the 'comments.txt' file. (One comment per line).
```
```
6. Replace the keywords (hashtags) in line 69 of the 'AutoInsta.py' file with the ones you want.
```
```
7. Give execute permissions to the 'AutoInsta.py' file:
Ex: $ sudo chmod + x AutoInsta.py
```
```
8. Run the script:
Ex: ./AutoInsta.py
```

<!-- End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment
 -->
## ✍️ Authors <a name = "authors"></a>

- [@icaromsales](https://github.com/icaromsales) - Idea & Initial work

<!-- See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
 -->