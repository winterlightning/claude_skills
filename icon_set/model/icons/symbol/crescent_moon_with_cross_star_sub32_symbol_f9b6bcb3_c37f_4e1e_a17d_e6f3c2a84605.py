"""Independent 32px profile of crescent-moon-with-cross-star.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f9b6bcb3-c37f-4e1e-a17d-e6f3c2a84605'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/night_f9b6bcb3-c37f-4e1e-a17d-e6f3c2a84605.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f9b6bcb3-c37f-4e1e-a17d-e6f3c2a84605', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/night_f9b6bcb3-c37f-4e1e-a17d-e6f3c2a84605.svg'),)
PROFILE_SOURCE_KEYS = ('solo/crescent-moon-with-cross-star',)
SOLO_SOURCE_ICON_IDS = ('crescent-moon-with-cross-star',)
REFERENCE_EXPORT_SHA256 = '9e071a74a949ed1b886f23953763911d68a1462af5742b15fbfbd8fc8d59abe6'

class DrawingContainerSymbol(Sub32):
    icon_id = 'crescent-moon-with-cross-star-sub32-symbol'
    related_origin_icon_id = 'crescent-moon-with-cross-star-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/crescent-moon-with-cross-star-sub32'
    counterpart_icon_id = 'crescent-moon-with-cross-star-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (18, 2), ((8, 2), (2, 8), (2, 18)))
        self.add_bezier('p1-r1-2', (2, 18), ((2, 25), (8, 30), (16, 30)))
        self.add_bezier('p1-r1-3', (16, 30), ((22, 30), (27, 27), (30, 21)))
        self.add_bezier('p1-r1-4', (30, 21), ((29, 21), (27, 21), (26, 21)))
        self.add_bezier('p1-r1-5', (26, 21), ((20, 21), (15, 17), (15, 10)))
        self.add_bezier('p1-r1-6', (15, 10), ((15, 8), (16, 5), (18, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (23, 8), (27, 8))
        self.add_line('p2-r1-2', (27, 8), (30, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (27, 5), (27, 8))
        self.add_line('p3-r1-2', (27, 8), (27, 11))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
