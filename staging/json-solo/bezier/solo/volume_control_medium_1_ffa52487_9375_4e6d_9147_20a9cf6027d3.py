"""Volume control medium 1 (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffa52487-9375-4e6d-9147-20a9cf6027d3'
SOURCE_PATH = 'icons-json/audio/volume control medium 1_ffa52487-9375-4e6d-9147-20a9cf6027d3.json'
AUTHOR = 'json_to_solo'

class VolumeControlMedium1Audio(Solo48):
    icon_id = 'volume-control-medium-1-audio'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'medium', 'audio')

    def build(self):
        self.add_bezier('sym-e0', (42, 24), ((42, 23.806), (42, 23.196), (42, 23)))
        self.add_bezier('sym-e1', (42, 23), ((42, 19.245), (40.389, 15.806), (38, 13)))
        self.add_bezier('sym-e2', (36, 24), ((36, 22.37), (36.113, 20.65), (35, 19)))
        self.add_line('sym-e3', (6, 24), (6, 19))
        self.add_bezier('sym-e4', (6, 19), ((6, 18.926), (6, 19.074), (6, 19)))
        self.add_bezier('sym-e5', (6, 19), ((6, 17.904), (7.174, 17.515), (8, 17)))
        self.add_line('sym-e6', (8, 17), (16, 17))
        self.add_bezier('sym-e7', (16, 17), ((16.27, 17), (16.73, 17), (17, 17)))
        self.add_line('sym-e8', (17, 17), (26, 6))
        self.add_bezier('sym-e9', (26, 6), ((26.115, 6), (26.885, 6), (27, 6)))
        self.add_bezier('sym-e10', (27, 6), ((27.18, 6), (26.836, 6), (27, 6)))
        self.add_bezier('sym-e11', (27, 6), ((27.057, 6), (26.943, 6), (27, 6)))
        self.add_bezier('sym-e12', (27, 6), ((27.123, 6), (27.877, 6), (28, 6)))
        self.add_bezier('sym-e13', (28, 6), ((28.524, 6), (28.861, 7.632), (29, 8)))
        self.add_line('sym-e14', (29, 8), (29, 24))
        self.add_line('sym-e15', (29, 24), (29, 40))
        self.add_bezier('sym-e16', (29, 40), ((28.861, 40.368), (28.524, 42), (28, 42)))
        self.add_bezier('sym-e17', (28, 42), ((27.877, 42), (27.123, 42), (27, 42)))
        self.add_bezier('sym-e18', (27, 42), ((26.943, 42), (27.057, 42), (27, 42)))
        self.add_bezier('sym-e19', (27, 42), ((26.836, 42), (27.18, 42), (27, 42)))
        self.add_bezier('sym-e20', (27, 42), ((26.885, 42), (26.115, 42), (26, 42)))
        self.add_line('sym-e21', (26, 42), (17, 31))
        self.add_bezier('sym-e22', (17, 31), ((16.73, 31), (16.27, 31), (16, 31)))
        self.add_line('sym-e23', (16, 31), (8, 31))
        self.add_bezier('sym-e24', (8, 31), ((7.174, 30.485), (6, 30.096), (6, 29)))
        self.add_bezier('sym-e25', (6, 29), ((6, 28.926), (6, 29.074), (6, 29)))
        self.add_line('sym-e26', (6, 29), (6, 24))
        self.add_bezier('sym-e27', (42, 24), ((42, 24.194), (42, 24.804), (42, 25)))
        self.add_bezier('sym-e28', (42, 25), ((42, 28.755), (40.389, 32.194), (38, 35)))
        self.add_bezier('sym-e29', (36, 24), ((36, 25.63), (36.113, 27.35), (35, 29)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', closed=True)
        self.add_contour('sym-c3', 'sym-e27', 'sym-e28')
        self.add_contour('sym-c4', 'sym-e29')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
