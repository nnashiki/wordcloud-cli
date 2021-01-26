from wordcloud import WordCloud
import MeCab
from wordcloudja.stopwords import stop_lists
import os


def wakati(text):
    tagger = MeCab.Tagger('')
    tagger.parse('')
    node = tagger.parseToNode(text)
    word_list = []

    while node:
        pos = node.feature.split(",")[0]
        # 品詞を選択
        if pos in ["形容詞", "動詞", "名詞"]:
            word = node.surface
            word_list.append(word)
        node = node.next

    return word_list


def text_to_img(text: str, out: str):
    wakati_texts = " ".join(wakati(text))
    wordcloud = WordCloud(background_color="white",
                          width=900,
                          height=500,
                          font_path=os.path.dirname(__file__) + '/data/ipaexm.ttf',
                          stopwords=set(stop_lists)
                          ).generate(wakati_texts)
    wordcloud.to_file(out)
