"""Poodle Head.

Plan: Cloud-like topknot, long rounded pompom ears and narrow squared face. Mirrored lobes share radii.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e314897f-f4bf-493a-bfcc-5a3f735b207b'
SOURCE_PATH = 'pictographic-primitives/pets/poodle_e314897f-f4bf-493a-bfcc-5a3f735b207b.svg'
AUTHOR = 'gpt-6'

class PoodleHead(Solo48):
    icon_id = 'poodle-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'poodle', 'head', 'breed', 'topknot', 'groomed', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        arc('top-left',(6,18),(18,18),6,8)
        arc('top-middle',(18,10),mirror((18,10)),6,4)
        arc('top-right',mirror((18,18)),mirror((6,18)),6,8)
        line('top-join-left',(18,18),(18,10))
        line('top-join-right',mirror((18,10)),mirror((18,18)))
        contour('topknot','top-left','top-join-left','top-middle','top-join-right','top-right')
        line('right-side',mirror((6,18)),mirror((6,34)))
        arc('right-ear',mirror((6,34)),mirror((16,34)),5,8)
        line('left-inner',(16,34),(16,24))
        line('right-inner',mirror((16,24)),mirror((16,34)))
        arc('left-ear',(16,34),(6,34),5,8)
        line('left-side',(6,34),(6,18))
        self.relate('connect','topknot','right-side')
        self.relate('connect','topknot','left-side')
        contour('ear-left','left-inner')
        self.add_polyline('face',(16,24),(20,40),mirror((20,40)),mirror((16,24)))
        for a,b in [('right-side','right-ear'),('right-ear','right-inner'),('left-ear','left-side'),('left-ear','ear-left'),('ear-left','face'),('right-inner','face')]:self.relate('connect',a,b)
