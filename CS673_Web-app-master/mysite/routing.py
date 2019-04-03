from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from chat.consumers import ChatConsumer
import chat.routing

application = ProtocolTypeRouter({
    'websocket':AllowedHostsOriginValidator(
    		AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )

            )
        )
    

})