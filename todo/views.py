from rest_framework import viewsets
from .serializer import TodoSerializer, UserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from rest_framework.decorators import api_view, APIView

from todo.models import Todo

@api_view(['GET'])
def index(request, pk):
    todo = Todo.objects.get(pk=1)
    ser = TodoSerializer(todo)
    return Response(request.query_params) 

# with httpresponse
# def index(request):
#     todo = Todo.objects.get(pk=1)
#     ser= TodoSerializer(todo)
#     print(ser.data)
#     return HttpResponse("Hello! World")

@api_view(['POST'])
def dummy(request):
    todo = Todo(task=request.data["task"])
    todo.save()
    return Response(request.data)


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = (DjangoModelPermissions,)

class UserAuth(APIView):
    """
    Manager User Login and other things
    """
    def post(self, request):
        """
        login
        """
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if user is not None:
            # A backend authenticated the credentials
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(token.key)
        else:
            # No backend authenticated the credentials
            return Response([], status=status.HTTP_401_UNAUTHORIZED)

    permission_classes = (IsAuthenticated,)
    def get(self, request):
        ser = UserSerializer(request.user)
        return Response(ser.data)


class UserRegister(APIView):
    """
    Create user 
    """

    def post(self, request):
        user = User.objects.create_user(
            username=request.data.get("username"),
            email=request.data.get("email"),
            password=request.data.get("password"))
        user.save()

        if user is not None:
            token = Token.objects.create(user=user)
            print(token.key)
            print(user)
            return Response(token.key)
        else:
            return Response([], status=status.HTTP_400_BAD_REQUEST)