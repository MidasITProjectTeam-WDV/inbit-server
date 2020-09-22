import json
import jwt
import bcrypt
from django.views import View
from django.http import JsonResponse
from django.conf import settings
from .serializers import UserSerializer
from .authentication import JSONWebTokenAuthentication
from .models import Users


# Create your views here.
class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        Users(
            email = data["email"],
            name = data["name"],
            password = data["password"],
            phone_num = data["phone_num"],
            position = data["position"],
        )
    
        if Users.objects.filter(email = data["email"]).exists() == True:
            response = JsonResponse({"message":"already existed email"}, status = 401)
            return response
        else:
            # password = data["password"].encode('utf-8')
            # password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())
            # password_crypt = password_crypt.decode('utf-8')
            Users.objects.create(email = data["email"], name = data["name"], password = data["password"], phone_num = data["phone_num"], position = data["position"],)
            response =  JsonResponse({"message":"successfully registered"}, status = 200)
            return response

class LoginView(View):

    def post(self, request):
        data = json.loads(request.body)
        try:    
            if Users.objects.filter(email = data["email"]).exists():
                user = Users.objects.get(email= data["email"])
                if Users.objects.get(email=data["email"], password=data["password"]):
                    token = jwt.encode({'email': data['email']}, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
                    token = token.decode('utf-8')
                    response = JsonResponse({"message": "login success", "token": token, "email": data["email"]}, status=200)
                    return response
                else:
                    response = JsonResponse({"message":"password not matched"})
                    return response
            else:
                response = JsonResponse({"message":"email isn't existed"}, status = 400)
                return response
        except KeyError:
            response = JsonResponse({"message": "INVALID_KEYS"}, status = 400)
            return response
            


class LogoutView(View):
    def delete(self, request):
        request.user.auth_token.delete()
        return JsonResponse(status=status.HTTP_200_OK)