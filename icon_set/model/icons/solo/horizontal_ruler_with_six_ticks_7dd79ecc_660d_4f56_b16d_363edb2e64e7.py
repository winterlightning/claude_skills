"""Horizontal measuring ruler. Four evenly spaced ticks replace six for SOLO48
clearance. HRECT_M is the shallowest horizontal keyshape. Split lower edge
at tick attachment nodes. Lucide ruler supplies edge-attached tick principle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7dd79ecc-660d-4f56-b16d-363edb2e64e7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/ruler horizontal_7dd79ecc-660d-4f56-b16d-363edb2e64e7.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'horizontal-ruler-with-six-ticks'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Horizontal Measuring Ruler']
    keywords = ['ruler', 'measure', 'tick', 'stationery', 'length', 'tool']
    def build(self):
        xs = (4,12,20,28,36,44)
        self.add_line('upper-1',(4,38),(4,10))
        self.add_line('upper-2',(4,10),(44,10))
        self.add_line('upper-3',(44,10),(44,38))
        for i in range(5):
            self.add_line(f'lower-{i}',(xs[5-i],38),(xs[4-i],38))
        self.add_contour('body','upper-1','upper-2','upper-3',*[f'lower-{i}' for i in range(5)],closed=True)
        for i,x in enumerate(xs[1:-1]):
            tick=f'tick-{i}'
            self.add_line(tick,(x,38),(x,28))
            self.relate('connect',tick,f'lower-{3-i}')
            self.relate('connect',tick,f'lower-{4-i}')
