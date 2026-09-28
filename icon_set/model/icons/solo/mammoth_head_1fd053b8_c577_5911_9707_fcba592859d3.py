'Mammoth profile: high domed head, upturned crescent tusk and downward curling trunk. Bounds 6,6 to42,42.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1fd053b8-c577-5911-9707-fcba592859d3'
SOURCE_PATH = 'pictographic-primitives/animals/mammoth elephant_1fd053b8-c577-5911-9707-fcba592859d3.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'No useful local mammoth match; source crescent tusk and domed head.'
OMISSIONS = 'Eye omitted as absent in reference.'

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
    icon_id = 'mammoth-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('mammoth', 'elephant')
    def build(self):
        path(self,'head',(20,25),[('C',(22,13),(25,6),(32,6)),('C',(38,6),(42,12),(42,20)),('L',(42,42))])
        path(self,'tusk',(6,20),[('C',(6,29),(13,34),(22,33)),('C',(25,32),(28,28),(30,24)),('C',(27,23),(23,25),(20,25)),('C',(14,26),(9,24),(6,20))],True)
        path(self,'trunk',(30,24),[('C',(31,30),(28,38),(21,42)),('L',(14,38)),('C',(20,36),(21,34),(22,33))])
        self.relate('connect','tusk','trunk')
        self.relate('connect','head','tusk')
