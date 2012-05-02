class MqttService(object):
    def __init__(self, keepalive=300, timeout=1):
        self._connected = False
        self._continue = False
        self._keepalive = keepalive
        self._timeout = timeout
        self._subscriptions = { None: [] }
        self._pending = {} # TODO: Timers for re-send all pending
