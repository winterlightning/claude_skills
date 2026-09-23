"""Independent 32px profile of text-number-twenty-four-e3ef1255.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'e3ef1255-7230-466e-a0e3-b1897407d9eb'
SOURCE_PATH = 'icon_set/dist/text32/text-number-twenty-four-e3ef1255.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3ef1255-7230-466e-a0e3-b1897407d9eb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/24 (text)_e3ef1255-7230-466e-a0e3-b1897407d9eb.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-twenty-four-e3ef1255',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-2', 'digit-4')
REFERENCE_EXPORT_SHA256 = '4ea08e000af44f9e276dfa903baed513fc578a6cdc3084dcaef0498f42edb88f'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-number-twenty-four-e3ef1255-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 42.0, 20.0001)

    def build(self):
        """Source-native uppercase composition for '24'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (4.55109, 6.1626), ((4.55109, 6.1626), (3.96613, 2), (9.98841, 2)))
        self.add_bezier('p1-r1-2', (9.98841, 2), ((16.0107, 2), (16.3103, 7.1822), (13.6, 8.85714)))
        self.add_line('p1-r1-3', (13.6, 8.85714), (5.8, 14))
        self.add_bezier('p1-r1-4', (5.8, 14), ((4.43905, 14.8411), (4, 16), (4, 16.9646)))
        self.add_line('p1-r1-5', (4, 16.9646), (4, 17.2495))
        self.add_bezier('p1-r1-6', (4, 17.2495), ((4, 17.664), (4.37623, 18), (4.84034, 18)))
        self.add_line('p1-r1-7', (4.84034, 18), (16, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (40, 12.8572), (28.40861, 12.8572))
        self.add_bezier('p2-r1-2', (28.40861, 12.8572), ((28.18045, 12.8572), (27.81423, 12.5715), (28.11142, 12.2858)))
        self.add_line('p2-r1-3', (28.11142, 12.2858), (37.622299999999996, 2.00009))
        self.add_line('p2-r1-4', (37.622299999999996, 2.00009), (37.622299999999996, 18.0001))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
