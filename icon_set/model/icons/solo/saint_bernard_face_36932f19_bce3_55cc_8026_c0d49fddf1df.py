"""Saint Bernard Face.

Plan: Broad domed head with long hanging jowls, centered nose and split lip; shared paired lower lobes.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36932f19-bce3-55cc-8026-c0d49fddf1df'
SOURCE_PATH = 'pictographic-primitives/pets/saint bernard_36932f19-bce3-55cc-8026-c0d49fddf1df.svg'
AUTHOR = 'gpt-6'

class SaintBernardFace(Solo48):
    icon_id = 'saint-bernard-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('dog', 'saint-bernard', 'face', 'breed', 'jowls', 'large-dog', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        arc('crown',(6,24),mirror((6,24)),18)
        line('right-side',mirror((6,24)),mirror((14,32)))
        line('left-side',(14,32),(6,24))
        contour('head','left-side','crown','right-side')
        line('jowl-left',(14,20),(14,36))
        arc('lower-left',(14,36),(24,36),5,6,False)
        arc('lower-right',(24,36),mirror((14,36)),5,6,False)
        line('jowl-right',mirror((14,36)),mirror((14,20)))
        contour('jowls','jowl-left','lower-left','lower-right','jowl-right')
        self.relate('connect','jowls','head')
        line('nose',(23,24),mirror((23,24)))
        line('stem',(24,24),(24,36))
        self.relate('connect','nose','stem')
        self.relate('connect','stem','jowls')
