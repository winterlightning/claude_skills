"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '331d4b6a-2a43-520f-b93c-bc9a0f5e1062'
SOURCE_PATH = 'icon_set/model/icons/symbol/person_in_ski_mask_sub32_331d4b6a_2a43_520f_b93c_bc9a0f5e1062.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '39d68df6ce4c33d8958db6e6e2081253ea11e2a4c3a19a6c8eb847adcf553275'
SOURCE_REFERENCES = (('331d4b6a-2a43-520f-b93c-bc9a0f5e1062', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/tools criminal mask_331d4b6a-2a43-520f-b93c-bc9a0f5e1062.svg'), ('8a4bd6ce-492d-5b6a-a9ab-d8e814463361', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/criminal mask_8a4bd6ce-492d-5b6a-a9ab-d8e814463361.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'person-in-ski-mask-sub32-resize'
    variant_of = 'person-in-ski-mask-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/crime'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 22), (5, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (5, 19), (5, 18))
        self.add_arc('p1-r1-3', (5, 18), (2, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (2, 15), (2, 10))
        self.add_arc('p1-r1-5', (2, 10), (10, 2), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (10, 2), (18, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (18, 10), (18, 15))
        self.add_arc('p1-r1-8', (18, 15), (15, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (15, 18), (15, 19))
        self.add_arc('p1-r1-10', (15, 19), (18, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (9, 7), (11, 7))
        self.add_arc('p2-r1-2', (11, 7), (11, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (11, 11), (9, 11))
        self.add_arc('p2-r1-4', (9, 11), (9, 7), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-1', (9, 16), (11, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
