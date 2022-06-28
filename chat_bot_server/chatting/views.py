import json

from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from rest_framework import status, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from chatting import picklemade

from chatting.test import *
from .apps import ChattingConfig
from .models import *
from .serializer import *
import validators

sql_query = "select area from pigon.accounts_userinformation where user_id=(SELECT id FROM pigon.auth_user where " \
            "username=data['user']) "

@permission_classes([AllowAny])
class MyChatViewSet(viewsets.ModelViewSet):
    serializer_class = MyChatSerializer
    queryset = UserChat.objects.all()

    def show_list(self, request):
        user = self.request.user
        queryset = UserChat.objects.filter(user=user)
        serializer = MyChatSerializer(queryset, many=True)

        return Response(serializer.data)

    # @login_required()
    def create(self, request, *args, **kwargs):
        global answer
        global score
        global answer_list

        data = request.data
        print(data)
        data['user'] = self.request.user
        print(data)
        query_dict = QueryDict('', mutable=True)
        query_dict.update(data)
        print(query_dict)
        serializer = MyChatSerializer(
            data=query_dict, context={'request': request}
        )

        if serializer.is_valid():
            serializer.save(user=self.request.user)
            answer, score = sementic_answer([data['my_chat']])
            
            if score > 0.22 :
                answer_list = [[answer[i]['서비스제목'], answer[i]['서비스내용']] for i in range(len(answer))]

                text = str(1) + ". 서비스제목: " + answer_list[0][0] + "\n서비스내용: " + answer_list[0][1] + "\n\n" + \
                       str(2) + ". 서비스제목: " + answer_list[1][0] + "\n서비스내용: " + answer_list[1][1] + "\n\n" + \
                       str(3) + ". 서비스제목: " + answer_list[2][0] + "\n서비스내용: " + answer_list[2][1]

                return Response({'message': text}, status=status.HTTP_200_OK)

            else :
                return Response({'message': answer}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@permission_classes([AllowAny])
class MyChatViewSet2(viewsets.ModelViewSet):
    serializer_class = MyChatSerializer
    queryset = UserChat.objects.all()

    def show_list(self, request):
        user = self.request.user
        queryset = UserChat.objects.filter(user=user)
        serializer = MyChatSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_detail(self, request):
        global ans_json
        data = request.data
        data['user'] = self.request.user
        query_dict = QueryDict('', mutable=True)
        query_dict.update(data)
        serializer = MyChatSerializer(
            data=query_dict, context={'request': request}
        )

        if serializer.is_valid():
            serializer.save(user=self.request.user)
            ans, f_score, ans_json = return_service([data['my_chat']], answer)

            return Response({'message': ans}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class MyChatViewSet3(viewsets.ModelViewSet):
    serializer_class = MyChatSerializer
    queryset = UserChat.objects.all()

    def show_list(self, request):
        user = self.request.user
        queryset = UserChat.objects.filter(user=user)
        serializer = MyChatSerializer(queryset, many=True)
        return Response(serializer.data)

    def detail_info(self, request):
        data = request.data
        data['user'] = self.request.user
        query_dict = QueryDict('', mutable=True)
        query_dict.update(data)
        serializer = MyChatSerializer(
            data=query_dict, context={'request': request}
        )
        
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            info, obj = how_to([data['my_chat']], ans_json)

            if validators.url(obj):
                return Response({'message': info, 'url': obj}, status=status.HTTP_200_OK)

            else:
                return Response({'message': info + "\n" + obj}, status=status.HTTP_200_OK)


        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            