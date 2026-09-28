'Alert meerkat facing right, curved back tapering into tail and curved chest. Open lower contour follows reference. Centerline10,4 to38,44.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b4920684-b8a7-4041-8e84-67476dd1c016'
SOURCE_PATH = 'pictographic-primitives/animals/meerkat_b4920684-b8a7-4041-8e84-67476dd1c016.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'No useful local meerkat match; source open back/tail and small snout.'
OMISSIONS = 'No invented eye, paw or closed baseline.'

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
    icon_id = 'meerkat'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('meerkat',)
    def build(self):
        path(self,'back',(10,44),[('C',(18,44),(18,41),(18,36)),('C',(18,24),(23,16),(23,11)),('C',(18,11),(19,7),(23,7)),('C',(23,4),(27,4),(30,4)),('L',(38,5)),('C',(38,11),(31,10),(31,16)),('C',(31,22),(35,23),(34,29))])
