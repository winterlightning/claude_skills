'Three outlined smoke puffs over a broad pointed flame, smooth base and two tongues. Extremes6,6 to42,42.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e169ce75-2425-4df4-8390-e71be7ca6c54'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/wildfire_e169ce75-2425-4df4-8390-e71be7ca6c54.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide flame: pointed tongue flowing into round lower bowl.'
OMISSIONS = 'Inner flame omitted to retain clearance; all three smoke puffs retained.'

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
    icon_id = 'open-flame-with-three-rounded-smoke-puffs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/ecology'
    aliases = ()
    keywords = ('wildfire',)
    def build(self):
        circle(self,'smoke-left',9,18,3)
        circle(self,'smoke-middle',21,9,3)
        circle(self,'smoke-right',38,11,4)
        path(self,'flame',(20,21),[('C',(29,25),(28,31),(30,32)),('L',(35,26)),('C',(41,34),(42,42),(26,42)),('C',(9,42),(8,37),(13,29)),('L',(17,33)),('C',(21,29),(21,25),(20,21))],True)
