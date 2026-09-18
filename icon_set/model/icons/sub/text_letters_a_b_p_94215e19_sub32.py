"""Independent 32px profile of text-letters-a-b-p-94215e19.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '94215e19-fc65-4b56-b956-c56498ca0382'
SOURCE_PATH = 'icon_set/dist/text32/text-letters-a-b-p-94215e19.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('94215e19-fc65-4b56-b956-c56498ca0382', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/ABP_94215e19-fc65-4b56-b956-c56498ca0382.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-letters-a-b-p-94215e19',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-b-uppercase', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = 'e4b8d290f8e2c628cdefcfd83a10c5c98293350f1118cb72c7c829d3a88bc269'

class Drawing(TextSub32):
    icon_id = 'text-letters-a-b-p-94215e19-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 79
    text_ink_bounds = (0.0, 0.0, 79.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (57, 30), (57, 2))
        self.add_line('p1-r1-2', (57, 2), (67, 2))
        self.add_bezier('p1-r1-3', (67, 2), ((74, 2), (77, 6), (77, 9)))
        self.add_bezier('p1-r1-4', (77, 9), ((77, 13), (74, 17), (67, 17)))
        self.add_line('p1-r1-5', (67, 17), (57, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (31, 30), (31, 2))
        self.add_line('p2-r1-2', (31, 2), (40, 2))
        self.add_bezier('p2-r1-3', (40, 2), ((46, 2), (49, 6), (49, 9)))
        self.add_bezier('p2-r1-4', (49, 9), ((49, 13), (46, 16), (40, 16)))
        self.add_line('p2-r1-5', (40, 16), (31, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_bezier('p3-r1-1', (40, 16), ((46, 16), (49, 20), (49, 23)))
        self.add_bezier('p3-r1-2', (49, 23), ((49, 27), (46, 30), (40, 30)))
        self.add_line('p3-r1-3', (40, 30), (31, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 30), (11, 3))
        self.add_bezier('p4-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p4-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p4-r1-4', (14, 3), (23, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (6, 18), (19, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-3')
        self.relate("connect", 'p2-r1-4', 'p3-r1-1')
        self.relate("connect", 'p2-r1-5', 'p3-r1-1')
