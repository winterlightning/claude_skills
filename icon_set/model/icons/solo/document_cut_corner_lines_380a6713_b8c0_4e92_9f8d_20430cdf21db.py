"""Upright document with cut corner and two text lines. Lucide file-text informs the page contour and corner hierarchy; no words or extra furniture added.

SOLO48 VRECT_L; live visible envelope (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='380a6713-b8c0-4e92-9f8d-20430cdf21db'
SOURCE_PATH='pictographic-primitives/symbol/text file_380a6713-b8c0-4e92-9f8d-20430cdf21db.svg'
AUTHOR='gpt-6'

class DocumentCutCornerLines(Solo48):
    icon_id='document-cut-corner-lines'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('document', 'file', 'text', 'page', 'paper', 'note', 'content', 'report')

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

        self.add_line('top',(14,4),(28,4))
        self.add_line('cut',(28,4),(40,16))
        self.add_line('right',(40,16),(40,38))
        self.add_arc('br',(40,38),(34,44),radius_x=6)
        self.add_line('bottom',(34,44),(14,44))
        self.add_arc('bl',(14,44),(8,38),radius_x=6)
        self.add_line('left',(8,38),(8,10))
        self.add_arc('tl',(8,10),(14,4),radius_x=6)
        self.add_contour('page','top','cut','right','br','bottom','bl','left','tl',closed=True)
        for j,y in enumerate([22, 32]):self.add_line('text-'+str(j),(18,y),(28,y))
