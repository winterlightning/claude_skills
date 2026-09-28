"""Fork and spoon cross at a shared node. Lucide utensils-crossed informs diagonal handle geometry; three tines and oval spoon bowl retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='6305d089-5f4e-4d0d-8488-b6bf8ef99e4d'
SOURCE_PATH='pictographic-primitives/symbol/spoon and fork_6305d089-5f4e-4d0d-8488-b6bf8ef99e4d.svg'
AUTHOR='gpt-6'

class ForkSpoonCrossed(Solo48):
    icon_id='fork-spoon-crossed'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('restaurant', 'fork', 'spoon', 'food', 'dining', 'cutlery', 'eat', 'meal')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.path('fork-head',[(6,18),(12,24),(18,24),(24,18),(24,12),(18,6)])
        self.path('fork-stem',[(6,6),(21,21),(27,27),(42,42)])
        self.relate('connect','fork-head','fork-stem')
        self.path('spoon-stem',[(12,42),(27,27),(37,18)])
        self.relate('connect','spoon-stem','fork-stem')
        self.oval('spoon-bowl',37,12,5,6)
        self.relate('connect','spoon-bowl','spoon-stem')
