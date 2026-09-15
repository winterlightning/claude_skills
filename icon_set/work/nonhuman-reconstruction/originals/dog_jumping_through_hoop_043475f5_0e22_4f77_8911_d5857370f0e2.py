"""Dog Jumping through Hoop.

Plan: Right-facing leaping dog crosses an open oval hoop. Hoop is interrupted where dog passes; extended legs and pointed ear carry the action.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '043475f5-0e22-4f77-8911-d5857370f0e2'
SOURCE_PATH = 'pictographic-primitives/pets/dog jump_043475f5-0e22-4f77-8911-d5857370f0e2.svg'
AUTHOR = 'gpt-6'

class DogJumpingThroughHoop(Solo48):
    icon_id = 'dog-jumping-through-hoop'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'jump', 'hoop', 'agility', 'trick', 'training', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        arc('hoop-upper',(4,24),(20,8),16,16)
        arc('hoop-lower',(20,40),(4,24),16,16)
        self.add_polyline('back',(4,24),(30,16),(34,8),(38,16),(44,20),(40,24),(32,24))
        self.add_polyline('legs',(32,24),(40,32),(34,34),(26,28),(16,30),(12,40))
        self.relate('connect','back','legs')
        self.relate('connect','hoop-upper','back')
        self.relate('connect','hoop-lower','back')
        self.relate('connect','hoop-upper','hoop-lower')
