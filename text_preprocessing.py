import re
from pymorphy2 import MorphAnalyzer
from sklearn.metrics.pairwise import cosine_similarity
from run_bot import enc_full, df_base, stopwords_ru, vectors

patterns = r'[^a-zA-Zа-яА-Я0-9ёЁ]'
morph = MorphAnalyzer()

# Поиск похожего текста
def get_sim_text(example):
    simili = cosine_similarity(vectors, enc_full.transform([example]).toarray())
    arg = simili.argmax()
    samp = df_base.iloc[arg, :]
    return f'Title: {samp.title} \n\n Body: {samp.text} \n\n class: {samp.topic}'


def preprocess(text):
    return ' '.join(
        [morph.normal_forms(i)[0] for i in re.sub(patterns, ' ', text.lower()).split() if i not in stopwords_ru])
