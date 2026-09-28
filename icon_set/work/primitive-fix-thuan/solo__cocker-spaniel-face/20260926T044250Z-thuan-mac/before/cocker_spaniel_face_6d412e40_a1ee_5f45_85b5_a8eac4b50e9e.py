"""Cocker Spaniel Face.

Plan: Domed crown with long wavy open ears and a central nose/split mouth. Paired curves mirror around shared axis.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d412e40-a1ee-5f45-85b5-a8eac4b50e9e'
SOURCE_PATH = 'pictographic-primitives/pets/cocker spaniel_6d412e40-a1ee-5f45-85b5-a8eac4b50e9e.svg'
AUTHOR = 'gpt-6'

class CockerSpanielFace(Solo48):
    icon_id = 'cocker-spaniel-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('dog', 'cocker-spaniel', 'spaniel', 'face', 'breed', 'floppy-ears', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis = 24
        def mirror(p): return (2 * axis - p[0], p[1])
        arc('crown',(6,24),mirror((6,24)),18)
        arc('ear-right-upper',mirror((6,24)),mirror((10,33)),4,9)
        arc('ear-right-lower',mirror((10,33)),mirror((6,42)),4,9,False)
        arc('ear-left-lower',(6,42),(10,33),4,9,False)
        arc('ear-left-upper',(10,33),(6,24),4,9)
        contour('outline','ear-left-lower','ear-left-upper','crown','ear-right-upper','ear-right-lower')
        line('nose',(22,23),mirror((22,23)))
        line('stem',(24,23),(24,29))
        arc('muzzle-left',(19,29),(24,29),3,3,False)
        arc('muzzle-right',(24,29),mirror((19,29)),3,3,False)
        contour('muzzle','muzzle-left','muzzle-right')
        self.relate('connect','nose','stem')
        self.relate('connect','stem','muzzle')
