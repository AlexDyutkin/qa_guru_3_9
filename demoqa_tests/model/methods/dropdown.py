from selene import have


class Dropdown:

    def __init__(self, element, elements):
        self.element = element
        self.elements = elements

    def select(self, value):
        self.element.click()
        self.elements.element_by(have.exact_text(value)).click()
