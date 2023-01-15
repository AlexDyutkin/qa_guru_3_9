from selene import have


class Checkbox:

    def __init__(self, element):
        self.element = element

    def set(self, list_value):
        for hobby in list_value:
            self.element.element_by(have.exact_text(hobby.name)).click()



