# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 9:02
# @Author  : Yaojie Chang
# @File    : DataVerify.py
# @Software: PyCharm
from django.http import JsonResponse
from django.views import View
import random
import redis


class DataVerifyView(View):
    def post(self, request):
        """信息验证以及二次请求的token的获取，"""
        name = request.POST.get('name', '')
        major = request.POST.get('major', '')
        if not is_chinese(name):
            return JsonResponse({'code': 0, 'msg': '小可爱姓名是不是输错啦？'})
        if not is_chinese(major):
            return JsonResponse({'code': 0, 'msg': '小可爱是不是专业输错啦？不输入班级哦！'})
        ticket_type = request.POST.get('ticket_type', '')
        stu_id = request.POST.get('stu_id', '')
        times = request.POST.get('times', '')
        try:
            int_stu_id = int(stu_id)
        except:
            int_stu_id = 0
        if 2019000000 <= int_stu_id < 2019008000:
            r = redis.StrictRedis(decode_responses=True)
            if r.hsetnx(ticket_type+'-U-' + times + '-' + stu_id, 'stu_id', stu_id):
                all_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-'
                token_code = ''.join(random.choices(all_char, k=20))
                r.set('token-' + token_code, 1)
                return JsonResponse({'code': 1, 'token_code': token_code})
            else:
                return JsonResponse({'code': 2, 'msg': '小可爱已经抢过本时间段的票啦！'})
        elif len(stu_id) != 10:
            return JsonResponse({'code': 0, 'msg': '小可爱学号输错啦！'})
        elif stu_id[:4] != '2019':
            return JsonResponse({'code': 0, 'msg': '抱歉，只有2019新生可以抢票哦！'})


def is_chinese(check_string):
    for char in check_string:
        if not('\u4e00' <= char <= '\u9fa5'):
            return False
    return True


