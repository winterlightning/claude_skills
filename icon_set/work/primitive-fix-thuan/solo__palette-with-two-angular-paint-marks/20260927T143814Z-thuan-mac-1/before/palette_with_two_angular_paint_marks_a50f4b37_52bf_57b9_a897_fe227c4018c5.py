'Kidney-shaped artist palette with round thumb hole and two open angular paint daubs. Bounds6,6 to42,42.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a50f4b37-52bf-57b9-a897-fe227c4018c5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color palette sample_a50f4b37-52bf-57b9-a897-fe227c4018c5.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide palette: coherent kidney contour with isolated paint marks.'
OMISSIONS = 'Closed paint patches reduced to open angular daubs because two closed patches plus a thumb hole cannot retain the required clearance.'

def path(s,n,p,cs,closed=False):
    ids=[]
    for j,c in enumerate(cs):
        eid=f'{n}-{j}';q=c[-1]
        if c[0]=='L':s.add_line(eid,p,q)
        elif c[0]=='A':s.add_arc(eid,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
        elif c[0]=='C':s.add_bezier(eid,p,(c[1],c[2],q))
        ids.append(eid);p=q
    s.add_contour(n,*ids,closed=closed)
def circle(s,n,x,y,r):
    path(s,n,(x-r,y),[('A',r,r,True,(x+r,y)),('A',r,r,True,(x-r,y))],True)

class Drawing(Solo48):
    icon_id = 'palette-with-two-angular-paint-marks'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('color', 'palette', 'sample')
    def build(self):
        path(self,'palette',(24,6),[('C',(35,6),(42,10),(42,18)),('C',(42,23),(36,23),(36,27)),('C',(36,31),(42,30),(42,34)),('C',(42,39),(34,42),(24,42)),('A',18,18,True,(6,24)),('A',18,18,True,(24,6))],True)
        circle(self,'thumb',29,17,2)
        self.add_polyline('paint-top',(18,17),(16,21),(19,21))
        self.add_polyline('paint-bottom',(19,29),(19,32),(23,32))
