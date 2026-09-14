"""5 (text) (text), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7313b9de-e69b-43f7-8caa-a6ffcfca182e'
SOURCE_PATH = 'icons-json/text/5 (text)_7313b9de-e69b-43f7-8caa-a6ffcfca182e.json'
AUTHOR = 'json_to_solo'

class Icon5TextText(Solo48):
    icon_id = 'icon-5-text-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('text',)

    def build(self):
        self.add_line('e0', (38, 4), (13, 4))
        self.add_line('e1', (13, 4), (9, 22))
        self.add_bezier('e2', (9, 22), ((15.4, 18.645), (23.729, 17.527), (31.151, 19.9)), ((34.892, 21.091), (37.748, 23.245), (39.065, 26.109)), ((39.618, 27.318), (39.975, 28.655), (39.975, 29.927)), ((39.975, 30.191), (40, 30.455), (40, 30.718)), ((40, 30.721), (40, 30.724), (40, 30.727)), ((40, 30.915), (39.988, 31.103), (39.988, 31.291)), ((39.988, 37.891), (33.415, 43.982), (23.951, 43.982)), ((23.631, 43.982), (23.323, 44), (23.003, 44)), ((22.997, 44), (22.992, 44), (22.986, 44)), ((22.622, 44), (22.259, 43.982), (21.883, 43.982)), ((17.932, 43.982), (13.132, 43.3), (10.178, 41.2)), ((9.477, 40.709), (8.012, 39.391), (8.012, 38.6)), ((8.012, 38.582), (8, 39.018), (8, 39)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
