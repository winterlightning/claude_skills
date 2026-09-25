'Side cutaway of an open mouth: upper lip, two teeth, tongue and lower jaw. Bounds6,6 to42,42.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '83188d0d-6fe1-57ec-8f6f-153a95690e91'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-mouth-in-side-section-83188d0d/20260924T093935Z-thuan-mac/reference/mouthwash teeth_83188d0d-6fe1-57ec-8f6f-153a95690e91.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Human source side section; no useful Lucide match.'
OMISSIONS = 'Two teeth merged to broad dental edge; no lower neck.'

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
    icon_id = 'open-mouth-in-side-section-83188d0d-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('mouthwash', 'teeth')
    def build(self):
        path(self,'upper',(6,6),[('C',(6,12),(13,14),(18,14)),('L',(26,14)),('C',(36,14),(36,23),(34,27))])
        path(self,'teeth',(14,14),[('L',(14,22)),('L',(26,22)),('L',(26,14))])
        self.relate('connect','upper','teeth')
        path(self,'tongue',(12,34),[('C',(16,25),(23,33),(27,29)),('C',(29,27),(31,25),(34,27))])
        path(self,'jaw',(12,34),[('L',(12,38)),('A',4,4,False,(16,42)),('L',(32,42)),('A',10,10,False,(42,32)),('L',(42,25))])
        self.relate('connect','upper','tongue');self.relate('connect','tongue','jaw')
