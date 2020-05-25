<<<<<<< HEAD
=======

>>>>>>> 867c183c51dd50eb208de57cc750e37545f65345
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import App.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            App.routing.websocket_urlpatterns
        )
    ),
})