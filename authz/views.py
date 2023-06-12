from django.http import JsonResponse
from django.views import View
from passlib.hash import pbkdf2_sha256
from .models import User


import json
from django.core.exceptions import ValidationError


# Create your views here.
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate(
    'authz/test-5de46-firebase-adminsdk-7x9io-77fc5f03b5.json')

firebase_admin.initialize_app(cred)


class LoginView(View):
    def get(self, request):
        try:
            a = request.session.get("user")
            if a:

                return JsonResponse(a, safe=False,)
            else : 
                return JsonResponse({"message": "Not logged In!"}, status=401, safe=False)
        except:
            return JsonResponse({"message": "Not logged In!"}, status=401, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            try:
                user = User.objects.get(email=username)
            except:
                return JsonResponse({"message": "User not found!"}, status=400)

            if pbkdf2_sha256.verify(password, user.password):
                request.session["user"] = {"email": user.email, "id": user.id}
                print(user.id)
                return JsonResponse({"email": user.email, "name": user.name,  "id": user.id})
            else:
                return JsonResponse({"message": "Password do not match!"}, status=400)

        except Exception as error:
            data = {'message': str(error)}
            return JsonResponse(data, status=400)


def login_with_google(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        access_token = data.get('access_token')
        try:
            print("hello World")
            decoded_token = auth.verify_id_token(access_token)
            print(decoded_token)
            return JsonResponse({"message": "success!"})
        except Exception as error:
            print(error)
            # user token is invalid so give status 401 error
            return JsonResponse({"message": "Login Failed!"}, status=401)


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        password = data.get('password')
        encrypted_password = pbkdf2_sha256.encrypt(password, salt_size=2)
        if (len(password) < 4):
            return JsonResponse({"message": "Password is too short!"}, status=400)
        try:
            user = User(email=data.get('email'), password=encrypted_password)
            try:
                user.full_clean()
            except ValidationError as error:
                response_data = {'status': 'error', 'message': str(error)}
                return JsonResponse(response_data, status=400)

            user.save()
            request.session["user"] = {"email": user.email, "id": user.id}
            response_data = {'status': 'success', 'user_id': user.id}
            return JsonResponse(response_data, status=201)

        except Exception as error:
            JsonResponse({"message": str(error)}, status=400)
