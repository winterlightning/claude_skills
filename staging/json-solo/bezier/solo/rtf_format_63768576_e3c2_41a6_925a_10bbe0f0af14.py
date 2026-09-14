"""Rtf format (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63768576-e3c2-41a6-925a-10bbe0f0af14'
SOURCE_PATH = 'icons-json/state/rtf format_63768576-e3c2-41a6-925a-10bbe0f0af14.json'
AUTHOR = 'json_to_solo'

class RtfFormatState(Solo48):
    icon_id = 'rtf-format-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('rtf', 'format', 'state')

    def build(self):
        self.add_line('e0', (40, 13), (39, 11))
        self.add_line('e1', (39, 11), (33, 6))
        self.add_line('e2', (33, 6), (32, 4))
        self.add_line('e3', (32, 4), (12, 4))
        self.add_line('e4', (8, 9), (8, 39))
        self.add_line('e5', (11, 44), (36, 44))
        self.add_line('e6', (40, 39), (40, 13))
        self.add_line('e7', (18, 24), (30, 24))
        self.add_line('e8', (28, 34), (20, 34))
        self.add_line('e9', (18, 32), (18, 16))
        self.add_line('e10', (20, 14), (28, 14))
        self.add_line('e11', (30, 16), (30, 32))
        self.add_bezier('e12', (12, 4), ((11.613, 4), (11.427, 4.009), (11.04, 4.009)), ((9.272, 4.009), (8.008, 5.845), (8.008, 7.618)), ((8.008, 8.018), (8, 8.418), (8, 8.818)), ((8, 9.036), (8, 8.791), (8, 9)))
        self.add_bezier('e13', (8, 39), ((8, 39.718), (8.017, 39.973), (8.017, 40.691)), ((8.017, 42.309), (9.44, 43.991), (10.973, 43.991)), ((11.032, 44), (11.099, 44), (11.166, 44)), ((11.234, 44), (10.933, 44), (11, 44)))
        self.add_bezier('e14', (36, 44), ((36.337, 44), (36.463, 43.982), (36.8, 43.982)), ((38.307, 43.982), (39.983, 42.391), (39.983, 40.7)), ((39.992, 40.627), (39.992, 40.564), (40, 40.5)), ((40, 39.845), (40, 39.655), (40, 39)))
        self.add_bezier('e15', (20, 34), ((19.082, 34), (18, 32.982), (18, 32)))
        self.add_bezier('e16', (18, 16), ((18, 15.018), (19.082, 14), (20, 14)))
        self.add_bezier('e17', (28, 14), ((28.918, 14), (30, 15.018), (30, 16)))
        self.add_bezier('e18', (30, 32), ((30, 32.982), (28.918, 34), (28, 34)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e12', 'e4', 'e13', 'e5', 'e14', 'e6')
        self.add_contour('c1', 'e7')
        self.add_contour('c2', 'e8', 'e15', 'e9', 'e16', 'e10', 'e17', 'e11', 'e18', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
