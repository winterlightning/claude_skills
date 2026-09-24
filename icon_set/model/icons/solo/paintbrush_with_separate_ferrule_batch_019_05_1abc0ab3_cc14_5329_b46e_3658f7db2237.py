'Diagonal artist brush: round-ended handle, ferrule band and soft pointed bristles. Centerline6,6 to42,42.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1abc0ab3-cc14-5329-b46e-3658f7db2237'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/brush_1abc0ab3-cc14-5329-b46e-3658f7db2237.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide paintbrush: distinct ferrule and flowing bristle outline; source round handle.'
OMISSIONS = 'None'

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
    icon_id = 'paintbrush-with-separate-ferrule-batch-019-05'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('brush',)
    def build(self):
        path(self,'handle',(22,20),[('L',(32,8)),('C',(33,7),(35,6),(36,6)),('A',6,6,True,(42,12)),('C',(42,14),(41,16),(39,18)),('L',(30,28))])
        path(self,'ferrule',(22,20),[('L',(14,28)),('L',(22,36)),('L',(30,28)),('L',(22,20))],True)
        self.relate('connect','handle','ferrule')
        path(self,'bristles',(14,28),[('C',(7,28),(8,35),(6,42)),('C',(14,42),(20,42),(22,36))])
        self.relate('connect','bristles','ferrule')
