"""Cup holding a pointed pencil and ruler. Lucide pencil and pencil-ruler inform simple tool silhouettes; ruler slot omitted for clearance. Physical tool grouping retained.

SOLO48 VRECT_L; live visible envelope (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='104c25ae-97c3-4c5b-897d-6e2ec2b026fa'
SOURCE_PATH='pictographic-primitives/symbol/stationary_104c25ae-97c3-4c5b-897d-6e2ec2b026fa.svg'
AUTHOR='gpt-6'

class PencilCup(Solo48):
    icon_id='pencil-cup'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('stationery', 'pencil', 'cup', 'ruler', 'desk', 'office', 'school', 'supplies')

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

        self.raw('rim',[(8,24),(12,24),(20,24),(30,24),(40,24)])
        self.add_line('right',(40,24),(40,38))
        self.add_arc('br',(40,38),(34,44),radius_x=6)
        self.add_line('base',(34,44),(14,44))
        self.add_arc('bl',(14,44),(8,38),radius_x=6)
        self.add_line('left',(8,38),(8,24))
        self.add_contour('cup',*['rim-'+str(i) for i in range(1,5)],'right','br','base','bl','left',closed=True)
        self.path('pencil',[(12,24),(8,12),(12,4),(16,10),(20,24)],True)
        self.path('ruler',[(30,24),(30,4),(40,4),(40,24)],True)
        self.relate('connect','pencil','cup');self.relate('connect','ruler','cup')
