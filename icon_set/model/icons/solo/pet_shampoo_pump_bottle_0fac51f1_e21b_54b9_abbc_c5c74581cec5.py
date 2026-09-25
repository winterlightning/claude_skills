"""Pet Shampoo Pump Bottle.

Plan: Rounded bottle with short pump stem and right-pointing nozzle; one centered oval label.
Centerline extremes: (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fac51f1-e21b-54b9-abbc-c5c74581cec5'
SOURCE_PATH = 'pictographic-primitives/pets/grooming shampoo_0fac51f1-e21b-54b9-abbc-c5c74581cec5.svg'
AUTHOR = 'gpt-6'

class PetShampooPumpBottle(Solo48):
    icon_id = 'pet-shampoo-pump-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('shampoo', 'bottle', 'pump', 'grooming', 'wash', 'bath', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        line('pump-top',(16,4),(32,4))
        line('nozzle',(32,4),(40,8))
        line('stem',(24,4),(24,16))
        self.relate('connect','pump-top','nozzle')
        self.relate('connect','pump-top','stem')
        line('shoulder',(16,16),(24,16))
        line('shoulder-right',(24,16),(32,16))
        arc('corner-tr',(32,16),(40,24),8)
        line('side-right',(40,24),(40,36))
        arc('corner-br',(40,36),(32,44),8)
        line('base',(32,44),(16,44))
        arc('corner-bl',(16,44),(8,36),8)
        line('side-left',(8,36),(8,24))
        arc('corner-tl',(8,24),(16,16),8)
        contour('bottle','shoulder','shoulder-right','corner-tr','side-right','corner-br','base','corner-bl','side-left','corner-tl',closed=True)
        self.relate('connect','stem','bottle')
        line('label',(24,27),(24,33))
