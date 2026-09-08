"""Mirrored upright ears, rounded face and splayed haunches. Lucide rabbit informs capsule ears and simple haunch arcs. Leg seams omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c76e3bee-26aa-4b66-9845-18e5b5d46930'
SOURCE_PATH = 'pictographic-primitives/animals/rabbit body_c76e3bee-26aa-4b66-9845-18e5b5d46930.svg'
AUTHOR = 'gpt-6'


class SittingRabbit(Solo48):
    icon_id = 'sitting-rabbit'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ('sitting-bunny',)
    keywords = ('rabbit', 'bunny', 'sitting', 'ears', 'hare', 'animal', 'pet', 'easter')

    def build(self) -> None:
        self.add_arc('outline-1', (14, 19), (12, 26), radius_x=8, radius_y=9, sweep=False)
        self.add_line('outline-2', (12, 26), (16, 31))
        self.add_line('outline-3', (16, 31), (11, 36))
        self.add_arc('outline-4', (11, 36), (8, 41), radius_x=6, radius_y=7, sweep=False)
        self.add_arc('outline-5', (8, 41), (13, 46), radius_x=5, radius_y=5, sweep=False)
        self.add_line('outline-6', (13, 46), (35, 46))
        self.add_arc('outline-7', (35, 46), (40, 41), radius_x=5, radius_y=5, sweep=False)
        self.add_arc('outline-8', (40, 41), (37, 36), radius_x=6, radius_y=7, sweep=False)
        self.add_line('outline-9', (37, 36), (32, 31))
        self.add_line('outline-10', (32, 31), (36, 26))
        self.add_arc('outline-11', (36, 26), (34, 19), radius_x=8, radius_y=9, sweep=False)
        self.add_arc('outline-12', (34, 19), (24, 13), radius_x=11, radius_y=8, sweep=False)
        self.add_arc('outline-13', (24, 13), (14, 19), radius_x=11, radius_y=8, sweep=False)
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', 'outline-10', 'outline-11', 'outline-12', 'outline-13', closed=True)
        self.add_line('ear-left-1', (14, 19), (14, 5))
        self.add_arc('ear-left-2', (14, 5), (20, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_line('ear-left-3', (20, 5), (20, 13))
        self.add_contour('ear-left', 'ear-left-1', 'ear-left-2', 'ear-left-3', closed=False)
        self.add_line('ear-right-1', (28, 13), (28, 5))
        self.add_arc('ear-right-2', (28, 5), (34, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_line('ear-right-3', (34, 5), (34, 19))
        self.add_contour('ear-right', 'ear-right-1', 'ear-right-2', 'ear-right-3', closed=False)
        self.add_dot('eye-left', (20, 23))
        self.add_dot('eye-right', (28, 23))
        self.relate("connect", 'outline', 'ear-left')
        self.relate("connect", 'outline', 'ear-right')
