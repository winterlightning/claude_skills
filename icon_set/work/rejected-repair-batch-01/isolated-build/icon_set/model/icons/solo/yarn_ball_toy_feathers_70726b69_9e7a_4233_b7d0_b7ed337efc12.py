"""Yarn Ball Toy with Feathers.

Plan: Lower-left yarn ball with one curved winding band and two open leaf-shaped feather strokes above-right. Motion dashes omitted.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70726b69-9e7a-4233-b7d0-b7ed337efc12'
SOURCE_PATH = 'pictographic-primitives/pets/cat yarn toy_70726b69-9e7a-4233-b7d0-b7ed337efc12.svg'
AUTHOR = 'gpt-6'

class YarnBallToyFeathers(Solo48):
    icon_id = 'yarn-ball-toy-feathers'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('yarn', 'ball', 'cat-toy', 'feathers', 'play', 'motion', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        arc('ball-upper',(6,28),(30,28),12)
        arc('ball-lower',(30,28),(6,28),12,14)
        contour('ball','ball-upper','ball-lower',closed=True)
        arc('winding',(6,28),(18,42),12,14)
        self.relate('connect','winding','ball')
        arc('feather-back',(18,16),(24,6),10,8,False)
        arc('feather-tip',(24,6),(36,18),12)
        arc('feather-front',(36,18),(42,8),10,12,False)
        contour('feathers','feather-back','feather-tip','feather-front')
        self.relate('connect','ball','feathers')
