import time

from selene.support.shared import browser
from selene import command, have
import os
import tests # импорт фото

def test_submit_text_box_form():
    browser.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').type('Alex') # id="firstName"
    browser.element('#lastName').type('Narberkovas')
    browser.element('#userEmail').type('yaebal@gmail.com')

    # browser.element ('#gender-radio-1').double_click()
    male = browser.element('[for=gender-radio-1]')
    male.click() # for="gender-radio-1"
    browser.element('#userNumber').type('8005553535') 

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click() # class="react-datepicker__month-select"
    browser.element('[value="6"]').click() # value="6"
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1995"]').click()
    browser.element('.react-datepicker__day--024').click()

    browser.element('#subjectsInput').type('History').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()


    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), 'files/kappa.png')))
    # abspath возвращает абсолютный путь пути
    # join присоединиться к строкам пути
    # dirname возвращает каталог файла
    # __file__ относится к имени файла script
    # pardir возвращает представление родительского каталога в ОС (обычно ..)


    browser.element('#currentAddress').type('улица Пушкина, дом Колотушкина')
    browser.element('[id="react-select-3-input"]').type('Haryana').press_enter()
    browser.element('[id="react-select-4-input"]').type('Karnal').press_enter()
    browser.element('[id="submit"]').press_enter()

    # THEN
    browser.all('.table-responsive td:nth-child(2)').should(have.texts( # внутри значения атрибута класс table-responsive - пробел на любой глубине вложенности - найти все td это ячейки таблицы, nth-child(2) взять вторые td которые являются ребенком своего родителя
         'Alex Narberkovas',
         'yaebal@gmail.com',
         'Male',
         '8005553535',
         '24 July,1995',
         'History',
         'Sports',
         'kappa.png',
         'улица Пушкина, дом Колотушкина',
         'Haryana Karnal'))

