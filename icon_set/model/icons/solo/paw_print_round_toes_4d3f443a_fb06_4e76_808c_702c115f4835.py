'Paw print: four outlined rounded toes around a broad curved triangular pad. Mirror symmetry about24. Bounds6,6 to42,42.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4d3f443a-fb06-4e76-808c-702c115f4835'
SOURCE_PATH = 'pictographic-primitives/pets/pets allowed_4d3f443a-fb06-4e76-808c-702c115f4835.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide paw-print: four circular toes and smooth central pad.'
OMISSIONS = 'Oval toes replaced by circular outlines for legibility.'

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
    icon_id = 'paw-print-round-toes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('pets', 'allowed')
    def build(self):
        for n,x,y in [('top-left',17,9),('top-right',31,9),('outer-left',9,22),('outer-right',39,22)]:
            circle(self,n,x,y,3)
        path(self,'pad',(24,24),[('C',(28,24),(31,31),(34,34)),('C',(38,40),(32,42),(28,42)),('L',(20,42)),('C',(16,42),(10,40),(14,34)),('C',(17,31),(20,24),(24,24))],True)
