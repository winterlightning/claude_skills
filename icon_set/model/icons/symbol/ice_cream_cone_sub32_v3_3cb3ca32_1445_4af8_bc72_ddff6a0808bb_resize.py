"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3cb3ca32-1445-4af8-bc72-ddff6a0808bb'
SOURCE_PATH = 'icon_set/model/icons/symbol/ice_cream_cone_sub32_v3_3cb3ca32_1445_4af8_bc72_ddff6a0808bb.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '32c5db5288a9b420363dba871a15f7a2fff41a291d36c13a00bffd93769209cb'
SOURCE_REFERENCES = (('3cb3ca32-1445-4af8-bc72-ddff6a0808bb', 'pictographic-primitives/symbol/ice scream_3cb3ca32-1445-4af8-bc72-ddff6a0808bb.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'ice-cream-cone-sub32-v3-resize'
    variant_of = 'ice-cream-cone-sub32-v3'
    variant_label = 'Resize 18 × 24'
    canvas_width = 18
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('dome', (5, 6), (13, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('shoulder-right', (13, 6), ((13, 8), (16, 8), (16, 9)))
        self.add_arc('lobe-right', (16, 9), (13, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('rim', (13, 12), (5, 12))
        self.add_arc('lobe-left', (5, 12), (2, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('shoulder-left', (2, 9), ((2, 8), (5, 8), (5, 6)))
        self.add_line('cone-1', (5, 12), (9, 22))
        self.add_line('cone-2', (9, 22), (13, 12))
        self.add_contour('scoop', 'dome', 'shoulder-right', 'lobe-right', 'rim', 'lobe-left', 'shoulder-left', closed=True)
        self.add_contour('cone', 'cone-1', 'cone-2', closed=False)
        self.relate('connect', 'cone', 'scoop')
