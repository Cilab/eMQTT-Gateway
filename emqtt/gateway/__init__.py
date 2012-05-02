import threading

class Gateway(object):
    def __init__(self, serial, mqtt, iq, oq):
        self.serial = serial
        self.mqtt = mqtt
        self.iq = iq
        self.oq = oq
        self._write_lock = threading.Lock()

    def shortcut(self):
        self.alive = True
        self.thread_read = threading.Thread(target=self.reader)
        self.thread_read.setDaemon(True)
        self.thread_read.setName('serial->mqtt')
        self.thread_read.start()

        self.thread_write = threading.Thread(target=self.writer)
        self.thread_write.setDaemon(True)
        self.thread_write.setName('mqtt->serial')
        self.thread_write.start()
