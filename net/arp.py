from scapy.all import srp, Ether, ARP
from net.interface.network_info import NetworkInfo
from typing import List


class ARPScanner:
    def __init__(self, dst="ff:ff:ff:ff:ff:ff", pdst="192.168.1.0/24"):
        self.dst = dst
        self.pdst = pdst

    def all(self) -> List[NetworkInfo]:
        result = []
        ans, _ = srp(Ether(dst=self.dst)/ARP(pdst=self.pdst), timeout=5)
        for _, received in ans:
            result.append(NetworkInfo(received.psrc, received.hwsrc))
        return result
