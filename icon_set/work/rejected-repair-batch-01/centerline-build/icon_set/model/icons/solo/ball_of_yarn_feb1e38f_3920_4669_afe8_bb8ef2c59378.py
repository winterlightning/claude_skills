"""Ball of Yarn.

Plan: Round yarn ball with two curved winding runs and a loose right-hand strand. Large crossings remain structural.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'feb1e38f-3920-4669-afe8-bb8ef2c59378'
SOURCE_PATH = 'pictographic-primitives/pets/cat yarn_feb1e38f-3920-4669-afe8-bb8ef2c59378.svg'
AUTHOR = 'gpt-6'

class BallOfYarn(Solo48):
    icon_id = 'ball-of-yarn'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('yarn', 'ball', 'wool', 'knitting', 'cat-toy', 'thread', 'play')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        arc('ball-top',(6,24),(38,24),16,18)
        arc('ball-bottom',(38,24),(6,24),16,18)
        contour('ball','ball-top','ball-bottom',closed=True)
        arc('wrap-left',(22,6),(6,24),16,18)
        arc('wrap-right',(38,24),(22,42),16,18,False)
        self.relate('connect','ball','wrap-left')
        self.relate('connect','ball','wrap-right')
        arc('strand',(38,24),(42,34),4,10)
        line('strand-tip',(42,34),(42,42))
        contour('tail','strand','strand-tip')
        self.relate('connect','tail','ball')
