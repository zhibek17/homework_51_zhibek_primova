from django.urls import path

from cat_game.views import index_view, cat_stats_view

urlpatterns = [
    path('', index_view),
    path('cat_stats/', cat_stats_view),
]