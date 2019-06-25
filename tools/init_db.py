# -*- coding: utf-8 -*-
from peewee import MySQLDatabase

from apps.users.models import User
from apps.community.models import CommunityGroup, CommunityGroupMember, Post, CommentLike, PostComment


dataBase = MySQLDatabase("rt_forum", host="127.0.0.1", user="root", password="root", port=3306)


def init():
    """
    生成数据表
    """
    dataBase.create_tables([User])
    dataBase.create_tables([CommunityGroup, CommunityGroupMember])
    dataBase.create_tables([Post, PostComment, CommentLike])


if __name__ == '__main__':
    init()
