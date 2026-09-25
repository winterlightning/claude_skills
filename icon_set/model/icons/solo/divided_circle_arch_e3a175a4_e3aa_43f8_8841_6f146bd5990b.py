"""Divided Circle with Arch. Retains the identifying silhouette and visible features.

CIRCLE visible extremes (2, 2, 46, 46); centerlines (4, 4, 44, 44).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3a175a4-e3aa-43f8-8841-6f146bd5990b'
SOURCE_PATH = 'pictographic-primitives/symbol/divided face_e3a175a4-e3aa-43f8-8841-6f146bd5990b.svg'
AUTHOR = 'gpt-6'


class DividedCircleArch(Solo48):
    icon_id = 'divided-circle-arch'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('circle', 'divided', 'symbol', 'peace', 'face', 'split', 'emblem', 'sign')

    def build(self) -> None:
        self.add_arc('circle-right', (24, 4), (24, 44), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('circle-left', (24, 44), (24, 4), radius_x=20, radius_y=20, sweep=True)
        self.add_contour('circle', 'circle-right', 'circle-left', closed=True)
        self.add_polyline('divider', (24, 4), (24, 30), (24, 44))
        self.relate("connect", 'circle', 'divider')
        self.add_arc('arch-left', (16, 34), (24, 30), radius_x=8, radius_y=4, sweep=True)
        self.add_arc('arch-right', (24, 30), (32, 34), radius_x=8, radius_y=4, sweep=True)
        self.add_contour('arch', 'arch-left', 'arch-right')
        self.relate("connect", 'divider', 'arch')
