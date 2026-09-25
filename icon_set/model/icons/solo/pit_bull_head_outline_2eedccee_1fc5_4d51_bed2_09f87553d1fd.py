"""Pit Bull Head Outline.

Plan: Broad flat crown, small curled folded ears and open lower cheeks; mirrored elliptical turns.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2eedccee-1fc5-4d51-bed2-09f87553d1fd'
SOURCE_PATH = 'pictographic-primitives/pets/dog pitbull_2eedccee-1fc5-4d51-bed2-09f87553d1fd.svg'
AUTHOR = 'gpt-6'

class PitBullHeadOutline(Solo48):
    icon_id = 'pit-bull-head-outline'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'pit-bull', 'head', 'breed', 'outline', 'ears', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('crown',(4,20),(8,8),(16,8),(20,12),mirror((20,12)),mirror((16,8)),mirror((8,8)),mirror((4,20)))
        arc('ear-left-inner',(16,20),(10,24),6,4)
        arc('ear-left-outer',(10,24),(4,20),6,4)
        arc('ear-right-outer',mirror((4,20)),mirror((10,24)),6,4)
        arc('ear-right-inner',mirror((10,24)),mirror((16,20)),6,4)
        contour('ear-left','ear-left-inner','ear-left-outer')
        contour('ear-right','ear-right-outer','ear-right-inner')
        self.relate('connect','crown','ear-right')
        self.relate('connect','crown','ear-left')
        arc('jaw-left',(10,24),(10,40),5,8,False)
        arc('jaw-right',mirror((10,40)),mirror((10,24)),5,8,False)
        self.relate('connect','ear-left','jaw-left')
        self.relate('connect','ear-right','jaw-right')
