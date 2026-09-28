"""Bernese Mountain Dog Face.

Plan: Flat crown and broad cheeks, mirrored long hanging coat edges, central split muzzle.
Keyshape centerline extremes: (6,6)-(42,42)
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abf9d7c5-9b5d-543d-86fe-9e1ff0364cb2'
SOURCE_PATH = 'pictographic-primitives/pets/bernese mountain dog_abf9d7c5-9b5d-543d-86fe-9e1ff0364cb2.svg'
AUTHOR = 'gpt-6'

class BerneseMountainDogFace(Solo48):
    icon_id = 'bernese-mountain-dog-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('dog', 'bernese', 'mountain-dog', 'face', 'breed', 'pet', 'floppy-ears')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(point): return (2 * axis - point[0], point[1])
        line('crown',(16,6),mirror((16,6)))
        arc('right-temple',mirror((16,6)),mirror((6,16)),10)
        line('right-coat',mirror((6,16)),mirror((6,42)))
        line('left-coat',(6,42),(6,16))
        arc('left-temple',(6,16),(16,6),10)
        contour('coat','left-coat','left-temple','crown','right-temple','right-coat')
        line('nose',(22,22),mirror((22,22)))
        line('muzzle-stem',(24,22),(24,29))
        arc('muzzle-left',(15,29),(24,29),5,5,False)
        arc('muzzle-right',(24,29),mirror((15,29)),5,5,False)
        contour('muzzle','muzzle-left','muzzle-right')
        self.relate('connect','nose','muzzle-stem')
        self.relate('connect','muzzle','muzzle-stem')
