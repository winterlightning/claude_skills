"""Persian Cat Face.

Plan: Round flat face with short ears, squinting eyes, small W mouth and simplified whiskers.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '732fc3f1-4105-500c-9a70-0bc9b625943c'
SOURCE_PATH = 'pictographic-primitives/pets/persian_732fc3f1-4105-500c-9a70-0bc9b625943c.svg'
AUTHOR = 'gpt-6'

class PersianCatFace(Solo48):
    icon_id = 'persian-cat-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('cat', 'persian', 'face', 'breed', 'whiskers', 'feline', 'grumpy')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('upper',(6,24),(6,6),(16,14),mirror((16,14)),mirror((6,6)),mirror((6,24)))
        arc('right-jaw',mirror((6,24)),(24,42),18)
        arc('left-jaw',(24,42),(6,24),18)
        contour('jaw','right-jaw','left-jaw')
        self.relate('connect','upper','jaw')
        for i,x in enumerate((16,30)):line(f'eye-{i}',(x,23),(x+2,23))
        self.add_polyline('mouth',(20,32),(22,33),(24,32),mirror((22,33)),mirror((20,32)))
