from django.shortcuts import render
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from rest_framework import generics # generics class-based view 사용할 계획
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated
from django.http import QueryDict
from rest_framework.views import APIView

from .serializer import *
from .models import *

# 누구나 접근가능

@permission_classes([AllowAny])
class Registration(generics.GenericAPIView):
    serializer_class = CustomRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error"}, status=status.HTTP_409_CONFLICT)

        serializer.is_valid(raise_exception=True)
        user = serializer.save(request)
        return Response(
            {
    # get_serializer_context: serializer에 포함되어야 할 어떠한 정보의 context를 딕셔너리 형태로 리턴
    # 디폴트 정보 context는 request, view, format
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data
            },
            status=status.HTTP_201_CREATED,
        )


@permission_classes([AllowAny])
class Login(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    # @api_view(['GET', 'POST'])
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data

        if user['username'] == "None":
            return Response({"message": "fail"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context(),
                ).data,
                "access": user['access']
            }, status=status.HTTP_200_OK
        )


@permission_classes([AllowAny])
class PostListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            if serializer.data.get("new_password") == serializer.data.get("new_password2"):
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    # 'status': 'success',
                    # 'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully'
                }
            else:
                return Response(
                    {"message": "새로운 비밀번호를 다시 확인해주세요"},
                    status=status.HTTP_400_BAD_REQUEST)
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInformationViewSet(viewsets.ModelViewSet):
    serializer_class = UserInformationSerializer
    queryset = UserInformation.objects.all()

    def show_list(self, request):
        user = self.request.user
        queryset = UserInformation.objects.filter(user=user)

        serializer = UserInformationSerializer(queryset, many=True)

        return Response(serializer.data)

    def save_information(self, request, *args, **kwargs):
        data = request.data
        print(data)
        # data['user'] = self.request.user
        print(data)
        query_dict = QueryDict('', mutable=True)
        query_dict.update(data)
        print(query_dict)
        serializer = UserInformationSerializer(
            data=query_dict, context={'request':request}
        )

        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response({'message':'save_success'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_information(self, request):
        data = request.data
        user = self.request.user
        delete_infor = UserInformation.objects.filter(user=user)

        if delete_infor.exists():
            delete_infor.delete()
            return Response({'message':'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'Fail'}, status=status.HTTP_400_BAD_REQUEST)


class UserDelete(generics.DestroyAPIView):
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        delete_user = User.objects.filter(username=user)

        if delete_user.exists():
            delete_user.delete()
            return Response({'message': 'Delete success'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Delete Failed'}, status=status.HTTP_400_BAD_REQUEST)




# 비번 변경 - 1
# class ChangePasswordView(generics.UpdateAPIView):
#
#     queryset = User.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ChangePasswordSerializer
