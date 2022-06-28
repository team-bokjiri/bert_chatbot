# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/ubuntu/chat_bot_server/')
from chatting.test import *


condition = True

print('안녕하세요 복지친구 복지리예요.\n어떤 도움이 필요하신지 말씀해주시면 정보를 제공해드려요.\n채팅종료를 원하시면 종료라고 입력해주시면 됩니다.')


while condition:
    query = input('어떤 도움이 필요하신가요?: ')

    if query != '종료':
        ans_list, score = sementic_answer([query])
        for text in ans_list:
            for t in text:
                t.replace('\n', '')
        print(ans_list)
        print('관심있는 서비스를 골라주세요.\n만약 없다면 `아니`를 입력해주세요.')

        query2 = input()

        if query2 != '아니':

            title,score,answer = return_service([query2])
            print(title," 일치도: %.4f" % score)



        while condition:
            print('어떤게 궁금하신가요?\n필요한게 없으시면 `아니`를 입력해주시면 됩니다.')
            query3 = input()

            if query3 != '아니':
                if query3 == '종료':
                    condition = False

                else:
                    how = how_to([query3])
                    print(how)
                    continue

            else:
                break

        else :
            break

