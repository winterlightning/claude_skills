"""Building: A tall rectangular building stands beside a lower right-hand annex with a sloping roof. Two short horizontal window marks sit on the tower, and both sections share a baseline.

Construction: Tall left building retains two short horizontal window marks, right low annex and continuous ground line.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '04275826-0e0d-4236-97f8-ba6f0486843e'
SOURCE_PATH = 'pictographic-primitives/state/embassy_04275826-0e0d-4236-97f8-ba6f0486843e.svg'
AUTHOR = 'gpt-6'


class BuildingSubState114(Sub32):
    icon_id = 'building-sub-state-114'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('building', 'tall', 'rectangular', 'stands', 'beside', 'lower', 'right', 'hand')

    def build(self):
        self.add_polyline('tower',(6,30),(6,2),(22,2),(22,30))
        self.add_line('ground',(2,30),(30,30))
        self.add_polyline('annex',(22,12),(30,16),(30,30))
        for y in (12,22):self.add_line(f'window-{y}',(13,y),(15,y))
        self.relate('connect','tower','ground')
        self.relate('connect','tower','annex')
        self.relate('connect','ground','annex')
