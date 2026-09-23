"""Independent 32px profile of text-uppercase-letters-rb-928601b1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '928601b1-cc6f-4c81-b977-ad0ce69dd337'
SOURCE_PATH = 'icon_set/dist/text32/text-uppercase-letters-rb-928601b1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('928601b1-cc6f-4c81-b977-ad0ce69dd337', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/rb (text)_928601b1-cc6f-4c81-b977-ad0ce69dd337.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-uppercase-letters-rb-928601b1',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-b-uppercase')
REFERENCE_EXPORT_SHA256 = 'bfdfcc93900607f5f78706c9664db1b4a12c987e757377af6e6ed60a5e9854d7'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-uppercase-letters-rb-928601b1-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 42.0, 20.000000000000007)

    def build(self):
        """Source-native uppercase composition for 'RB'; 4-unit letter spacing."""
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
        self.add_line('p5-r1-1', (28, 2), (34.1362, 2))
        self.add_bezier('p5-r1-2', (34.1362, 2), ((36.3453, 2), (38.1362, 3.79086), (38.1362, 6)))
        self.add_bezier('p5-r1-3', (38.1362, 6), ((38.1362, 8.20914), (36.3453, 10), (34.1362, 10)))
        self.add_line('p5-r1-4', (34.1362, 10), (28, 10))
        self.add_line('p5-r1-5', (28, 10), (28, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.add_line('p6-r1-1', (28, 10.0101), (36.005, 10.0101))
        self.add_bezier('p6-r1-2', (36.005, 10.0101), ((38.2114, 10.0101), (40, 11.7987), (40, 14.005)))
        self.add_bezier('p6-r1-3', (40, 14.005), ((40, 16.2114), (38.2114, 18), (36.005, 18)))
        self.add_line('p6-r1-4', (36.005, 18), (28, 18))
        self.add_line('p6-r1-5', (28, 18), (28, 10.0101))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-1-1', 'path-3-1')
        self.relate("connect", 'path-1-1', 'path-4-1')
        self.relate("connect", 'path-2-1', 'path-3-1')
        self.relate("connect", 'path-2-1', 'path-4-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
        self.relate("connect", 'path-5-1', 'path-6-1')
