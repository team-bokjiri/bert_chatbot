import torch
import pandas as pd
from sentence_transformers import util
import numpy as np
from chatting import apps
from chatting.apps import ChattingConfig
from chatting.picklemade import make_embedding, embedder
from functools import reduce





def sementic_answer(queries=[]):
    global ans_list
    top_k = 3
    title = []
    content = []
    target = []
    contact = []
    url = []
    score_list = []

    for query in queries:
        query_embedding = ChattingConfig.embedder.encode(query, convert_to_tensor=True)
        cos_scores = util.pytorch_cos_sim(query_embedding, ChattingConfig.embedded_content)[0]  # 질문과 데이터
        cos_scores = cos_scores.cpu()

        # We use np.argpartition, to only partially sort the top_k results

        top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]
        # type(top_results) = <class 'torch.Tensor'>

        for idx in top_results[0:top_k]:
            title.append(ChattingConfig.title[idx])
            content.append(ChattingConfig.content[idx])
            target.append(ChattingConfig.target[idx])
            contact.append(ChattingConfig.contact[idx])
            url.append(ChattingConfig.url[idx])
            score_list.append(cos_scores[idx])

            ans_list = [{'서비스제목': x[0], '서비스내용': x[1], '지원대상': x[2], '신청방법': x[3], 'url': x[4], 'score':x[5]} for x in
                        zip(title, content, target, contact, url, score_list)]

            score = cos_scores[idx]

            if score < 0.22:
                return "어떤 도움이 필요하신지 정확하게 입력해주세요~", score

        return ans_list, score


def return_service(queries=[], ans_list=[]):

    corpus = ['첫번째,1번,처음,맨앞', '두번째,2번,가운데', '세번째,3번,마지막,맨뒤']

    title_list = [ans_list[i]['서비스제목'] for i in range(len(ans_list))]
    contact_list = [ans_list[i]['신청방법'] for i in range(len(ans_list))]
    target_list = [ans_list[i]['지원대상'] for i in range(len(ans_list))]
    url_list = [ans_list[i]['url'] for i in range(len(ans_list))]

    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)
    top_k = 1

    for query in queries:
        query_embedding = embedder.encode(query, convert_to_tensor=True)
        cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
        cos_scores = cos_scores.cpu()

        # We use np.argpartition, to only partially sort the top_k results
        top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]

        for idx in top_results[0:top_k]:
            score = cos_scores[idx]
            answer = {'서비스제목': title_list[idx],
                      '신청방법': contact_list[idx],
                      '지원대상': target_list[idx],
                      'url': url_list[idx]}

            if score < 0.4:

                title_embeddings = embedder.encode(title_list, convert_to_tensor=True)
                cos_scores = util.pytorch_cos_sim(query_embedding, title_embeddings)[0]  # 질문과 데이터
                cos_scores = cos_scores.cpu()
                top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]
                # type(top_results) = <class 'torch.Tensor'>

                for ix in top_results[0:top_k]:
                    f_score = cos_scores[idx]

                    if f_score > 0.3:
                    
                        answer = {'서비스제목': title_list[ix],
                                  '신청방법': contact_list[ix],
                                  '지원대상': target_list[ix],
                                  'url': url_list[ix]}
                        c_score = cos_scores[ix]

                        if queries[0] in title_list:
                            return answer['서비스제목'] + "을(를) 선택하신 게 맞나요?", c_score, answer

                        else:
                            return answer['서비스제목'] + "을(를) 입력하신 게 맞나요?", c_score, answer

                    else:
                        return "잘 모르겠어요ㅠㅜ 복지리가 더 공부해야겠어요", f_score, "no"
            else:
                return answer['서비스제목'] + "을(를) 선택하신 게 맞나요?", score, answer




def how_to(queries=[], answer={}):
    corpus = ['지원대상 알려줘,누가 지원할 수 있어?,어떤 사람을 지원해?,누가 신청할 수 있어?',
              '어떻게 신청해?, 신청방법이 뭐야? 지원방법이 뭐야? 어디서 신청해? 어디에 신청해?',
              'url 알려줘, 주소 알려줘, 자세하게 보여줘']
    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)
    top_k = 1

    for query in queries:
        query_embedding = embedder.encode(query, convert_to_tensor=True)
        cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
        cos_scores = cos_scores.cpu()

        # We use np.argpartition, to only partially sort the top_k results
        top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]

        for idx in top_results[0:top_k]:
            index = corpus[idx].strip()

            if index == corpus[0]:
                return "지원대상을 알려 드리겠습니다!\n",answer['지원대상']
            elif index == corpus[1]:
                return "신청방법을 알려 드리겠습니다!\n",answer['신청방법']
            elif index == corpus[2]:
                return "더 자세한 정보를 원하시면 이동하기를 입력해주세요\n",answer['url']





