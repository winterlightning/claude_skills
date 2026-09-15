"""Dog Food Bowl.

Plan: Broad sloped bowl with flat base and three rounded kibble lobes; mirrored food mound.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef989e1c-ca2d-4808-9e01-23f51f35f24a'
SOURCE_PATH = 'pictographic-primitives/pets/dog food_ef989e1c-ca2d-4808-9e01-23f51f35f24a.svg'
AUTHOR = 'gpt-6'

class DogFoodBowl(Solo48):
    icon_id = 'dog-food-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog-food', 'bowl', 'kibble', 'feeding', 'pet', 'food', 'dish')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('bowl',(8,25),mirror((8,25)),mirror((4,40)),(4,40),(8,25))
        arc('food-left',(8,16),(16,12),8,4)
        arc('food-center',(16,12),mirror((16,12)),8,4)
        arc('food-right',mirror((16,12)),mirror((8,16)),8,4)
        contour('food','food-left','food-center','food-right')
