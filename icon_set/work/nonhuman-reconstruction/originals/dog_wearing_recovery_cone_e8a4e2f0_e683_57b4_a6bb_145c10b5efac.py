"""Dog Wearing Recovery Cone.

Plan: Right-facing pointed-ear dog behind a broad funnel collar; two legs descend from its lower edge. Collar is physical equipment.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8a4e2f0-e683-57b4-a6bb-145c10b5efac'
SOURCE_PATH = 'pictographic-primitives/pets/pet cone_e8a4e2f0-e683-57b4-a6bb-145c10b5efac.svg'
AUTHOR = 'gpt-6'

class DogWearingRecoveryCone(Solo48):
    icon_id = 'dog-wearing-recovery-cone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'cone', 'recovery', 'e-collar', 'vet', 'injury', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('cone',(6,28),(15,24),(33,16),(42,12),(36,32),(18,40),(6,28))
        self.add_polyline('head',(15,24),(15,16),(22,12),(22,6),(30,12),(33,16))
        self.relate('connect','head','cone')
        line('leg-left',(18,40),(18,42))
        line('leg-right',(36,32),(42,42))
        self.relate('connect','cone','leg-left')
        self.relate('connect','cone','leg-right')
