from pypinyin import pinyin

class LocalPyTranslte:
    def __init__(self):
        pass


    def combine(self, l):
        out_l = []
        for i in l:
            out_l.append(i[0])
        return out_l


    def translate(self, text):
        map = {}
        map["text"] = text
        pinyin_result = pinyin(text)
        pinyin_list = self.combine(pinyin_result)
        pinyin_words = ' '.join(pinyin_list)
        map["pinyin"] = pinyin_words
        return map


    def test(self, text):
        res = pinyin(text)


    def text(self, text):
        res = pinyin(text)
        pinyin_list = self.combine(res)
        pinyin_words = ' '.join(pinyin_list)
        return pinyin_words
        

if __name__ == "__main__":
    tran = LocalPyTranslte()
    tran.translate("123")