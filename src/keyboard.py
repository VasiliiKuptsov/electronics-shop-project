

from src.item import Item

class Keyboard(Item, MixinLog):
    def __init__(self,language):
        self.language = language

class MixinLog:
    LANGUAGE = 'EN'
    def __init__(self):
        self.language = LANGUAGE
        MixinLog.LANGUAGE = change_lang()



    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'



