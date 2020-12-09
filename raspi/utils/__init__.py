from api import hx, tempsensor

def get_hx_weight(self):
    return max(0, int(hx.get_weight(5)))

def get_tempsensor(self):
    return max(0, int(tempsensor.get_water_temp()))
