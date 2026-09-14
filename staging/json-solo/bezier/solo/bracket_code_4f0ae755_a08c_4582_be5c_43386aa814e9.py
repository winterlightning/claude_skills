"""Bracket code (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f0ae755-a08c-4582-be5c-43386aa814e9'
SOURCE_PATH = 'icons-json/symbol/bracket code_4f0ae755-a08c-4582-be5c-43386aa814e9.json'
AUTHOR = 'json_to_solo'

class BracketCodeSymbol(Solo48):
    icon_id = 'bracket-code-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bracket', 'code', 'symbol')

    def build(self):
        self.add_bezier('sym-e0', (4, 24), ((4.686, 24.514), (5.313, 25.486), (6, 26)))
        self.add_bezier('sym-e1', (6, 26), ((6.9, 26.691), (7.518, 27.023), (8, 28)))
        self.add_bezier('sym-e2', (8, 28), ((8.653, 29.332), (9, 30.513), (9, 32)))
        self.add_bezier('sym-e3', (9, 32), ((9, 34.78), (8.624, 37.535), (12, 39)))
        self.add_bezier('sym-e4', (12, 39), ((12.855, 39.371), (14.082, 39.857), (15, 40)))
        self.add_bezier('sym-e5', (44, 24), ((43.314, 24.514), (42.687, 25.486), (42, 26)))
        self.add_bezier('sym-e6', (42, 26), ((41.1, 26.691), (40.482, 27.023), (40, 28)))
        self.add_bezier('sym-e7', (40, 28), ((39.347, 29.332), (39, 30.513), (39, 32)))
        self.add_bezier('sym-e8', (39, 32), ((39, 34.78), (39.376, 37.535), (36, 39)))
        self.add_bezier('sym-e9', (36, 39), ((35.145, 39.371), (33.918, 39.857), (33, 40)))
        self.add_bezier('sym-e10', (4, 24), ((4.686, 23.486), (5.313, 22.514), (6, 22)))
        self.add_bezier('sym-e11', (6, 22), ((6.9, 21.309), (7.518, 20.977), (8, 20)))
        self.add_bezier('sym-e12', (8, 20), ((8.653, 18.668), (9, 17.487), (9, 16)))
        self.add_bezier('sym-e13', (9, 16), ((9, 13.22), (8.624, 10.465), (12, 9)))
        self.add_bezier('sym-e14', (12, 9), ((12.855, 8.629), (14.082, 8.143), (15, 8)))
        self.add_bezier('sym-e15', (44, 24), ((43.314, 23.486), (42.687, 22.514), (42, 22)))
        self.add_bezier('sym-e16', (42, 22), ((41.1, 21.309), (40.482, 20.977), (40, 20)))
        self.add_bezier('sym-e17', (40, 20), ((39.347, 18.668), (39, 17.487), (39, 16)))
        self.add_bezier('sym-e18', (39, 16), ((39, 13.22), (39.376, 10.465), (36, 9)))
        self.add_bezier('sym-e19', (36, 9), ((35.145, 8.629), (33.918, 8.143), (33, 8)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c3', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
