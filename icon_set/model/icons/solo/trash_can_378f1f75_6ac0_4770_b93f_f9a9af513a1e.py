"""Tapered trash can with domed lid handle and central rib. Lucide trash-2 informs the rim/handle/body hierarchy; only one source rib retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='378f1f75-6ac0-4770-b93f-f9a9af513a1e'
SOURCE_PATH='pictographic-primitives/symbol/trash_378f1f75-6ac0-4770-b93f-f9a9af513a1e.svg'
AUTHOR='gpt-6'

class TrashCan(Solo48):
    icon_id='trash-can'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('trash', 'delete', 'bin', 'garbage', 'waste', 'remove', 'rubbish', 'discard')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def raw(self,n,points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(n+'-'+str(j),a,b)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.path('rim',[(6,14),(10,14),(14,14),(34,14),(38,14),(42,14)])
        self.add_arc('handle',(14,14),(34,14),radius_x=10,radius_y=8)
        self.relate('connect','handle','rim')
        self.path('body',[(10,14),(12,36),(16,42),(32,42),(36,36),(38,14)])
        self.relate('connect','body','rim')
        self.add_line('rib',(24,24),(24,32))
