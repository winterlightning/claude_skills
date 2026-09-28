"""A sparkle cluster with a left star and two right twinkles. Lucide sparkles informs the hierarchy; both plus-shaped twinkles are intrinsic shine marks, not action badges.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='a760b4a2-03ae-462b-9aa6-3ee940a9e6bb'
SOURCE_PATH='pictographic-primitives/symbol/sparkles_a760b4a2-03ae-462b-9aa6-3ee940a9e6bb.svg'
AUTHOR='gpt-6'

class SparklesStarPlus(Solo48):
    icon_id='sparkles-star-plus'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol",)
    aliases=()
    keywords=('sparkles', 'magic', 'shine', 'ai', 'new', 'clean', 'twinkle', 'effects')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.path('star',[(16,12),(20,23),(26,28),(20,32),(16,42),(12,32),(6,28),(12,23)],True)
        for name,cx,cy,r in [('upper',32,10,4),('lower',38,32,4)]:
            self.path(name+'-h',[(cx-r,cy),(cx,cy),(cx+r,cy)])
            self.path(name+'-v',[(cx,cy-r),(cx,cy),(cx,cy+r)])
            self.relate('connect',name+'-h',name+'-v')
