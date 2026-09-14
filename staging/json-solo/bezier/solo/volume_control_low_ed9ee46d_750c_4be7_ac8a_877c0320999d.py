"""Volume control low (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed9ee46d-750c-4be7-ac8a-877c0320999d'
SOURCE_PATH = 'icons-json/audio/volume control low_ed9ee46d-750c-4be7-ac8a-877c0320999d.json'
AUTHOR = 'json_to_solo'

class VolumeControlLowAudio(Solo48):
    icon_id = 'volume-control-low-audio'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'low', 'audio')

    def build(self):
        self.add_line('sym-e0', (19, 32), (19, 16))
        self.add_line('sym-e1', (19, 16), (12, 16))
        self.add_bezier('sym-e2', (12, 16), ((10.585, 16), (8.775, 15.527), (8, 17)))
        self.add_bezier('sym-e3', (8, 17), ((8, 17.382), (8, 18.545), (8, 19)))
        self.add_line('sym-e4', (8, 19), (8, 24))
        self.add_line('sym-e5', (8, 24), (8, 29))
        self.add_bezier('sym-e6', (8, 29), ((8, 29.455), (8, 30.618), (8, 31)))
        self.add_bezier('sym-e7', (8, 31), ((8.775, 32.473), (10.585, 32), (12, 32)))
        self.add_line('sym-e8', (12, 32), (19, 32))
        self.add_bezier('sym-e9', (19, 32), ((21.029, 33.327), (23.08, 35.5), (25, 37)))
        self.add_bezier('sym-e10', (25, 37), ((26.979, 38.545), (28.962, 39.555), (31, 41)))
        self.add_bezier('sym-e11', (31, 41), ((32.625, 42.155), (33.945, 44), (36, 44)))
        self.add_bezier('sym-e12', (36, 44), ((36.152, 44), (36.848, 44), (37, 44)))
        self.add_bezier('sym-e13', (37, 44), ((37.042, 44), (36.958, 44), (37, 44)))
        self.add_bezier('sym-e14', (37, 44), ((38.061, 44), (40, 42.327), (40, 41)))
        self.add_bezier('sym-e15', (40, 41), ((40, 40.955), (40, 41.045), (40, 41)))
        self.add_line('sym-e16', (40, 41), (40, 24))
        self.add_line('sym-e17', (40, 24), (40, 7))
        self.add_bezier('sym-e18', (40, 7), ((40, 6.955), (40, 7.045), (40, 7)))
        self.add_bezier('sym-e19', (40, 7), ((40, 5.673), (38.061, 4), (37, 4)))
        self.add_bezier('sym-e20', (37, 4), ((36.958, 4), (37.042, 4), (37, 4)))
        self.add_bezier('sym-e21', (37, 4), ((36.848, 4), (36.152, 4), (36, 4)))
        self.add_bezier('sym-e22', (36, 4), ((33.945, 4), (32.625, 5.845), (31, 7)))
        self.add_bezier('sym-e23', (31, 7), ((28.962, 8.445), (26.979, 9.455), (25, 11)))
        self.add_bezier('sym-e24', (25, 11), ((23.08, 12.5), (21.029, 14.673), (19, 16)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24')
