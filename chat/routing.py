from django.urls import re_path # relative path, a more advanced routing technique
# sometimes a regular path string doesn't quite meet our requirements, this can
# make more advanced paths

from . import consumers

websocket_urlpatterns = [
    # remember consumers are essentially views
    re_path(r'ws/chat/(?P<room_name>\w+)', consumers.ChatRoomConsumer),
]