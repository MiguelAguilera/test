from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from ensemble.links.views import LinkList, LinkCreate, LinkDetail, CommentList, TagList


urlpatterns = patterns("",
    url("^$",
        LinkList.as_view(), {"order": "hot"},
        name="home"),
    url("^hot/$",
        LinkList.as_view(), {"order": "hot"},
        name="link_list_hot"),
    url("^consensus/$",
        LinkList.as_view(), {"order": "consensus"},
        name="link_list_consensus"),
    url("^latest/$",
        LinkList.as_view(), {"order": "latest"},
        name="link_list_latest"),
    url("^top/$",
        LinkList.as_view(), {"order": "top"},
        name="link_list_top"),
    url("^comments/$",
        CommentList.as_view(), {"by_score": False},
        name="comment_list_latest"),
    url("^link/create/$",
        login_required(LinkCreate.as_view()),
        name="link_create"),
    url("^link/(?P<slug>.*)/$",
        LinkDetail.as_view(),
        name="link_detail"),
    url("^users/(?P<username>.*)/links/$",
        LinkList.as_view(), {"by_score": False},
        name="link_list_user"),
    url("^users/(?P<username>.*)/links/$",
        LinkList.as_view(), {"by_score": False},
        name="link_list_user"),
    url("^users/(?P<username>.*)/comments/$",
        CommentList.as_view(), {"by_score": False},
        name="comment_list_user"),
    url("^tags/$",
        TagList.as_view(),
        name="tag_list"),
    url("^tags/(?P<tag>.*)/$",
        LinkList.as_view(),
        name="link_list_tag"),
)