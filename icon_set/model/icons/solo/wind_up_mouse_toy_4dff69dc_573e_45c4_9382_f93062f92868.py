"""Wind-Up Mouse Toy.

Plan: Right-facing mouse body, winding key with two circular lobes and a curling tail; asymmetric physical toy.
Keyshape centerline extremes: (6,6)-(42,42)
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4dff69dc-573e-45c4-9382-f93062f92868'
SOURCE_PATH = 'pictographic-primitives/pets/cat mouse toy_4dff69dc-573e-45c4-9382-f93062f92868.svg'
AUTHOR = 'gpt-6'

class WindUpMouseToy(Solo48):
    icon_id = 'wind-up-mouse-toy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('mouse', 'toy', 'wind-up', 'cat-toy', 'key', 'play', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        arc('back',(14,30),(26,18),12)
        arc('snout',(26,18),(42,30),16,12)
        arc('nose',(42,30),(36,36),6)
        line('belly',(36,36),(20,36))
        arc('haunch',(20,36),(14,30),6)
        contour('body','back','snout','nose','belly','haunch',closed=True)
        # Two equal circular key lobes and the stem form one winding mechanism.
        for side,cx in (('left',18),('right',34)):
            arc(f'key-{side}-top',(cx-3,9),(cx+3,9),3)
            arc(f'key-{side}-bottom',(cx+3,9),(cx-3,9),3)
            contour(f'key-{side}',f'key-{side}-top',f'key-{side}-bottom',closed=True)
        self.add_polyline('key-branch',(21,9),(26,14),(31,9))
        line('shaft',(26,14),(26,18))
        self.relate('connect','key-branch','key-left')
        self.relate('connect','key-branch','key-right')
        self.relate('connect','key-branch','shaft')
        self.relate('connect','body','shaft')
        arc('tail-turn',(14,30),(6,38),8,sweep=False)
        arc('tail-end',(6,38),(10,42),4,sweep=False)
        line('tail-tip',(10,42),(18,42))
        contour('tail','tail-turn','tail-end','tail-tip')
        self.relate('connect','body','tail')
