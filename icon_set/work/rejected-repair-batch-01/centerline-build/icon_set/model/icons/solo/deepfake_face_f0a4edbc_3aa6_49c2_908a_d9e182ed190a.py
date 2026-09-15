"""Deepfake Face. Preserves the divided upper face and smile with broad open quadrants.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0a4edbc-3aa6-49c2-908a-d9e182ed190a'
SOURCE_PATH = 'pictographic-primitives/symbol/deep fake_f0a4edbc-3aa6-49c2-908a-d9e182ed190a.svg'
AUTHOR = 'gpt-6'


class DeepfakeFace(Solo48):
    icon_id = 'deepfake-face'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('deepfake', 'face', 'ai', 'fake', 'identity', 'synthetic', 'mask', 'recognition')

    def build(self) -> None:
        self.add_line('top', (18, 4), (24, 4))
        self.add_line('top-right', (24, 4), (30, 4))
        self.add_arc('ne', (30, 4), (40, 14), radius_x=10, radius_y=10, sweep=True)
        self.add_line('right-1', (40, 14), (40, 20))
        self.add_line('right-2', (40, 20), (40, 28))
        self.add_arc('chin-right', (40, 28), (24, 44), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('chin-left', (24, 44), (8, 28), radius_x=16, radius_y=16, sweep=True)
        self.add_line('left-1', (8, 28), (8, 20))
        self.add_line('left-2', (8, 20), (8, 14))
        self.add_arc('nw', (8, 14), (18, 4), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('face', 'top', 'top-right', 'ne', 'right-1', 'right-2', 'chin-right', 'chin-left', 'left-1', 'left-2', 'nw', closed=True)
        self.add_polyline('crossbar', (8, 20), (24, 20), (40, 20))
        self.add_polyline('divider', (24, 4), (24, 20), (24, 26))
        self.relate("connect", 'face', 'crossbar')
        self.relate("connect", 'face', 'divider')
        self.relate("connect", 'crossbar', 'divider')
        self.add_arc('smile', (30, 32), (18, 32), radius_x=6, radius_y=3, sweep=True)
