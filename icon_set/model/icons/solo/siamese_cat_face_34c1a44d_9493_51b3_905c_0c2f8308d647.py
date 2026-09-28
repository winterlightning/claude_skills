"""Siamese Cat Face.

Plan: Large ears and tapering rounded lower face with central nose and one pair of whiskers; symmetric.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34c1a44d-9493-51b3-905c-0c2f8308d647'
SOURCE_PATH = 'pictographic-primitives/pets/siamese_34c1a44d-9493-51b3-905c-0c2f8308d647.svg'
AUTHOR = 'gpt-6'

class SiameseCatFace(Solo48):
    icon_id = 'siamese-cat-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('cat', 'siamese', 'face', 'breed', 'whiskers', 'feline', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('upper',(6,24),(6,6),(18,16),mirror((18,16)),mirror((6,6)),mirror((6,24)))
        arc('right-jaw',mirror((6,24)),(24,42),18)
        arc('left-jaw',(24,42),(6,24),18)
        contour('jaw','right-jaw','left-jaw')
        self.relate('connect','upper','jaw')
        line('nose',(24,27),(24,32))
        line('whisker-left',(6,24),(14,24))
        line('whisker-right',mirror((14,24)),mirror((6,24)))
        for w in ('whisker-left','whisker-right'):
         self.relate('connect','upper',w);self.relate('connect','jaw',w)
