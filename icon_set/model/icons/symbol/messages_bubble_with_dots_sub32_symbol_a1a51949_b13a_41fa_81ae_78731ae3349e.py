"""Independent 32px profile of messages-bubble-with-dots.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a1a51949-b13a-41fa-81ae-78731ae3349e'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble with dots_a1a51949-b13a-41fa-81ae-78731ae3349e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a1a51949-b13a-41fa-81ae-78731ae3349e', 'pictographic-primitives/symbol/messages bubble with dots_a1a51949-b13a-41fa-81ae-78731ae3349e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/messages-bubble-with-dots',)
SOLO_SOURCE_ICON_IDS = ('messages-bubble-with-dots',)
REFERENCE_EXPORT_SHA256 = '39f8291b05f35e684ddf67feec2714d56e71bdfd75efac63617f290be00c2909'

class DrawingContainerSymbol(Sub32):
    icon_id = 'messages-bubble-with-dots-sub32-symbol'
    related_origin_icon_id = 'messages-bubble-with-dots-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/messages-bubble-with-dots-sub32'
    counterpart_icon_id = 'messages-bubble-with-dots-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (3, 27), ((4, 26), (5, 25), (6, 24)))
        self.add_bezier('p1-r1-2', (6, 24), ((6, 24), (6, 23), (6, 23)))
        self.add_bezier('p1-r1-3', (6, 23), ((6, 23), (6, 23), (6, 23)))
        self.add_bezier('p1-r1-4', (6, 23), ((6, 23), (5, 22), (4, 21)))
        self.add_bezier('p1-r1-5', (4, 21), ((3, 20), (2, 18), (2, 16)))
        self.add_bezier('p1-r1-6', (2, 16), ((2, 15), (2, 15), (2, 15)))
        self.add_bezier('p1-r1-7', (2, 15), ((2, 15), (2, 15), (2, 15)))
        self.add_bezier('p1-r1-8', (2, 15), ((2, 14), (2, 13), (3, 12)))
        self.add_bezier('p1-r1-9', (3, 12), ((5, 7), (11, 5), (15, 5)))
        self.add_bezier('p1-r1-10', (15, 5), ((15, 5), (15, 5), (16, 5)))
        self.add_bezier('p1-r1-11', (16, 5), ((16, 5), (16, 5), (17, 5)))
        self.add_bezier('p1-r1-12', (17, 5), ((21, 5), (27, 7), (29, 12)))
        self.add_bezier('p1-r1-13', (29, 12), ((30, 13), (30, 14), (30, 15)))
        self.add_bezier('p1-r1-14', (30, 15), ((30, 15), (30, 15), (30, 16)))
        self.add_bezier('p1-r1-15', (30, 16), ((30, 17), (30, 18), (29, 19)))
        self.add_bezier('p1-r1-16', (29, 19), ((26, 24), (21, 26), (16, 26)))
        self.add_bezier('p1-r1-17', (16, 26), ((16, 26), (16, 26), (15, 26)))
        self.add_bezier('p1-r1-18', (15, 26), ((14, 26), (13, 26), (12, 25)))
        self.add_bezier('p1-r1-19', (12, 25), ((11, 25), (10, 25), (10, 25)))
        self.add_bezier('p1-r1-20', (10, 25), ((10, 25), (10, 25), (10, 25)))
        self.add_bezier('p1-r1-21', (10, 25), ((10, 25), (9, 26), (8, 26)))
        self.add_bezier('p1-r1-22', (8, 26), ((7, 27), (6, 27), (4, 27)))
        self.add_bezier('p1-r1-23', (4, 27), ((4, 27), (4, 27), (4, 27)))
        self.add_bezier('p1-r1-24', (4, 27), ((3, 27), (3, 27), (3, 27)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', 'p1-r1-23', 'p1-r1-24', closed=False)
        self.add_line('p2-r1-1', (8, 15), (8, 15))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 15), (16, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (24, 15), (24, 15))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
