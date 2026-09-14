"""Beagle Face.

Plan: Domed crown owns mirrored hanging ears; centered muzzle and hanging tongue.
Keyshape centerline extremes: (6,6)-(42,42)
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a59ab79-e2e5-4a74-9b88-e1e5c0c1cad4'
SOURCE_PATH = 'pictographic-primitives/pets/beagle_8a59ab79-e2e5-4a74-9b88-e1e5c0c1cad4.svg'
AUTHOR = 'gpt-6'

class BeagleFace(Solo48):
    icon_id = 'beagle-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'beagle', 'face', 'breed', 'floppy-ears', 'tongue', 'pet', 'puppy')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(point): return (2 * axis - point[0], point[1])
        arc('crown',(6,24),mirror((6,24)),18)
        line('right-ear-side',mirror((6,24)),mirror((6,30)))
        arc('right-ear-end',mirror((6,30)),mirror((15,30)),5,5)
        line('right-ear-inner',mirror((15,30)),mirror((15,21)))
        line('left-ear-inner',(15,21),(15,30))
        arc('left-ear-end',(15,30),(6,30),5,5)
        line('left-ear-side',(6,30),(6,24))
        contour('outline','left-ear-inner','left-ear-end','left-ear-side','crown','right-ear-side','right-ear-end','right-ear-inner')
        self.add_dot('nose',(24,25))
        arc('tongue',(20,38),mirror((20,38)),4,4,False)
