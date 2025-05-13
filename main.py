#Код, написанный экспертом в уроке.
# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер
# driver = webdriver.Firefox()
# Если мы используем Chrome, пишем
driver = webdriver.Chrome()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://divan.ru/category/svet"

# Открываем веб-страницу
driver.get(url)

# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
#time.sleep(3)

# Находим все карточки с источниками света (ИС) с помощью названия класса
# Названия классов берём с кода сайта
svets = driver.find_elements(By.CLASS_NAME, 'lsooF')

# Выводим ИС на экран
print(svets)
# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем коллекцию ИС
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for svet in svets:
   try:
   # Находим элементы внутри ИС по значению
       # Находим названия ИС
     title = svet.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').text
     # Находим цену
     price = svet.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
     # Находим ссылку с помощью атрибута 'href'
     link = svet.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
   # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
   except Exception as e:
     print(f"произошла ошибка при парсинге: {e}")
     continue

    # Вносим найденную информацию в список
   parsed_data.append([title, price, link])

# Закрываем подключение браузер
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("svet.csv", 'w',newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название источника освещения', 'Цена', 'Ссылка на источник освещения'])
    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)