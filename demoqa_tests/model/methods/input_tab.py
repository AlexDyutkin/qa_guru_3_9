from selene import have, be


class InputTab:

    def __init__(self, element, elements):
        self.element = element
        self.elements = elements

    def set_value(self, value):
        self.element.type(value)
        self.elements.element_by(have.exact_text(value)).should(be.visible)
        self.element.press_tab()
