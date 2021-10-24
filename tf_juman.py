import collections
from pyknp import Juman

#リスト化する方法
def _juman(text):
    """
    見出し:mrph.midasi
    読み:mrph.yomi
    原形:mrph.genkei
    品詞:mrph.hinsi
    品詞細分類:mrph.bunrui
    活用型:mrph.katuyou1
    活用形:mrph.katuyou2
    意味情報:mrph.imis
    代表表記:mrph.repname
    """
    word_class=[]
    juman = Juman()
    result = juman.analysis(text)
    for mrph in result.mrph_list(): # 各形態素にアクセス
        if mrph.hinsi == "名詞":
            word_class.append(mrph.midasi)
    return word_class

#TF値
def count(text,num):
    i=0
    Count = collections.Counter(text)
    for word,freq in Count.most_common():
        print(str(word)+":"+str(freq))
        i+=1
        if i ==num:
            break

def main():
    text="すもももももももものうち"
    juman = Juman()
    analysis = juman.analysis(text)
    result=[]
    for m in analysis.mrph_list():
        result.append(m.midasi)
    #result = [mrph.midasi for mrph in analysis.mrph_list()]
    print(result)
    l =_juman(text)
    print(l)
    count(l,50)


if __name__ == "__main__":
    main()
