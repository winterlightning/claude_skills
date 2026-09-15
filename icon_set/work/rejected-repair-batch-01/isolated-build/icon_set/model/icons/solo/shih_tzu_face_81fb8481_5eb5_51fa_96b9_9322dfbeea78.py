"""Shih Tzu Face.

Plan: Domed crown and long hanging ears with paired eyes and central muzzle; shared symmetrical ear radii.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81fb8481-5eb5-51fa-96b9-9322dfbeea78'
SOURCE_PATH = 'pictographic-primitives/pets/shih tzu_81fb8481-5eb5-51fa-96b9-9322dfbeea78.svg'
AUTHOR = 'gpt-6'

class ShihTzuFace(Solo48):
    icon_id = 'shih-tzu-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'shih-tzu', 'face', 'breed', 'long-ears', 'small-dog', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        arc('crown',(6,24),mirror((6,24)),18)
        line('right-side',mirror((6,24)),mirror((6,36)))
        arc('right-ear',mirror((6,36)),mirror((14,36)),4,6)
        line('right-inner',mirror((14,36)),mirror((14,28)))
        line('left-inner',(14,28),(14,36))
        arc('left-ear',(14,36),(6,36),4,6)
        line('left-side',(6,36),(6,24))
        contour('outline','left-inner','left-ear','left-side','crown','right-side','right-ear','right-inner')
        for i,x in enumerate((20,28)):self.add_dot(f'eye-{i}',(x,20))
        self.add_polyline('muzzle',(23,32),(24,29),mirror((23,32)))
