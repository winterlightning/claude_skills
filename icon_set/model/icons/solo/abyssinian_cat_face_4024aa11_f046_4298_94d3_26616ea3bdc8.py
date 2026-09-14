"""Abyssinian Cat Face.

Plan: Tall mirrored ears, round cheeks and scalloped lower muzzle; whiskers reduced to one pair.
Keyshape centerline extremes: (6,6)-(42,42)
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4024aa11-f046-4298-94d3-26616ea3bdc8'
SOURCE_PATH = 'pictographic-primitives/pets/abyssinian_4024aa11-f046-4298-94d3-26616ea3bdc8.svg'
AUTHOR = 'gpt-6'

class AbyssinianCatFace(Solo48):
    icon_id = 'abyssinian-cat-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('cat', 'abyssinian', 'face', 'breed', 'whiskers', 'pet', 'feline', 'kitten')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(point): return (2 * axis - point[0], point[1])
        self.add_polyline('ears',(6,24),(6,6),(16,16),mirror((16,16)),mirror((6,6)),mirror((6,24)))
        arc('right-cheek',mirror((6,24)),mirror((16,34)),10)
        arc('right-muzzle',mirror((16,34)),(24,42),8)
        arc('left-muzzle',(24,42),(16,34),8)
        arc('left-cheek',(16,34),(6,24),10)
        contour('lower','right-cheek','right-muzzle','left-muzzle','left-cheek')
        self.relate('connect','ears','lower')
        line('whisker-left',(6,34),(16,34))
        line('whisker-right',mirror((16,34)),mirror((6,34)))
        self.relate('connect','lower','whisker-left')
        self.relate('connect','lower','whisker-right')
