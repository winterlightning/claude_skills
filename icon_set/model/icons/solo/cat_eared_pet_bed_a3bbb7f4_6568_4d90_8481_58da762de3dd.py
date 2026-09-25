"""Cat-Eared Pet Bed.

Plan: Cat-eared shell encloses one large arched opening; cushion seam omitted for clearance.
Keyshape centerline extremes: (6,6)-(42,42)
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3bbb7f4-6568-4d90-8481-58da762de3dd'
SOURCE_PATH = 'pictographic-primitives/pets/cat bed_a3bbb7f4-6568-4d90-8481-58da762de3dd.svg'
AUTHOR = 'gpt-6'

class CatEaredPetBed(Solo48):
    icon_id = 'cat-eared-pet-bed'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('cat-bed', 'bed', 'cave', 'cushion', 'cat', 'pet', 'sleep', 'furniture')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(point): return (2 * axis - point[0], point[1])
        self.add_polyline('shell',(6,42),(6,6),(16,10),mirror((16,10)),mirror((6,6)),mirror((6,42)),(6,42))
        arc('opening-top',(15,27),mirror((15,27)),9,8)
        line('opening-right',mirror((15,27)),mirror((15,33)))
        line('opening-bottom',mirror((15,33)),(15,33))
        line('opening-left',(15,33),(15,27))
        contour('opening','opening-top','opening-right','opening-bottom','opening-left',closed=True)
