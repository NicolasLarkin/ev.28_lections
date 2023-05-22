# PostgreSQL - система управления базами данных(СУДБ/DBMS)
# Это ряд програм и инструментов позволяющих создавать БД, управлять ею и манипулировать данными внутри(CRUD)

# Postgres - сама база данных, она объектно реляционная , то етсь данные хранятся в виде таблиц, и таблицы имеют сязи между собой

# SQL (Structured Query Language) - декларативный язык структурированных запросов,
# он позволяет он применяется для создания и получения данных при помощи запросов в БД

#--------------------------------------------------------------------------------------------
# команда для входа в БД через юзера postgres:
# sudo -u postgres psql

# команда для входа 
# exit 

# команда для входа в своего юзера 
# psql

# команда для выхода 
# \q

# создние суперюзера
# CREATE ROLE 'username' SUPERUSER LOGIN PASSWORD '1'; 

# изменение пароля 
# ALTER USER 'username' WITH PASSWORD '1';

# создание БД
# CREATE DATABASE 'name' ;

#\l - список всех БД

# \du - все юзеры 

# \dt - все таблицы (нужно подключиться в БД заранее)

# \c 'name' - команда подключения к БД

# psql -U <username> -d <dbname> - подключаемся под выбранным username к dbname

# \d 'name' -> подробная инфа о таблице

# комнада для создания таблицы 
# CREATE TABLE <table name> (
#   <column> <type>,

# CREATE TABLE films (
# code char(5),
# title varchar(100),
# date date,
# ganre varchar(50),
# budget integer,
# country varchar(50),
# id serial
# );

# Команда для добавления данных в таблицу
# INSERT INFO <tablename> [(columns)] VALUES (data), (data) ; :

# INSERT INTO Films (code, title, date, genre, budget, country) VALUES ('AU56', 'Game of Thrones', '2015-05-31', 'Fantasy', 100000, 'U.S.A.'),
# ('het-5', 'Lord of the Rings', '2001-06-12', 'Fantasy', 1923873, 'USA') ;

# Команда для получения данных
# SELECT *(или колонны по отдельности) FROM <table name> ;

# Команда для обновления данных
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value> ;

# Команда для удаления данных
# DELETE FROM <table> WHERE <column> = <value> ;

# ORDER BY: Позволяет анм сортировать выводящие данные по убыванию или возрастанию. 
# ASC(по возрастанию) / DESC(по убыванию)
# Синтаксис : SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC];

# WHERE: используется для фильтрации по полям. Будут выводится только те данные которые соответствуют условию оператора WHERE.
# SELECT <row> FROM <table name> WHERE <row> = 'чему-либо' ;

# BETWEEN: условие между 
# SELECT * FROM <row> WHERE id BETWEEN 3 and 8
# LIKE: выводит результат который соответствует введенному шаблону для строк.
#       Чувствителен к регистру.
# ILIKE: то же самое только не зависит от регистра
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> LIKE/ILIKE 'чему-либо';

# AND оператор и, для множественных условий 
# IN: WHERE <row> IN (1,2,3,4) ;

# Экспорт БД(дамп): 
# pg_dump -u <username> -d 'dbname' > 'file.sql'

#Импорт:
# psql -u <username> -d <dbname> -f <filename> 

# LIMIT: ставит ограничение в кол-во получаемых данных

# GROUP BY: разделяет данные которые мы получаем в SELECT, при этом группируя их по
# - определенному признаку. И теперь для каждой группы можно сипользовать функцию

# Агрегатные функции: AVG(), COUNT(), MIN(), MAX(), SUM(). 

# HAVING: ставит условие при помощи которого данные отбираются в группировку

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Numeric Types(числовые типы)

# 1) smallint(2 bytes) -> -32767 to 32767
# 2) integer(4 bytes) -> -2.147.903 to 2.147.903
# 3) bigint(8 bytes) -> ... to ... (no limits)
# 4) real(4 bytes) -> числа с плавающей точкой (float) - 6 number after the point
# 5) double precsion (8 bytes) - real но только с двойной точностью
# 6) serial (4 bytes) -> integer, auto-increment (has no negative number)

# Character Types (Символьные типы(Строчные))

# 1) varchar(кол-во символов) -> если мы укажем 50 символов, а заполним только 10, то остальные будут свободны, не будет занимать память. Макс 255.
# 2) char(кол-во символов) -> если мы укажем 50 символов, а заполним только 10, то остальные будут заполнены пробелом, не будет занимать память. Макс 255.
# 3) text() -> неограниченное кол-во символов

# Boolen Type 
    # a) boolean(1 bytes) -> True / False 

# Date -> каледарная дата (год/месяц/день)

# Location -> координатная точка (x, y) - (245, -12)

# Enumerate Types:
    # ('a','b','c')
    # CREATE TYPE <any name> AS ENUM ('Happy', 'Sad', 'Mad')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Связи ммежду таблицами(relations):
    # 1. Один к одному (One to one) - человек и паспорт, в одну из таблиц добавляется поле fk и дается ограничение unique
    # 2. Один ко многим (One to Many) - человек и банковские карты, в таблицу много (банковские карты) доб. поле fk
    # 3. Много ко многим (Many to Many) - Студенты и преподы, создается вспомогательная 3-я таблица со связями.
\
# Ограничения : 
    # NOT NULL - обязательное к заполненнию
    # UNIQUE - то что будут хранится только уникальные данные
    # CHECK -> CHECK age > 0 - ограничение проверки на условие
    # PIMARY KEY(для установки идентификатора данных в таблице)
    # FOREIGN KEY(для установления связей между таблицами)
    # ON DELETE - для установки поведения при удалении данных которые были связаны

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# JOIN - выборка данных из двух таблиц, соединение таблиц

# LEFT JOIN - выборка будет содержать все строки из левой таблицы

# RIGHT JOIN - выборка будет содержать все строки из правой таблицы

# SELECT p2.title, p1.prie, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1, orders o1 WHERE p1.id = o1.product_id;
# - Запрос сразу в две таблицы 

# SELECT p2.title, p1.prie, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1 JOIN orders o1 ON p1.id = o1.product_id;

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# 1. Вытащить все произведения в котрых sourse = Moby и кол-во параграфов меньше 100
# SELECT source, totalparagraphs FROM work WHERE source = 'Moby' AND totalparagraphs < 100; 


# 2. Найти кол-во глав в каждом произведении
# select count(*), work.title from chapter join work on work.workid = chapter.workid group by work.title order by count(*) desc;

# 3. Найти сколько произведений относятся к каждому 
# select count(*), genretype from work group by genretype;

# 4. Найти кол-во параграфов в каждом произведении и вытащить названия произведений
# select count(*), work.title from paragraph join work on work.workid = paragraph.workid group by work.title;


# 5. Вытащить имена героев, чьи реплики состовляют больше 200 слов, также произведения в которых они встречаються, жанр, год выхода произдведения в порядке убывания
# select character.charname, work.title, work.genretype, work.year from character_work join character on character.charid = character_work.charid join work on work.workid = character_work.workid where character.speechcount > 200 order by work.year desc;


# 6. Вытащить героя, который чаще всех появляется в произведениях
# SELECT character.charname, COUNT(*) AS works_count FROM character_work JOIN character
# ON character.charid = character_work.charid JOIN work ON character_work.workid = work.workid
# GROUP BY character.charname ORDER BY works_count DESC LIMIT 1;





