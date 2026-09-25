"""Hamster Wheel.

Plan: Circular wheel radius 15 on an A-frame with exact circle/leg intersection nodes; wide baseline. Upper spokes and hub ring omitted.
Centerline extremes: (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '023215a4-3acc-561f-981a-83bb796d3f4c'
SOURCE_PATH = 'pictographic-primitives/pets/hamster wheel_023215a4-3acc-561f-981a-83bb796d3f4c.svg'
AUTHOR = 'gpt-6'

class HamsterWheel(Solo48):
    icon_id = 'hamster-wheel'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('hamster-wheel', 'wheel', 'hamster', 'exercise', 'rodent', 'cage', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        points=[(24,4),(39,19),(33,31),(24,34),(15,31),(9,19),(24,4)]
        parts=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
         arc(f'rim-{i}',a,b,15);parts.append(f'rim-{i}')
        contour('wheel',*parts,closed=True)
        self.add_polyline('stand-left',(24,19),(15,31),(9,39),(9,44))
        self.add_polyline('stand-right',(24,19),(33,31),(39,39),(39,44))
        self.add_polyline('base',(8,44),(9,44),(39,44),(40,44))
        self.relate('connect','stand-left','stand-right')
        for leg in ('stand-left','stand-right'):
         self.relate('connect',leg,'wheel')
         self.relate('connect',leg,'base')
