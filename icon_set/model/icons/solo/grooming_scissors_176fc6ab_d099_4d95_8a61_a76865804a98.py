"""Grooming Scissors.

Plan: Two separate equal round finger loops, two shafts meeting at one pivot and divergent blades; intentional diagonal orientation.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '176fc6ab-d099-4d95-8a61-a76865804a98'
SOURCE_PATH = 'pictographic-primitives/pets/grooming scissor_176fc6ab-d099-4d95-8a61-a76865804a98.svg'
AUTHOR = 'gpt-6'

class GroomingScissors(Solo48):
    icon_id = 'grooming-scissors'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('scissors', 'grooming', 'cut', 'trim', 'shears', 'pet', 'salon')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        for name,cx,cy in [('upper-loop',12,14),('lower-loop',18,36)]:
         arc(name+'-right',(cx,cy-6),(cx,cy+6),6)
         arc(name+'-left',(cx,cy+6),(cx,cy-6),6)
         contour(name,name+'-right',name+'-left',closed=True)
        self.add_polyline('upper-shaft',(18,14),(30,22),(42,14))
        self.add_polyline('lower-shaft',(18,30),(30,22),(36,6))
        self.relate('connect','upper-loop','upper-shaft')
        self.relate('connect','lower-loop','lower-shaft')
        self.relate('connect','upper-shaft','lower-shaft')
