"""Independent 32px profile of three-left-aligned-text-lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b84c42e8-662b-41fd-bb1e-bb264e55ee35'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/three lines_b84c42e8-662b-41fd-bb1e-bb264e55ee35.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b84c42e8-662b-41fd-bb1e-bb264e55ee35', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/three lines_b84c42e8-662b-41fd-bb1e-bb264e55ee35.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-left-aligned-text-lines',)
SOLO_SOURCE_ICON_IDS = ('three-left-aligned-text-lines',)
REFERENCE_EXPORT_SHA256 = 'a32e3d57b7b2b0d6664541bae3ee86e82daae4b865304bb80ec38ae9f2ddf730'

class DrawingContainerSymbol(Sub32):
    icon_id = 'three-left-aligned-text-lines-sub32-symbol'
    related_origin_icon_id = 'three-left-aligned-text-lines-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/three-left-aligned-text-lines-sub32'
    counterpart_icon_id = 'three-left-aligned-text-lines-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (30, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 16), (22, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 27), (30, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
