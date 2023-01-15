from selene import have
from selene.support.shared import browser

from demoqa_tests.model.methods.checkbox import Checkbox
from demoqa_tests.model.methods.datepicker import Datepicker
from demoqa_tests.model.methods.dropdown import Dropdown
from demoqa_tests.model.methods.input_tab import InputTab
from demoqa_tests.model.methods.radio import Radio
from demoqa_tests.utils import path, config


class PracticePage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_name(self, student):
        browser.element('#firstName').set_value(student.first_name)
        browser.element('#lastName').set_value(student.last_name)
        browser.driver.execute_script("$('#fixedban').remove()")
        return self

    def fill_contacts(self, student):
        browser.element('#userEmail').set_value(student.email)
        browser.element('#userNumber').set_value(student.phone)
        return self

    def set_gender(self, student):
        gender = Radio(browser.all('[name=gender]'))
        gender.set(student.gender)
        return self

    def input_birthday(self, student):
        birthday_datepicker = Datepicker(browser.element('#dateOfBirthInput'))
        birthday_datepicker.set(student.birthday)
        return self

    def input_subject(self, student):
        input_tab = InputTab(browser.element('#subjectsInput'), browser.all('.subjects-auto-complete__option'))
        input_tab.set_value(student.subject)
        return self

    def set_hobby(self, student):
        select_hobby = Checkbox(browser.all('[for^=hobbies-checkbox]'))
        select_hobby.set(student.hobby)
        return self

    def send_image(self, student):
        browser.element('#uploadPicture').set_value(path.to_resources(student.image))
        return self

    def input_address(self, student):
        browser.element('#currentAddress').set_value(student.address)
        return self

    def select_state(self, student):
        dropdown_state = Dropdown(browser.element('#state'), browser.all('[id^=react-select][id*=option]'))
        dropdown_state.select(student.state)
        return self

    def select_city(self, student):
        dropdown_city = Dropdown(browser.element('#city'), browser.all('[id^=react-select][id*=option]'))
        dropdown_city.select(student.city)
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def fill(self, student):
        self.fill_name(student) \
            .fill_contacts(student) \
            .set_gender(student) \
            .input_birthday(student) \
            .input_subject(student) \
            .set_hobby(student) \
            .send_image(student) \
            .input_address(student) \
            .select_state(student) \
            .select_city(student)
        return self

    def assert_results_registration(self, student):
        browser.all('tbody tr td:last-child').should(have.exact_texts(
            student.first_name + ' ' + student.last_name,
            student.email,
            student.gender,
            student.phone,
            student.birthday.strftime(config.datetime_view_format),
            student.subject,
            ', '.join(hobby.name for hobby in student.hobby),
            student.image,
            student.address,
            student.state + ' ' + student.city))
        return self
