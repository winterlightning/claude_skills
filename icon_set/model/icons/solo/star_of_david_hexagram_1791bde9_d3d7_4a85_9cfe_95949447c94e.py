"""Two interlocking triangles form a Star of David. No local Lucide hexagram match; shared crossing nodes and reflection preserve its six-point geometry. Tiny source tip notch omitted.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='1791bde9-d3d7-4a85-9cfe-95949447c94e'
SOURCE_PATH='pictographic-primitives/symbol/star of david_1791bde9-d3d7-4a85-9cfe-95949447c94e.svg'
AUTHOR='gpt-6'

class StarOfDavidHexagram(Solo48):
    icon_id='star-of-david-hexagram'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('star-of-david', 'judaism', 'jewish', 'hexagram', 'religion', 'israel', 'faith', 'symbol')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.path('up',[(24,6),(30,15),(36,24),(42,33),(30,33),(18,33),(6,33),(12,24),(18,15)],True)
        self.path('down',[(6,15),(18,15),(30,15),(42,15),(36,24),(30,33),(24,42),(18,33),(12,24)],True)
        self.relate('connect','up','down')
