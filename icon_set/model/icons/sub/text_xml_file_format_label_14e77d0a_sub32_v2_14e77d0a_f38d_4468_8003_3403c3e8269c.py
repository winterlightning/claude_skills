"""Independent 32px profile of text-xml-file-format-label-14e77d0a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '14e77d0a-f38d-4468-8003-3403c3e8269c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/text-xml-file-format-label-14e77d0a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14e77d0a-f38d-4468-8003-3403c3e8269c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/xml (text)_14e77d0a-f38d-4468-8003-3403c3e8269c.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-xml-file-format-label-14e77d0a',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '9069c9a0be00054f0eae3c807f669f6e29eedd81e819a84d97e9dfaed5418e5e'

TYPEFACE_GLYPH_IDS = ('letter-x-uppercase', 'letter-m-uppercase', 'letter-l-uppercase')
























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class DrawingVariant2(TextSub32):
    icon_id = 'text-xml-file-format-label-14e77d0a-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (1.0, -1.9539862061712654e-06, 65.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'XML'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (3, 2.00003), (17, 17.9909))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (3.02295, 18), (16.9638, 2.04587))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (26, 18), (26, 2.4248))
        self.add_bezier('p3-r1-2', (26, 2.4248), ((26, 2.01632), (26.53474, 1.84408), (26.78474, 2.17204)))
        self.add_line('p3-r1-3', (26.78474, 2.17204), (33.65053, 11.1787))
        self.add_bezier('p3-r1-4', (33.65053, 11.1787), ((33.82456, 11.407), (34.175399999999996, 11.407), (34.3495, 11.1787)))
        self.add_line('p3-r1-5', (34.3495, 11.1787), (41.2153, 2.17204))
        self.add_bezier('p3-r1-6', (41.2153, 2.17204), ((41.4653, 1.84408), (42, 2.01632), (42, 2.4248)))
        self.add_line('p3-r1-7', (42, 2.4248), (42, 18))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
        self.add_bezier('p4-r1-1', (63, 18), ((59.9428, 18), (52.23973, 18), (52, 18)))
        self.add_line('p4-r1-2', (52, 18), (52, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
