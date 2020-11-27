class TextManager:

    @staticmethod
    def reader(route):
        res = ""
        with open(route, 'r') as File:
            lines = File.readlines()
            for line in lines:
                res += line
        return res

    @staticmethod
    def writer(route, res):
        with open(route, 'w') as File:
            for line in res.splitlines():
                File.write(line+"\n")
