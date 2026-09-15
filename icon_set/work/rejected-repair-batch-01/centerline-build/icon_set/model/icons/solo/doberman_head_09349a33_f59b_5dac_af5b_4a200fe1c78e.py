"""Doberman Head.

Plan: Mirrored tall cropped ears and steep taper to paired lower muzzle lobes; narrow front-facing head.
Centerline extremes: (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09349a33-f59b-5dac-af5b-4a200fe1c78e'
SOURCE_PATH = 'pictographic-primitives/pets/doberman_09349a33-f59b-5dac-af5b-4a200fe1c78e.svg'
AUTHOR = 'gpt-6'

class DobermanHead(Solo48):
    icon_id = 'doberman-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'doberman', 'head', 'breed', 'ears', 'guard-dog', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis = 24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('upper',(8,22),(8,4),(18,14),mirror((18,14)),mirror((8,4)),mirror((8,22)),mirror((16,32)),mirror((18,40)))
        arc('muzzle-right',mirror((18,40)),(24,44),6,4)
        arc('muzzle-left',(24,44),(18,40),6,4)
        self.add_polyline('lower-left',(18,40),(16,32),(8,22))
        self.relate('connect','upper','muzzle-right')
        self.relate('connect','muzzle-right','muzzle-left')
        self.relate('connect','muzzle-left','lower-left')
        self.relate('connect','lower-left','upper')
