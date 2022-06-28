import pickle

from sentence_transformers import SentenceTransformer
import pandas as pd

sementic_path = '/home/ubuntu/chat_bot_server/chatting/deeplearning_models/sentencebert/'
embedder = SentenceTransformer(sementic_path)
data = pd.read_csv('/home/ubuntu/chat_bot_server/데이터-url추가.csv', encoding='cp949')

data.dropna(inplace=True)
title = [x for x in data['서비스제목']]
content = [x for x in data['서비스내용']]
target = [x for x in data['지원대상']]
contact = [x for x in data['신청방법']]
url = [x for x in data['url']]


def make_embedding(lst=[]):
    basic = [x for x in lst]
    _list = [[x] for x in basic]
    list_ = ' '.join(map(str, _list))
    list_first = list_.split('] [')
    list_first[0].replace('[', '')

    for i in range(len(list_first)):
        list_first[i].replace('"', '')

        corpus = list_first
        corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

        return corpus_embeddings


embedded_title = make_embedding(title)
embedded_content = make_embedding(content)
embedded_target = make_embedding(target)
embedded_contact = make_embedding(contact)
embedded_url = make_embedding(url)
