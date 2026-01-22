Описание работы над мини-системой сбора и анализа данных.
1. Генератор.
В качестве предметной области был выбран 5й вариант из таблицы - а именно такси.
Изначально я построил тестовый генератор, который только принтил данные в консоль.
У меня имеется список городов и список зон, куда и откуда у нас могут производиться поездки.
Далее у меня генерируются случаные значения и создаётся словарь с данными о поездке.
На следующем этапе я решил все данные записывать в БД. В mysql я создал БД "taxi" с таблицей поездок.
Далее я подкорректировал мой generator.py, чтобыл данные записывались в таблицу.
2. Docker.
Следующи этапом было завернуть всё в докер. Я добавил в проект Dockerfile для генератора данных, создал docker-compose с двумя сервисами
под SQL и генератор и добавил init.sql для создания бд и таблицы. Командой -docker-compose up поднял 2 контейнера и убедился в работоспособности.
3. Redash
Для работоспособоности Redash мне необходимо было накатить сервисы Redis и Postgres. Добавлены volumes для сохранения данных(mysql_data, redash_postgres_data)
Так же у меня redash-server, redash-worker - обработчик фоновых задач, redash-scheduler - планировщик задач.
Еще немного изменил данные для генерации.
Все это поднимаю командой -docker-compose up.Так же можно поднять через Docker desktop.
Результат:<img width="1568" height="886" alt="image" src="https://github.com/user-attachments/assets/b7d35bb4-a7e2-4387-b47a-3b5135761255" />
Далее я начинаю рабоать с Redash. При первом заходе по ip localhost:5000 мне выдавало ошибку
"Internal Server Error"
The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application."
Для ее фикса понадобилось ввести команду: -docker-compose run --rm redash-server create_db. Эта команда создаёт таблицы в PostgreSQL, без которых Redash не может работать.
Далее я все-таки попал в интерфейс редаша и зарегестрировался. На этом этапе следующей целью было зайти в настройки и привязать мою БД. Тут я столкнулся с тем, что test connect завершался с неизвестной ошибкой и коннекста не просходило. Я в init.sql добавил инициализацию нового пользователя, дабы пофиксить ситуацию с подклчением. Так же немного прошелся по yml файлу. В конечном итоге
подключится к БД с смог только с другого браузера(google, изначально запускал в microsoft edge).
Там я перешел в развел Queries, где сделал 3 запроса и 3 графика:<img width="944" height="971" alt="image" src="https://github.com/user-attachments/assets/31aa569e-bb23-4b87-945c-f46c40c8d7db" />
1<img width="1807" height="836" alt="image" src="https://github.com/user-attachments/assets/9d76dfef-e66e-48f1-8d26-4769cba356c3" />
<img width="1410" height="425" alt="image" src="https://github.com/user-attachments/assets/8199ab40-b970-453c-88d6-bb4456ff8f60" />
2. <img width="1812" height="878" alt="image" src="https://github.com/user-attachments/assets/e225dc44-324f-4f85-b5a2-11f10e4db286" />
<img width="1358" height="320" alt="image" src="https://github.com/user-attachments/assets/043216fe-c92a-4d13-8024-099d6d7c0b64" />
3. <img width="1823" height="880" alt="image" src="https://github.com/user-attachments/assets/addda7f5-7a62-4f78-860a-5c9d08df58d4" />
<img width="1363" height="418" alt="image" src="https://github.com/user-attachments/assets/cb37acb4-34d3-42da-bc01-0eb1d06f95f7" />
Далее я делаю Dashboard, куда закидывю все графики <img width="1811" height="893" alt="image" src="https://github.com/user-attachments/assets/e4c1991f-0494-4b6a-a943-078714f8734d" />
Так как у меня данные генеряться на рандоме в одинаковых примрено диапозонах, данные на графиках относительно равны между собой.

Таким образом, мной создана полностью работоспособная end-to-end система сбора и анализа данных, соответствующая всем требованиям задания:

Генератор создаёт осмысленные данные о поездках такси
Данные сохраняются в MySQL с использованием Docker volumes
Redash предоставляет интерактивный дашборд с тремя визуализациями
Вся система запускается одной командой docker-compose up





