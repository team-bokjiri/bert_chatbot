from sentence_transformers import util
import numpy as np
from chatting import apps
from chatting.apps import ChattingConfig

def sementic_answer(queries=[]):

    top_k = 3
    for query in queries:
        query_embedding = apps.embedder.encode(query, convert_to_tensor=True)
        cos_scores = util.pytorch_cos_sim(query_embedding, ChattingConfig.embedded_content)[0]
        cos_scores = cos_scores.cpu()


        #We use np.argpartition, to only partially sort the top_k results
        top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]
        # type(top_results) = <class 'torch.Tensor'>

        # print("\n\n======================\n")
        print("질문:", query)

        # Find the pairs with the highest cosine similarity scores

        # return top_results, cos_scores

        for idx in top_results[0:top_k]:


            title = ChattingConfig.title[idx].strip()
            content = ChattingConfig.content[idx].strip()
            target = ChattingConfig.target[idx]
            score = cos_scores[idx]


            answer = title, content, target, score

            return answer, score