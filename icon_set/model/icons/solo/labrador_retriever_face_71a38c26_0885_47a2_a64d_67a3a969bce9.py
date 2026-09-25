"""Labrador Retriever Face.

Plan: Flat crown, folded outward ears, broad neck and paired rounded muzzle lobes beneath a centered nose.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71a38c26-0885-47a2-a64d-67a3a969bce9'
SOURCE_PATH = 'pictographic-primitives/pets/labrador retriever_71a38c26-0885-47a2-a64d-67a3a969bce9.svg'
AUTHOR = 'gpt-6'

class LabradorRetrieverFace(Solo48):
    icon_id = 'labrador-retriever-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'labrador', 'retriever', 'face', 'breed', 'pet', 'friendly')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('crown',(6,20),(14,6),mirror((14,6)),mirror((6,20)),mirror((14,24)))
        line('left-ear',(14,24),(6,20))
        self.add_polyline('left-side',(14,18),(14,24),(6,42))
        self.add_polyline('right-side',mirror((14,18)),mirror((14,24)),mirror((6,42)))
        self.relate('connect','crown','left-ear')
        self.relate('connect','left-side','left-ear')
        self.relate('connect','right-side','crown')
        line('nose',(23,23),mirror((23,23)))
        line('stem',(24,23),(24,31))
        arc('muzzle-left',(20,31),(24,31),4,4,False)
        arc('muzzle-right',(24,31),mirror((20,31)),4,4,False)
        contour('muzzle','muzzle-left','muzzle-right')
        self.relate('connect','stem','nose')
        self.relate('connect','stem','muzzle')
