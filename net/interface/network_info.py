class NetworkInfo:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac

    def get_ip_addr(self):
        return self.ip

    def get_mac_addr(self):
        return self.mac

    def to_string(self):
        return '{}{}{}'.format(self.ip, '\t', self.mac)