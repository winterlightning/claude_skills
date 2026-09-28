'Angled painting applicator and detached winding paint stroke. One broad band between barrel and pointed tip. Centerline6,6 to42,42.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b06e64f7-64ba-40ee-b75d-72b9fb3f5a30'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__paint-applicator-with-wavy-stroke/20260927T143814Z-thuan-mac-1/reference/tube painting_b06e64f7-64ba-40ee-b75d-72b9fb3f5a30.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide paintbrush: distinct handle and bristle regions; source wavy paint.'
OMISSIONS = 'Top barrel seam omitted to open space.'

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
    icon_id = 'paint-applicator-with-wavy-stroke'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('tube', 'painting')
    def build(self):
        path(self,'tool',(30,6),[('L',(42,10)),('L',(34,30)),('C',(30,36),(26,40),(23,42)),('C',(21,36),(21,31),(22,26)),('L',(30,6))],True)
        self.add_line('ferrule',(22,26),(34,30));self.relate('connect','tool','ferrule')
        path(self,'paint',(13,12),[('C',(8,11),(6,12),(6,18)),('C',(6,22),(13,22),(13,27)),('C',(13,31),(6,31),(6,36)),('C',(6,39),(9,40),(13,40))])

# Revision comparison: The rejected marker point and paint wave were too cramped to read as an active applicator.
# Revision: Opened the pointed applicator and drew a more deliberate winding paint stroke.
