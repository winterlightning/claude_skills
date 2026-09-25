"""Dog Poop.

Plan: Three rounded tiers and a pointed swirl apex; one detached odour curl above-left.
Centerline extremes: (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef0fd2f3-dc42-584f-a8c4-323f8b0b1723'
SOURCE_PATH = 'pictographic-primitives/pets/dog poop_ef0fd2f3-dc42-584f-a8c4-323f8b0b1723.svg'
AUTHOR = 'gpt-6'

class DogPoop(Solo48):
    icon_id = 'dog-poop'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('poop', 'dog', 'waste', 'mess', 'pet', 'clean-up', 'smell')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        arc('bottom-left',(16,44),(8,36),8)
        arc('bottom-shoulder',(8,36),(14,30),6)
        arc('middle-left',(14,30),(18,20),6,10)
        line('tip-1',(18,20),(24,14))
        line('tip-2',(24,14),(26,22))
        arc('middle-top',(26,22),(34,30),8)
        arc('bottom-right',(34,30),(40,36),6)
        arc('base-right',(40,36),(32,44),8)
        line('base',(32,44),(16,44))
        contour('pile','bottom-left','bottom-shoulder','middle-left','tip-1','tip-2','middle-top','bottom-right','base-right','base',closed=True)
        arc('odor',(10,4),(10,12),2,4)
