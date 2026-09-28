"""Rounded square document with three descending text lines. Lucide file-text informs tangent page corners and repeated horizontal spacing; source has no folded corner.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='4121a762-5d64-4b1b-8992-24f234b162ec'
SOURCE_PATH='pictographic-primitives/symbol/text file 1_4121a762-5d64-4b1b-8992-24f234b162ec.svg'
AUTHOR='gpt-6'

class TextDocumentSquare(Solo48):
    icon_id='text-document-square'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('text', 'document', 'note', 'page', 'file', 'content', 'paragraph', 'notes')

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

        lo,hi,r=6,42,6
        self.add_line('top',(lo+r,lo),(hi-r,lo));self.add_arc('tr',(hi-r,lo),(hi,lo+r),radius_x=r)
        self.add_line('right',(hi,lo+r),(hi,hi-r));self.add_arc('br',(hi,hi-r),(hi-r,hi),radius_x=r)
        self.add_line('base',(hi-r,hi),(lo+r,hi));self.add_arc('bl',(lo+r,hi),(lo,hi-r),radius_x=r)
        self.add_line('left',(lo,hi-r),(lo,lo+r));self.add_arc('tl',(lo,lo+r),(lo+r,lo),radius_x=r)
        self.add_contour('page','top','tr','right','br','base','bl','left','tl',closed=True)
        for j,(y,end) in enumerate([(16,32),(24,27),(32,22)]):self.add_line('text-'+str(j),(16,y),(end,y))
