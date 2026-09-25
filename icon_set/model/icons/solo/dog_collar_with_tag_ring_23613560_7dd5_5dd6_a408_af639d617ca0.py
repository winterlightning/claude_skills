"""Dog Collar with Tag Ring.

Plan: Perspective collar band with elliptical top, curved front, central stem and round tag; one shared axis.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23613560-7dd5-5dd6-a408-af639d617ca0'
SOURCE_PATH = 'pictographic-primitives/pets/dog collar_23613560-7dd5-5dd6-a408-af639d617ca0.svg'
AUTHOR = 'gpt-6'

class DogCollarWithTagRing(Solo48):
    icon_id = 'dog-collar-with-tag-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('collar', 'dog', 'tag', 'ring', 'accessory', 'pet', 'id')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        # A single perspective band leaves room for a visibly open tag ring.
        arc('band-back',(6,14),mirror((6,14)),18,8)
        arc('band-front-right',mirror((6,14)),(24,22),18,8)
        arc('band-front-left',(24,22),(6,14),18,8)
        contour('band','band-back','band-front-right','band-front-left',closed=True)
        line('stem',(24,22),(24,34))
        arc('tag-right',(24,34),(24,42),4)
        arc('tag-left',(24,42),(24,34),4)
        contour('tag','tag-right','tag-left',closed=True)
        self.relate('connect','stem','band')
        self.relate('connect','stem','tag')
