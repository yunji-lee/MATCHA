from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Matzip_list, Star
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re

import pandas as pd
import numpy as np
# from __future__ import (absolute_import, division, print_function,unicode_literals)
import os

from surprise import BaselineOnly
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
from surprise import KNNBasic
# Create your views here.


def index(request):

    return render(request, 'posts/index.html')


def all(request):
    return render(request, 'posts/index.html')


def search(request):
    return render(request, 'posts/search.html')


def star(request):
    return render(request, 'posts/star.html')


def test(request):
    return render(request, 'posts/test.html')


def main(request):
    return render(request, 'posts/main.html')


def lists(request):
    query = request.GET.get('search', '')
    group = Matzip_list.objects.filter(address__contains=query).all()
    paginator = Paginator(group, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {
        'query': query,
        'contacts': contacts,

    }
    return render(request, 'posts/lists.html', context)

def mypage(request):
    file_path = os.path.expanduser('stars.csv')
    start_df = pd.read_csv(file_path, names=['rating', 'id', 'pred'])
    gp = []
    for i in range(len(start_df)):
        gp.append(Matzip_list.objects.filter(id=start_df.id[i]))
    group = []
    for i in range(len(gp)):
        group.append(gp[i][0])
    # group = Matzip_list.objects.get(id=150)
    # group2 = Matzip_list.objects.get(id=155)
    # images = re.sub("]|\[|'", "", group.images_url_preprocess).strip().split(',')
    # images2 = re.sub("]|\[|'", "", group2.images_url_preprocess).strip().split(',')

    context = {
        'group': group,
        # 'group2': group2,
        # 'images': images[0],
        # 'images2': images2[0],

    }
    return render(request, 'posts/mypage.html', context)


def detail(request, post_id):
    # 예상평점 알고리즘 넣기
    file_path = os.path.expanduser('stars.csv')
    reader = Reader(line_format='user item rating', sep=',')
    data = Dataset.load_from_file(file_path, reader=reader)
    trainset = data.build_full_trainset()
    algo = KNNBasic()
    algo.fit(trainset)
    uid = str(request.user.is_authenticated)  # 유저아이디 적어야함
    iid = str(post_id)  # raw item id (as in the ratings file). They are **strings**!

    pred = algo.predict(uid, iid, r_ui=4, verbose=True)   # 예상평점

    group = Matzip_list.objects.get(id=post_id)
    if not request.user.is_anonymous:
        if request.user.star_set.all().filter(matzip_id=post_id).first():
            my_rate = request.user.star_set.all().filter(matzip_id=post_id).first().rate
            is_rated = 1
        else:
            my_rate = pred
            is_rated = 0
    else:
        my_rate = "로그인을 해주세요"
        is_rated = 2
    images = re.sub("]|\[|'", "", group.images_url_preprocess).strip().split(',')


    context = {
        'group': group,
        'images': images,
        'my_rate': my_rate,
        'is_rated': is_rated,
        'pred': pred,
    }
    return render(request, 'posts/detail.html', context)

def personal_info(request):
    return render(request, 'posts/personal_info.html')


def start_check_list(request):
    posts = Post.objects.all()

    context = {
        'posts':posts,
    }
    return render(request, 'posts/start_check_list.html', context)


def star_rating(request, post_id):
    matzip = Matzip_list.objects.get(id=post_id)
    user = request.user
    Star.objects.create(user=user, matzip=matzip, rate=request.GET.get('rate'))
    return redirect('posts:detail', post_id)







