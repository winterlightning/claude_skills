"""Independent 32px profile of text-bold-capital-rent-word-af1e092e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'af1e092e-344d-41bf-83ad-5e5c46c9771f'
SOURCE_PATH = 'icon_set/dist/text32/text-bold-capital-rent-word-af1e092e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('af1e092e-344d-41bf-83ad-5e5c46c9771f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/rent (text)_af1e092e-344d-41bf-83ad-5e5c46c9771f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-bold-capital-rent-word-af1e092e',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-e-uppercase', 'letter-n-uppercase', 'letter-t-uppercase')
REFERENCE_EXPORT_SHA256 = 'a776338cf963f1ac32fbd09b047366a6766912726a4ee592afc28af03240f7ec'































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-bold-capital-rent-word-af1e092e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 92
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 90.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'RENT'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (10.8873, 10.2597), ((10.9927, 10.2656), (11.7461, 10.2002), (12.1943, 10.1448)))
        self.add_bezier('p1-r1-2', (12.1943, 10.1448), ((12.7739, 10.0215), (13.2364, 9.87383), (13.5786, 9.7323)))
        self.add_bezier('p1-r1-3', (13.5786, 9.7323), ((13.8168, 9.61569), (14.0581, 9.47953), (14.2933, 9.32693)))
        self.add_bezier('p1-r1-4', (14.2933, 9.32693), ((14.5206, 9.15663), (14.7316, 8.97268), (15.0066, 8.68112)))
        self.add_bezier('p1-r1-5', (15.0066, 8.68112), ((15.3006, 8.29491), (15.5148, 7.91654), (15.6705, 7.53332)))
        self.add_bezier('p1-r1-6', (15.6705, 7.53332), ((15.7876, 7.06309), (15.8622, 6.49759), (15.8754, 6.1192)))
        self.add_bezier('p1-r1-7', (15.8754, 6.1192), ((15.8688, 5.74217), (15.8129, 5.17647), (15.7555, 4.89334)))
        self.add_bezier('p1-r1-8', (15.7555, 4.89334), ((15.6735, 4.61016), (15.5144, 4.2323), (15.3444, 3.94479)))
        self.add_bezier('p1-r1-9', (15.3444, 3.94479), ((15.0433, 3.56633), (14.7559, 3.28724), (14.3151, 2.93323)))
        self.add_bezier('p1-r1-10', (14.3151, 2.93323), ((13.9612, 2.70704), (13.6152, 2.5248), (13.1474, 2.32978)))
        self.add_bezier('p1-r1-11', (13.1474, 2.32978), ((12.8004, 2.2177), (12.4606, 2.13329), (12.115, 2.07444)))
        self.add_bezier('p1-r1-12', (12.115, 2.07444), ((11.8881, 2.0514), (11.4301, 2.02658), (10.7396, 2.01318)))
        self.add_line('p1-r1-13', (10.7396, 2.01318), (8.21436, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.add_line('p2-r1-1', (4.00684, 10.2662), (10.8877, 10.2598))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16.0002, 17.9842), (10.9937, 10.2657))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (8.21543, 2), (4.32855, 2))
        self.add_bezier('p4-r1-2', (4.32855, 2), ((4.1471, 2), (4, 2.1471), (4, 2.32855)))
        self.add_line('p4-r1-3', (4, 2.32855), (4, 18))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.add_line('p5-r1-1', (40, 17.9999), (28.26183, 18))
        self.add_bezier('p5-r1-2', (28.26183, 18), ((28.11723, 18), (28, 17.8828), (28, 17.7382)))
        self.add_line('p5-r1-3', (28, 17.7382), (28, 9.98924))
        self.add_line('p5-r1-4', (28, 9.98924), (28, 2.01314))
        self.add_line('p5-r1-5', (28, 2.01314), (40, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.add_line('p6-r1-1', (36.4, 10), (28, 10))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (51, 18), (51, 2.21987))
        self.add_bezier('p7-r1-2', (51, 2.21987), ((51, 1.97187), (51.77876, 1.91394), (51.95982, 2.14847)))
        self.add_line('p7-r1-3', (51.95982, 2.14847), (64.0402, 17.7968))
        self.add_bezier('p7-r1-4', (64.0402, 17.7968), ((64.2212, 18.0313), (65, 17.9734), (65, 17.7254)))
        self.add_line('p7-r1-5', (65, 17.7254), (65, 2.02527))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', 'p7-r1-4', 'p7-r1-5', closed=False)
        self.add_line('p8-r1-1', (76, 2), (88, 2))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (82, 18), (82.0064, 2))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-1-1', 'path-3-1')
        self.relate("connect", 'path-1-1', 'path-4-1')
        self.relate("connect", 'path-2-1', 'path-3-1')
        self.relate("connect", 'path-2-1', 'path-4-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
        self.relate("connect", 'path-5-1', 'path-6-1')
        self.relate("connect", 'path-8-1', 'path-9-1')
