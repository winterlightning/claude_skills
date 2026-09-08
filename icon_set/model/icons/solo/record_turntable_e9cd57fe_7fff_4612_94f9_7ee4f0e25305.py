"""A turntable deck carries a circular platter, a diagonal arm and one control.

Keyshape VRECT_XL: visible extremes (3, 0, 45, 48).
Lucide disc-3: circular platter and central mark; monitor: rounded housing. The source diagonal tonearm is deliberately asymmetric. Spindle ring reduced to a dot."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9cd57fe-7fff-4612-94f9-7ee4f0e25305'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/turntable 1_e9cd57fe-7fff-4612-94f9-7ee4f0e25305.svg'


class RecordTurntable(Solo48):
    icon_id = 'record-turntable'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('turntable', 'record player', 'vinyl', 'dj', 'music', 'audio', 'platter', 'deck')

    def build(self) -> None:
        self.add_line('deck-top0', (9, 2), (39, 2))
        self.add_arc('deck-ne', (39, 2), (43, 6), radius_x=4, sweep=True)
        self.add_line('deck-right', (43, 6), (43, 42))
        self.add_arc('deck-se', (43, 42), (39, 46), radius_x=4, sweep=True)
        self.add_line('deck-bottom0', (39, 46), (9, 46))
        self.add_arc('deck-sw', (9, 46), (5, 42), radius_x=4, sweep=True)
        self.add_line('deck-left', (5, 42), (5, 6))
        self.add_arc('deck-nw', (5, 6), (9, 2), radius_x=4, sweep=True)
        self.add_contour('deck', 'deck-top0', 'deck-ne', 'deck-right', 'deck-se', 'deck-bottom0', 'deck-sw', 'deck-left', 'deck-nw', closed=True)
        self.add_arc('platter0', (36, 21), (24, 33), radius_x=12, sweep=True)
        self.add_arc('platter1', (24, 33), (12, 21), radius_x=12, sweep=True)
        self.add_arc('platter2', (12, 21), (24, 9), radius_x=12, sweep=True)
        self.add_arc('platter3', (24, 9), (36, 21), radius_x=12, sweep=True)
        self.add_contour('platter', 'platter0', 'platter1', 'platter2', 'platter3', closed=True)
        self.add_dot('spindle', (24, 21))
        self.add_line('tonearm', (24, 21), (13, 32))
        self.relate("connect", 'spindle', 'tonearm')
        self.relate("connect", 'platter', 'tonearm')
        self.add_line('control', (31, 39), (35, 39))
