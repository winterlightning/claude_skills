"""Independent 32px profile of text-number-sixty-six-71e1e7d3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '71e1e7d3-b065-4190-ab06-ebf4e384b98d'
SOURCE_PATH = 'icon_set/dist/text32/text-number-sixty-six-71e1e7d3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('71e1e7d3-b065-4190-ab06-ebf4e384b98d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/66 (text)_71e1e7d3-b065-4190-ab06-ebf4e384b98d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-sixty-six-71e1e7d3',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-6', 'digit-6')
REFERENCE_EXPORT_SHA256 = '17a81fdcafb761d3e698e0e88a44b4d0421813ec56f8a84d5b0c253f2cdd4446'

class Drawing(TextSub32):
    icon_id = 'text-number-sixty-six-71e1e7d3-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 51
    text_ink_bounds = (0.0, 0.0, 51.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (29, 22), (49, 22), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_arc('p1-r1-2', (49, 22), (29, 22), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (29, 22), (29, 12))
        self.add_bezier('p2-r1-2', (29, 12), ((29, 6), (34, 2), (39, 2)))
        self.add_line('p2-r1-3', (39, 2), (46, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (2, 22), (22, 22), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_arc('p3-r1-2', (22, 22), (2, 22), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 22), (2, 12))
        self.add_bezier('p4-r1-2', (2, 12), ((2, 6), (6, 2), (12, 2)))
        self.add_line('p4-r1-3', (12, 2), (19, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
