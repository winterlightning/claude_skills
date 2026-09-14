"""Sports strategy path from a ring to an arrow, with two X player marks. Lucide route informs tangent turns; all tactical marks belong to the diagram.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='cf25f25b-0432-4d98-b894-c281bc60e8ea'
SOURCE_PATH='pictographic-primitives/symbol/strategy_cf25f25b-0432-4d98-b894-c281bc60e8ea.svg'
AUTHOR='gpt-6'

class StrategyPlay(Solo48):
    icon_id='strategy-play'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('strategy', 'plan', 'tactics', 'route', 'game-plan', 'path', 'goal', 'sports')

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

        self.oval('start',10,38,4)
        self.add_line('rise',(10,34),(10,33))
        self.add_arc('turn-l',(10,33),(20,23),radius_x=10)
        self.add_line('middle',(20,23),(28,23))
        self.add_arc('turn-r',(28,23),(38,13),radius_x=10,sweep=False)
        self.add_line('finish',(38,13),(38,6))
        self.add_contour('route','rise','turn-l','middle','turn-r','finish')
        self.relate('connect','start','route')
        self.path('arrow',[(32,12),(38,6),(42,12)]);self.relate('connect','route','arrow')
        for name,cx,cy in [('upper',10,10),('lower',38,38)]:
            self.path(name+'-a',[(cx-4,cy-4),(cx,cy),(cx+4,cy+4)])
            self.path(name+'-b',[(cx-4,cy+4),(cx,cy),(cx+4,cy-4)])
            self.relate('connect',name+'-a',name+'-b')
