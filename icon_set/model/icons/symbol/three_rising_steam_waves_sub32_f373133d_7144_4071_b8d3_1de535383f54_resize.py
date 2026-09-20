"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'f373133d-7144-4071-b8d3-1de535383f54'
SOURCE_PATH = 'icon_set/model/icons/symbol/three_rising_steam_waves_sub32_f373133d_7144_4071_b8d3_1de535383f54.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '495b93bf252757767af1d097c7311ce975ba64e6775b9c99b17c4030023d8dc9'
SOURCE_REFERENCES = (('f373133d-7144-4071-b8d3-1de535383f54', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/heat waves_f373133d-7144-4071-b8d3-1de535383f54.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'three-rising-steam-waves-sub32-resize'
    variant_of = 'three-rising-steam-waves-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (6, 2), ((4, 4), (3, 6), (3, 8)))
        self.add_bezier('p1-r1-2', (3, 8), ((3, 11), (5, 13), (5, 16)))
        self.add_bezier('p1-r1-3', (5, 16), ((5, 18), (4, 20), (2, 22)))
        self.add_bezier('p2-r1-1', (14, 2), ((12, 4), (11, 6), (11, 8)))
        self.add_bezier('p2-r1-2', (11, 8), ((11, 11), (13, 13), (13, 16)))
        self.add_bezier('p2-r1-3', (13, 16), ((13, 18), (12, 20), (10, 22)))
        self.add_bezier('p3-r1-1', (22, 2), ((20, 4), (19, 6), (19, 8)))
        self.add_bezier('p3-r1-2', (19, 8), ((19, 11), (21, 13), (21, 16)))
        self.add_bezier('p3-r1-3', (21, 16), ((21, 18), (20, 20), (18, 22)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
