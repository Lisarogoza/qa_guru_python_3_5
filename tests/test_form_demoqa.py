import os
from selene.support.shared import browser
from selene import be, have

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'pictures/image.png')


def test_fill_reg_form():
    browser.open("/automation-practice-form")
    browser.element('#firstName').should(be.blank).type('Иван')
    browser.element('#lastName').should(be.blank).type('Севцов')
    browser.element('#userEmail').should(be.blank).type('s1e5v7_8l9e0f3@ya.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('89200000000')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select>option[value="1"]').click()
    browser.element('.react-datepicker__year-select>option[value="1998"]').click()
    browser.element('.react-datepicker__day--014').click()
    browser.element('#subjectsInput').should(be.blank).type('Physics').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element('#currentAddress').should(be.blank).type('Прианка Чопра стрит, 504')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').press_enter()
    browser.element('.table').should(have.text('Иван'
                                               and 'Севцов'
                                               and 's1e5v7_8l9e0f3@ya.ru'
                                               and 'Male'
                                               and '89200000000'
                                               and '14 Feb 1998'
                                               and 'Physics'
                                               and 'Music'
                                               #and 'photo.jpeg'
                                               and 'Прианка Чопра стрит, 504'
                                               and 'NCR'
                                               and 'Noida'))



