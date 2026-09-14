"""Volume control medium (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '341717b2-8a95-48bf-83d5-4321e85be4b7'
SOURCE_PATH = 'icons-json/audio/volume control medium_341717b2-8a95-48bf-83d5-4321e85be4b7.json'
AUTHOR = 'json_to_solo'

class VolumeControlMediumAudio(Solo48):
    icon_id = 'volume-control-medium-audio'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'medium', 'audio')

    def build(self):
        self.add_line('sym-e0', (14, 31), (14, 17))
        self.add_line('sym-e1', (14, 17), (7, 17))
        self.add_bezier('sym-e2', (7, 17), ((5.536, 17), (4, 18.29), (4, 20)))
        self.add_bezier('sym-e3', (4, 20), ((4, 20.05), (4, 19.95), (4, 20)))
        self.add_line('sym-e4', (4, 20), (4, 24))
        self.add_line('sym-e5', (4, 24), (4, 28))
        self.add_bezier('sym-e6', (4, 28), ((4, 28.05), (4, 27.95), (4, 28)))
        self.add_bezier('sym-e7', (4, 28), ((4, 29.71), (5.536, 31), (7, 31)))
        self.add_line('sym-e8', (7, 31), (14, 31))
        self.add_line('sym-e9', (14, 31), (28, 40))
        self.add_bezier('sym-e10', (28, 40), ((28.227, 40), (27.773, 40), (28, 40)))
        self.add_bezier('sym-e11', (28, 40), ((28.064, 40), (27.936, 40), (28, 40)))
        self.add_bezier('sym-e12', (28, 40), ((28.036, 40), (28.973, 40), (29, 40)))
        self.add_bezier('sym-e13', (29, 40), ((29.082, 40), (28.927, 40), (29, 40)))
        self.add_bezier('sym-e14', (29, 40), ((29.845, 40), (29.755, 38.65), (30, 38)))
        self.add_line('sym-e15', (30, 38), (30, 24))
        self.add_line('sym-e16', (30, 24), (30, 10))
        self.add_bezier('sym-e17', (30, 10), ((29.755, 9.35), (29.845, 8), (29, 8)))
        self.add_bezier('sym-e18', (29, 8), ((28.927, 8), (29.082, 8), (29, 8)))
        self.add_bezier('sym-e19', (29, 8), ((28.973, 8), (28.036, 8), (28, 8)))
        self.add_bezier('sym-e20', (28, 8), ((27.936, 8), (28.064, 8), (28, 8)))
        self.add_bezier('sym-e21', (28, 8), ((27.773, 8), (28.227, 8), (28, 8)))
        self.add_line('sym-e22', (28, 8), (14, 17))
        self.add_bezier('sym-e23', (39, 35), ((41.918, 32.41), (44, 28.33), (44, 24)))
        self.add_bezier('sym-e24', (44, 24), ((44, 23.887), (44, 24.113), (44, 24)))
        self.add_bezier('sym-e25', (44, 24), ((44, 23.887), (44, 24.113), (44, 24)))
        self.add_bezier('sym-e26', (44, 24), ((44, 19.67), (41.918, 15.59), (39, 13)))
        self.add_bezier('sym-e27', (38, 24), ((37.85, 26.083), (37.594, 28.154), (36, 30)))
        self.add_bezier('sym-e28', (38, 24), ((37.85, 21.917), (37.594, 19.846), (36, 18)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22')
        self.add_contour('sym-c1', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
        self.add_contour('sym-c2', 'sym-e27')
        self.add_contour('sym-c3', 'sym-e28')
        self.relate('connect', 'sym-c2', 'sym-c3')
