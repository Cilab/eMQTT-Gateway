if __name__ == '__main__':
    import Queue

    iq = Queue.Queue()
    oq = Queue.Queue()

    s = MqttService(3)
    if not s.connect('192.168.10.40', 1883, clientid='avengalvon', username='cid', password='campeador'):
        sys.stderr.write('Error on connect!')
        sys.exit(-1)

    r = Gateway(
        ser,
        s,
        options.convert and ser_newline or None,
        options.convert and net_newline or None,
    )
