"""Person with Sitting Dog.

Plan: Person at left with round head and reaching arm; smaller sitting dog at lower-right. Natural companion scene.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5975e83c-ac8d-537e-ad6b-a0dc227c0bdb'
SOURCE_PATH = 'pictographic-primitives/pets/dog playing_5975e83c-ac8d-537e-ad6b-a0dc227c0bdb.svg'
AUTHOR = 'gpt-6'

class PersonWithSittingDog(Solo48):
    icon_id = 'person-with-sitting-dog'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('dog', 'person', 'owner', 'training', 'play', 'pet', 'companion')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        arc('person-head-top',(6,12),(18,12),6)
        arc('person-head-bottom',(18,12),(6,12),6)
        contour('person-head','person-head-top','person-head-bottom',closed=True)
        self.add_polyline('person',(6,42),(6,28),(18,28),(26,22))
        line('arm-lower',(26,22),(28,16))
        self.relate('connect','person','arm-lower')
        self.add_polyline('dog',(24,42),(24,34),(32,30),(34,24),(40,30),(42,42))
