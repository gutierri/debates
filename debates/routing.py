from channels.staticfiles import StaticFilesConsumer
from channels.routing import route
from chat.consumers import ws_add, ws_message, ws_disconnect


channel_routing = {
    'http.request': StaticFilesConsumer(),
    'websocket.connect': ws_add,
    'websocket.receive': ws_message,
    'websocket.disconnect': ws_disconnect,
}
