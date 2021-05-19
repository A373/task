from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Newsfeed, Session
import uuid


# Create your views here.
@api_view(['POST'])
def sign_in(request):
    user_name = request.POST.get('user_name', None)
    password = request.POST.get('password', None)
    confirm_password = request.POST.get('confirm_password', None)
    if user_name is None or password is None or confirm_password is None:
        content = {
            'message': 'user_name,password and confirm_password are mandatory'
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    elif user_name is not None:
        new_user = User.objects.create_user(username=user_name, password=password)
        new_user.save()

        content = {
            'user_id': new_user.id,
            'user_name': new_user.username,
            'message': 'new_user has been created succesfully'
        }
        return Response(content, status=status.HTTP_200_OK)


@api_view(['POST'])
def log_in(request):
    user_name = request.POST.get('user_name', None)
    password = request.POST.get('password', None)
    user = authenticate(username=user_name, password=password)
    if user is None:
        content = {
            'message': 'incorrect user_name or password'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)
    else:
        new_token = str(uuid.uuid4())
        new_session = Session.objects.create(
            user_id=user.id,
            token=new_token
        )
        new_session.save()
        content = {
            'token': new_session.token
        }

        return Response(content, status=status.HTTP_200_OK)


@api_view(['POST'])
def news_feed(request):
    token = request.POST.get('token', None)
    if token is None:
        content = {
            'message': 'token cannot be none'
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    try:
        if token.is_active:
            print("token is valid, active and authenticated")
            token_info = Session.objects.get(
                token=token
            )

            news_feeds = Newsfeed.objects.filter(user_id=token_info.user_id)
            feed = []
            for news_feed in news_feeds:
                temp = {
                    'feed_id': news_feed.id,
                    'body': news_feed.body
                }
                feed.append(temp)
            content = {
                'news_feeds': feed
            }
            return Response(content, status=status.HTTP_200_OK)
        else:
            print("token is invalid, the token has been disabled!")
    except Session.DoesNotExist:
        content = {
            'message': 'Authentication failed'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def support(request):
    user_name = request.POST.get('user_name', None)
    password = request.POST.get('password', None)
    user = authenticate(username=user_name, password=password)
    if user is None:
        content = {
            'message': 'Hii, ==== you are not a user of our community ==== ',
            'support_number': '108'
        }
        return Response(content, status=status.HTTP_200_OK)
    elif user is not None:
        content = {
            'message': 'Welcome to our community @' + user.username,
            'support_number': '100'
        }
        return Response(content, status=status.HTTP_200_OK)
