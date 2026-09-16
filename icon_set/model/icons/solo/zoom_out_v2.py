# Variant of zoom-out; parent file remains unchanged.
"""Zoom out with a circular lens and one uninterrupted handle stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd05e7aa2-4c1e-43d5-8943-5f63cebcd390'
SOURCE_PATH = 'pictographic-primitives/interface-essential/zoom out_d05e7aa2-4c1e-43d5-8943-5f63cebcd390.svg'
AUTHOR = 'gpt-6'

class ZoomOutVariant2(Solo48):
    icon_id = 'zoom-out-v2'
    variant_of = 'zoom-out'
    variant_label = 'Straight handle stroke'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zoom', 'out', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: circular lens, centered minus, and one straight handle.
        # Lucide zoom-out informs the simple circle/line construction.
        # SQUARE centerline extremes: (6, 6)-(42, 42).
        center = 21
        radius = 15
        left = (center - radius, center)
        right = (center + radius, center)
        # The 9-12-15 triangle gives an exact integer point on the lens.
        attachment = (center + 12, center + 9)
        self.add_arc('lens-top', left, right,
                     radius_x=radius, radius_y=radius, sweep=True)
        self.add_arc('lens-join', right, attachment,
                     radius_x=radius, radius_y=radius, sweep=True)
        self.add_arc('lens-bottom', attachment, left,
                     radius_x=radius, radius_y=radius, sweep=True)
        self.add_contour('lens', 'lens-top', 'lens-join', 'lens-bottom', closed=True)
        self.add_line('minus', (center - 6, center), (center + 6, center))
        self.add_line('handle', attachment, (42, 42))
        self.relate('connect', 'lens', 'handle')
