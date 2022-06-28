import pickle

from django.apps import AppConfig
from sentence_transformers import SentenceTransformer
from transformers import BertForQuestionAnswering, BertTokenizer
import numpy as np
import pandas as pd
import os



class ChattingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatting'
    verbose_name = 'A Much Better Name'

    sementic_path = '/home/ubuntu/chat_bot_server/chatting/deeplearning_models/sentencebert'
    embedder = SentenceTransformer(sementic_path)


    data = pd.read_csv('/home/ubuntu/chat_bot_server/데이터-url추가.csv', encoding='cp949')
    data.dropna(inplace=True)
    title = [x for x in data['서비스제목']]
    content = [x for x in data['서비스내용']]
    target = [x for x in data['지원대상']]
    contact = [x for x in data['신청방법']]
    url = [x for x in data['url']]

    ### 피클 파일 불러오기 ###
    with open("/home/ubuntu/chat_bot_server/chatting/title.pickle", "rb") as a:
        embedded_title = pickle.load(a)

    with open("/home/ubuntu/chat_bot_server/chatting/content.pickle", "rb") as b:
        embedded_content = pickle.load(b)

    with open("/home/ubuntu/chat_bot_server/chatting/target.pickle", "rb") as c:
        embedded_target = pickle.load(c)

    with open("/home/ubuntu/chat_bot_server/chatting/contact.pickle", "rb") as d:
        embedded_contact = pickle.load(d)

    with open("/home/ubuntu/chat_bot_server/chatting/url.pickle", "rb") as e:
        embedded_url = pickle.load(e)


    mrc_path = '/home/ubuntu/chat_bot_server/chatting/deeplearning_models/mrc_model'
    mrc_model = BertForQuestionAnswering.from_pretrained(mrc_path, return_dict=False)
    tokenizer = BertTokenizer.from_pretrained(mrc_path,use_fast=False)

    def ready(self):
        pass


