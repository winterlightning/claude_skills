"""Meta quest (technology), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9210afd9-195d-52c8-ae01-b8d2485089f3'
SOURCE_PATH = 'icons-json/technology/meta quest_9210afd9-195d-52c8-ae01-b8d2485089f3.json'
AUTHOR = 'json_to_solo'

class MetaQuestTechnology(Solo48):
    icon_id = 'meta-quest-technology'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('meta', 'quest', 'technology')

    def build(self):
        self.add_bezier('sym-e0', (39, 19), ((38.5, 17.486), (38.727, 15.354), (38, 14)))
        self.add_bezier('sym-e1', (38, 14), ((36.045, 10.295), (32.436, 8), (29, 8)))
        self.add_bezier('sym-e2', (29, 8), ((28.836, 8), (29.164, 8), (29, 8)))
        self.add_line('sym-e3', (29, 8), (24, 8))
        self.add_line('sym-e4', (24, 8), (19, 8))
        self.add_bezier('sym-e5', (19, 8), ((18.836, 8), (19.164, 8), (19, 8)))
        self.add_bezier('sym-e6', (19, 8), ((15.564, 8), (11.955, 10.295), (10, 14)))
        self.add_bezier('sym-e7', (10, 14), ((9.273, 15.354), (9.5, 17.486), (9, 19)))
        self.add_bezier('sym-e8', (9, 19), ((6.964, 19.086), (4, 20.677), (4, 24)))
        self.add_bezier('sym-e9', (4, 24), ((4, 24.098), (4, 23.902), (4, 24)))
        self.add_line('sym-e10', (4, 24), (4, 33))
        self.add_bezier('sym-e11', (4, 33), ((4, 33.677), (4, 34.323), (4, 35)))
        self.add_bezier('sym-e12', (4, 35), ((4, 37.523), (6.182, 40), (8, 40)))
        self.add_bezier('sym-e13', (8, 40), ((8.145, 40), (8.855, 40), (9, 40)))
        self.add_line('sym-e14', (9, 40), (17, 40))
        self.add_bezier('sym-e15', (17, 40), ((17.518, 39.778), (17.518, 39.369), (18, 39)))
        self.add_bezier('sym-e16', (18, 39), ((18.964, 38.274), (20.045, 36.738), (21, 36)))
        self.add_bezier('sym-e17', (21, 36), ((21.689, 35.475), (22.766, 35.043), (24, 35)))
        self.add_bezier('sym-e18', (24, 35), ((25.234, 35.043), (26.311, 35.475), (27, 36)))
        self.add_bezier('sym-e19', (27, 36), ((27.955, 36.738), (29.036, 38.274), (30, 39)))
        self.add_bezier('sym-e20', (30, 39), ((30.482, 39.369), (30.482, 39.778), (31, 40)))
        self.add_line('sym-e21', (31, 40), (39, 40))
        self.add_bezier('sym-e22', (39, 40), ((39.145, 40), (39.855, 40), (40, 40)))
        self.add_bezier('sym-e23', (40, 40), ((41.818, 40), (44, 37.523), (44, 35)))
        self.add_bezier('sym-e24', (44, 35), ((44, 34.323), (44, 33.677), (44, 33)))
        self.add_line('sym-e25', (44, 33), (44, 24))
        self.add_bezier('sym-e26', (44, 24), ((44, 23.902), (44, 24.098), (44, 24)))
        self.add_bezier('sym-e27', (44, 24), ((44, 20.677), (41.036, 19.086), (39, 19)))
        self.add_bezier('sym-e28', (39, 19), ((37.782, 18.951), (37.209, 19), (36, 19)))
        self.add_line('sym-e29', (36, 19), (24, 19))
        self.add_line('sym-e30', (24, 19), (12, 19))
        self.add_bezier('sym-e31', (12, 19), ((10.791, 19), (10.218, 18.951), (9, 19)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31')
