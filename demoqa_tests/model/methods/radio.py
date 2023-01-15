from selene import have


class Radio:

    def __init__(self, element):
        self.element = element

    def set(self, value):
        self.element.element_by(have.value(value)).element('..').click()