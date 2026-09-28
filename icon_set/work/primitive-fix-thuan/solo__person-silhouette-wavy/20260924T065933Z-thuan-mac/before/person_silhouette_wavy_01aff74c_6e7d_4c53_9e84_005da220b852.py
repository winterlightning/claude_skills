"""Continuous head, neck and shoulder outline. Lucide user-round informs the crown and shoulder radii; gentle cheek curves replace tiny source ripples.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='01aff74c-6e7d-4c53-9e84-005da220b852'
SOURCE_PATH='pictographic-primitives/symbol/sub square_01aff74c-6e7d-4c53-9e84-005da220b852.svg'
AUTHOR='gpt-6'

class PersonSilhouetteWavy(Solo48):
    icon_id='person-silhouette-wavy'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('person', 'user', 'silhouette', 'profile', 'avatar', 'anonymous', 'account', 'member')

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

        self.add_line('left-base',(6,42),(6,40))
        self.add_arc('left-shoulder',(6,40),(12,34),radius_x=6)
        self.add_line('left-slope',(12,34),(20,30))
        self.add_line('left-neck',(20,30),(20,25))
        self.add_arc('left-cheek',(20,25),(16,17),radius_x=8)
        self.add_line('left-temple',(16,17),(16,14))
        self.add_arc('crown',(16,14),(32,14),radius_x=8)
        self.add_line('right-temple',(32,14),(32,17))
        self.add_arc('right-cheek',(32,17),(28,25),radius_x=8)
        self.add_line('right-neck',(28,25),(28,30))
        self.add_line('right-slope',(28,30),(36,34))
        self.add_arc('right-shoulder',(36,34),(42,40),radius_x=6)
        self.add_line('right-base',(42,40),(42,42))
        self.add_contour('silhouette','left-base','left-shoulder','left-slope','left-neck','left-cheek','left-temple','crown','right-temple','right-cheek','right-neck','right-slope','right-shoulder','right-base')
