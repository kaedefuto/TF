import sys
import MeCab
import collections

#リスト化する方法
def mecab_list(text):
    tagger = MeCab.Tagger("mecabrc")
    tagger.parse('') # UnicodeDecodeErrorを避けるため
    node = tagger.parseToNode(text) # nodeにsurface(単語),feature(品詞情報)を代入
    word_class = []
    while node:
        word = node.surface # 単語
        wclass = node.feature.split(',') # 品詞情報をリスト化
        if wclass[0] != u'BOS/EOS': #最初と最後
            if wclass[0] == "名詞":
                word_class.append(word)
        node = node.next # 次の単語
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
    """
    *初期
    mecabrc:(デフォルト)
    -Ochasen:(ChaSen 互換形式)
    -Owakati:(分かち書きのみを出力)
    -Oyomi:(読みのみを出力)

    *自分の環境の辞書も使える
    -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd:neologd辞書
    """
    text = "すもももももももものうち"
    m = MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    print(m.parse(text))

    l = mecab_list(text)
    count(l,50)

if __name__ == "__main__":
    main()
