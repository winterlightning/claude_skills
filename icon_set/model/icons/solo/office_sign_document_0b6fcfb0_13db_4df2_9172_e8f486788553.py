from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0b6fcfb0-13db-4df2-9172-e8f486788553'
SOURCE_PATH = 'icon_set/work/todo-references/office sign document_0b6fcfb0-13db-4df2-9172-e8f486788553.svg'
AUTHOR = 'gpt-6'
# Construction plan: Open document contour and diagonal signing pencil with pointed nib.
# Keyshape visible extremes are supplied by Keyshape.SQUARE.bounds_for(SOLO48).
# Lucide construction reference: notebook-pen.
class Drawing(Solo48):
    icon_id = 'office-sign-document'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('office', 'sign', 'document')
    def build(self):
        self.add_polyline('page',(42,29),(42,42),(6,42),(6,6),(25,6))
        self.add_polyline('pencil',(18,32),(22,21),(35,8),(42,15),(29,28),closed=True)
        self.add_line('ferrule',(29,14),(36,21));self.relate('connect','pencil','ferrule')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, x, y, right, bottom, r=3):
        points=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r),(x+r,y)]
        members=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            part=f'{name}-{i}'
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)

    def cross(self,name,cx,cy,r):
        for suffix,p in [('left',(cx-r,cy)),('right',(cx+r,cy)),('top',(cx,cy-r)),('bottom',(cx,cy+r))]:
            self.add_line(name+'-'+suffix,p,(cx,cy))
        self.relate('connect',*[name+'-'+s for s in ('left','right','top','bottom')])

    def clipboard(self):
        self.box('clip',17,4,31,12,4)
        self.add_polyline('board',(17,8),(8,8),(8,44),(40,44),(40,8),(31,8))
        self.relate('connect','clip','board')


# Visible keyshape extremes: (4, 4, 44, 44).
# Visual review: Document and signing pencil remain recognizable with open space between them; diagonal pencil and open upper-right page edge are intentional.
