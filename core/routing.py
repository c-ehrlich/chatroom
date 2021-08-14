from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack( # wrap URLs in this to allow for auth
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
