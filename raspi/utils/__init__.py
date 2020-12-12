from api import hx, tempsensor

def get_hx_weight():
    return max(0, int(hx.get_weight(5)))

def get_tempsensor():
    return max(0, int(tempsensor.get_water_temp()))
