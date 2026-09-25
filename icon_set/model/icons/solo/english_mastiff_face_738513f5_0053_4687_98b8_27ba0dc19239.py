"""English Mastiff Face.

Plan: Broad arched crown and folded side ears, heavy paired hanging jowls and central muzzle stem. Mirror pairs share radii.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '738513f5-0053-4687-98b8-27ba0dc19239'
SOURCE_PATH = 'pictographic-primitives/pets/english mastiff_738513f5-0053-4687-98b8-27ba0dc19239.svg'
AUTHOR = 'gpt-6'

class EnglishMastiffFace(Solo48):
    icon_id = 'english-mastiff-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'mastiff', 'english-mastiff', 'face', 'breed', 'jowls', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        arc('crown',(6,24),mirror((6,24)),18)
        arc('ear-right',mirror((6,24)),mirror((14,24)),4,6)
        arc('ear-left',(14,24),(6,24),4,6)
        contour('top','ear-left','crown','ear-right')
        line('jowl-left-down',(14,24),(14,36))
        arc('jowl-left-end',(14,36),(24,36),5,6,False)
        arc('jowl-right-end',(24,36),mirror((14,36)),5,6,False)
        line('jowl-right-up',mirror((14,36)),mirror((14,24)))
        contour('jowls','jowl-left-down','jowl-left-end','jowl-right-end','jowl-right-up')
        self.relate('connect','top','jowls')
        line('nose',(23,24),mirror((23,24)))
        line('muzzle',(24,24),(24,36))
        self.relate('connect','nose','muzzle')
        self.relate('connect','muzzle','jowls')
