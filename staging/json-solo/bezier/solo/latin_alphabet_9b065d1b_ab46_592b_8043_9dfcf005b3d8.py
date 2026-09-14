"""Latin alphabet (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b065d1b-ab46-592b-8043-9dfcf005b3d8'
SOURCE_PATH = 'icons-json/interface-essential/latin alphabet_9b065d1b-ab46-592b-8043-9dfcf005b3d8.json'
AUTHOR = 'json_to_solo'

class LatinAlphabetInterfaceEssential(Solo48):
    icon_id = 'latin-alphabet-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('latin', 'alphabet', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 39), (40, 24))
        self.add_line('e1', (40, 24), (30, 24))
        self.add_bezier('e2', (36, 7), ((33.137, 5.555), (29.903, 4.009), (26.686, 4.009)), ((26.62, 4.009), (26.554, 4), (26.487, 4)), ((26.486, 4), (26.485, 4), (26.484, 4)), ((26.257, 4), (26.038, 4.018), (25.811, 4.018)), ((15.865, 4.018), (8.008, 12.673), (8.008, 23.409)), ((8.008, 23.624), (8, 23.83), (8, 24.044)), ((8, 24.048), (8, 24.051), (8, 24.055)), ((8, 24.345), (8.008, 24.627), (8.008, 24.918)), ((8.008, 33.045), (12.573, 40.173), (19.663, 42.873)), ((21.373, 43.527), (23.251, 43.982), (25.078, 43.982)), ((25.347, 43.982), (25.617, 44), (25.886, 44)), ((25.891, 44), (25.895, 44), (25.899, 44)), ((26.164, 44), (26.429, 43.982), (26.695, 43.982)), ((29.895, 43.982), (33.541, 43.064), (36.531, 41.891)), ((37.364, 41.564), (39.36, 40.791), (39.848, 39.982)), ((39.949, 39.818), (39.916, 39.164), (40, 39)))
        self.add_contour('c0', 'e2', 'e0', 'e1')
