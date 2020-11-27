from TextManager import TextManager

class Converter:
    def ass_to_meluk(self, route: str):
        file = TextManager.reader(route)
        return file