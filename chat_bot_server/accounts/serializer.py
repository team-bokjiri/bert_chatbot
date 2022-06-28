from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *


# 기본 유저 모델 불러오기
User = get_user_model()

# 회원가입
class CustomRegisterSerializer(RegisterSerializer):
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()

        return data_dict

#로그인
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=30, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # username = data.get("username")
        username = data.get("username")
        password = data.get("password", None)

        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            return {'username': 'None'}
        try:
            update_last_login(None, user)
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            print(access)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does not exist'
            )
        return {
            'id': user.id,
            'username': user.username,
            'access': access,
        }

# 사용자 정보 추출
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=False)
    new_password = serializers.CharField(required=False)
    new_password2 = serializers.CharField(required=False)


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        exclude = ['user']









# 비번 변경 - 1
# class ChangePasswordSerializer(serializers.Serializer):
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#     old_password = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = User
#         fields = ('old_password', 'password', 'password2')
#
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})
#
#         return attrs
#
#     def validate_old_password(self, value):
#         user = self.context['request'].user
#         if not user.check_password(value):
#             raise serializers.ValidationError({"old_password": "Old password is not correct"})
#         return value
#
#     def update(self, instance, validated_data):
#
#         instance.set_password(validated_data['password'])
#         instance.save()
#
#         return instance