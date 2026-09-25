"""Dalmatian Face.

Plan: Rounded crown, folded ears, neck and central split mouth; omit small eyes to give muzzle clear space.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd0d9c0a-6ed5-48eb-b294-bbe6008deef9'
SOURCE_PATH = 'pictographic-primitives/pets/dalmatian_fd0d9c0a-6ed5-48eb-b294-bbe6008deef9.svg'
AUTHOR = 'gpt-6'

class DalmatianFace(Solo48):
    icon_id = 'dalmatian-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'dalmatian', 'face', 'breed', 'pet', 'puppy', 'ears')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis = 24
        def mirror(p): return (2 * axis - p[0], p[1])
        arc('crown',(6,24),mirror((6,24)),18)
        arc('ear-right',mirror((6,24)),mirror((14,24)),4,7)
        arc('ear-left',(14,24),(6,24),4,7)
        contour('head','ear-left','crown','ear-right')
        line('neck-left',(6,24),(10,42))
        line('neck-right',mirror((6,24)),mirror((10,42)))
        self.relate('connect','head','neck-left')
        self.relate('connect','head','neck-right')
        line('nose',(23,24),mirror((23,24)))
        line('stem',(24,24),(24,34))
        arc('mouth-left',(20,34),(24,34),3,3,False)
        arc('mouth-right',(24,34),mirror((20,34)),3,3,False)
        contour('mouth','mouth-left','mouth-right')
        self.relate('connect','stem','nose')
        self.relate('connect','stem','mouth')
