# This is similar to urls.py, but for websocket connections

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    # AuthMiddlewareStack() adds a reference of the current user to websocket scope
    'websocket': AuthMiddlewareStack(
    	# URLRouter routes websocket connections to particular websocket consumers
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})