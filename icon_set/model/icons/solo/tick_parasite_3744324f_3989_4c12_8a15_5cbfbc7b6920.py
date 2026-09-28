"""Tick.

Plan: Top-view tick with a large body, small head and four mirrored leg pairs attached at explicit body nodes.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3744324f-3989-4c12-8a15-5cbfbc7b6920'
SOURCE_PATH = 'pictographic-primitives/pets/pets tick_3744324f-3989-4c12-8a15-5cbfbc7b6920.svg'
AUTHOR = 'gpt-6'

class TickParasite(Solo48):
    icon_id = 'tick-parasite'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('tick', 'parasite', 'flea', 'insect', 'pest', 'pet-health', 'bug')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        arc('head',(20,10),(28,10),4)
        line('neck-right',(28,10),(30,18))
        points=[(30,18),(34,26),(30,34),(24,36),(18,34),(14,26),(18,18)]
        for i,(a,b) in enumerate(zip(points,points[1:])):arc(f'body-{i}',a,b,10)
        line('neck-left',(18,18),(20,10))
        contour('body','head','neck-right',*(f'body-{i}' for i in range(6)),'neck-left',closed=True)
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         for i,pts in enumerate(((p(6,18),p(14,12),p(14,6)),(p(10,26),p(18,22)),(p(6,34),p(18,34)),((24,36),p(10,42)))):
          name=f'leg-{side}-{i}';self.add_polyline(name,*pts);self.relate('connect','body',name)
