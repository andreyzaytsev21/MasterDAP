class CaseStr:
    def __init__(self, ip, rp, dp, vp, tp, pp):
        self._ip = ip
        self._rp = rp
        self._dp = dp
        self._vp = vp
        self._tp = tp
        self._pp = pp

    def to_json(self):
        return {
            "ip": self._ip,
            "rp": self._rp,
            "dp": self._dp,
            "vp": self._vp,
            "tp": self._tp,
            "pp": self._pp
        }