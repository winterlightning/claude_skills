"""Dog Face with Floppy Ears.

Plan: Rounded head and wide floppy ears with paired dot eyes and split muzzle; simplified face on a shared axis.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ca99e56-4412-50a8-b256-eb45334f9ed2'
SOURCE_PATH = 'pictographic-primitives/pets/dog face_7ca99e56-4412-50a8-b256-eb45334f9ed2.svg'
AUTHOR = 'gpt-6'

class DogFaceFloppyEars(Solo48):
    icon_id = 'dog-face-floppy-ears'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'face', 'puppy', 'floppy-ears', 'pet', 'friendly', 'head')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        arc('crown',(6,24),mirror((6,24)),18)
        line('ear-right',mirror((6,24)),mirror((6,34)))
        arc('ear-right-tip',mirror((6,34)),mirror((14,34)),4)
        line('inner-right',mirror((14,34)),mirror((14,29)))
        line('inner-left',(14,29),(14,34))
        arc('ear-left-tip',(14,34),(6,34),4)
        line('ear-left',(6,34),(6,24))
        contour('outline','inner-left','ear-left-tip','ear-left','crown','ear-right','ear-right-tip','inner-right')
        arc('chin',(14,34),mirror((14,34)),10,8,False)
        self.relate('connect','chin','outline')
        for i,x in enumerate((20,28)): self.add_dot(f'eye-{i}',(x,19))
        self.add_polyline('mouth',(23,29),(24,31),mirror((23,29)))
