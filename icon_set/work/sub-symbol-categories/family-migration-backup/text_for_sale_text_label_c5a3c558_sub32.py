"""Independent 32px profile of text-for-sale-text-label-c5a3c558.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'c5a3c558-10c8-4455-bdbc-45e3f9bead4b'
SOURCE_PATH = 'icon_set/dist/text32/text-for-sale-text-label-c5a3c558.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c5a3c558-10c8-4455-bdbc-45e3f9bead4b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/for sale (text)_c5a3c558-10c8-4455-bdbc-45e3f9bead4b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-for-sale-text-label-c5a3c558',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase', 'letter-o-uppercase', 'letter-r-uppercase', 'letter-s-uppercase', 'letter-a-uppercase', 'letter-l-uppercase', 'letter-e-uppercase')
REFERENCE_EXPORT_SHA256 = 'ee0b19fd64150403ae31c37c2503b5cebafd4d7cf732d5239206396eff609c9f'

class Drawing(TextSub32):
    icon_id = 'text-for-sale-text-label-c5a3c558-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 208
    text_ink_bounds = (0.0, 0.0, 208.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (206, 2), (189, 2))
        self.add_line('p1-r1-2', (189, 2), (189, 30))
        self.add_line('p1-r1-3', (189, 30), (206, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (189, 16), (203, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (162, 2), (162, 30))
        self.add_line('p3-r1-2', (162, 30), (178, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (130, 30), (140, 3))
        self.add_bezier('p4-r1-2', (140, 3), ((140, 2.3333333333333335), (140.33333333333334, 2), (141, 2)))
        self.add_bezier('p4-r1-3', (141, 2), ((141, 2), (141.33333333333334, 2.3333333333333335), (142, 3)))
        self.add_line('p4-r1-4', (142, 3), (151, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (135, 18), (147, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_bezier('p6-r1-1', (119, 6), ((118, 3), (115, 2), (111, 2)))
        self.add_bezier('p6-r1-2', (111, 2), ((107, 2), (103, 4), (102, 9)))
        self.add_bezier('p6-r1-3', (102, 9), ((102, 9), (102, 9), (102, 10)))
        self.add_bezier('p6-r1-4', (102, 10), ((102, 17), (119, 13), (120, 22)))
        self.add_bezier('p6-r1-5', (120, 22), ((120, 22), (120, 22), (120, 23)))
        self.add_bezier('p6-r1-6', (120, 23), ((120, 28), (115, 30), (111, 30)))
        self.add_bezier('p6-r1-7', (111, 30), ((107, 30), (103, 29), (102, 26)))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', 'p6-r1-6', 'p6-r1-7', closed=False)
        self.add_line('p7-r1-1', (60, 30), (60, 2))
        self.add_line('p7-r1-2', (60, 2), (70, 2))
        self.add_bezier('p7-r1-3', (70, 2), ((77, 2), (80, 6), (80, 9)))
        self.add_bezier('p7-r1-4', (80, 9), ((80, 13), (77, 17), (70, 17)))
        self.add_line('p7-r1-5', (70, 17), (60, 17))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', 'p7-r1-4', 'p7-r1-5', closed=False)
        self.add_line('p8-r1-1', (70, 17), (80, 30))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_bezier('p9-r1-1', (30, 16), ((30, 8), (34, 2), (40, 2)))
        self.add_bezier('p9-r1-2', (40, 2), ((45, 2), (50, 8), (50, 16)))
        self.add_bezier('p9-r1-3', (50, 16), ((50, 24), (45, 30), (40, 30)))
        self.add_bezier('p9-r1-4', (40, 30), ((34, 30), (30, 24), (30, 16)))
        self.add_contour('path-9-1', 'p9-r1-1', 'p9-r1-2', 'p9-r1-3', 'p9-r1-4', closed=False)
        self.add_line('p10-r1-1', (19, 2), (2, 2))
        self.add_line('p10-r1-2', (2, 2), (2, 30))
        self.add_contour('path-10-1', 'p10-r1-1', 'p10-r1-2', closed=False)
        self.add_line('p11-r1-1', (2, 16), (16, 16))
        self.add_contour('path-11-1', 'p11-r1-1', closed=False)
        self.relate("connect", 'p7-r1-4', 'p8-r1-1')
        self.relate("connect", 'p7-r1-5', 'p8-r1-1')
