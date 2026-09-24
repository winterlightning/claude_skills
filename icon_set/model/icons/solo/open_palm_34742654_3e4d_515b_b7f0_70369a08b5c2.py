'Stop palm: four rounded fingers and outward right thumb; shared radius4 and pitch8, smoothly curved lower palm.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '34742654-3e4d-515b-b7f0-70369a08b5c2'
SOURCE_PATH = 'pictographic-primitives/wayfinding/hand stop_34742654-3e4d-515b-b7f0-70369a08b5c2.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide hand: four finger seams and round fingertips; source reversed thumb.'
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
    icon_id = 'open-palm'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('hand', 'stop')
    def build(self):
        class Mirror:
            def __init__(s,icon):s.icon=icon
            def add_line(s,n,a,b):s.icon.add_line(n,(48-a[0],a[1]),(48-b[0],b[1]))
            def add_arc(s,n,a,b,**kw):
                kw['sweep']=not kw.get('sweep',True);s.icon.add_arc(n,(48-a[0],a[1]),(48-b[0],b[1]),**kw)
            def add_bezier(s,n,a,c):s.icon.add_bezier(n,(48-a[0],a[1]),tuple((48-p[0],p[1]) for p in c))
            def add_contour(s,*a,**kw):s.icon.add_contour(*a,**kw)
            def relate(s,*a):s.icon.relate(*a)
        s=Mirror(self)
        
        path(s,'hand',(12,27),[('L',(12,16)),('A',4,4,True,(20,16)),('L',(20,12)),('A',4,4,True,(28,12)),('L',(28,14)),('A',4,4,True,(36,14)),('L',(36,18)),('A',4,4,True,(44,18)),('L',(44,28)),('A',12,12,True,(32,40)),('L',(23,40)),('C',(15,40),(4,32),(4,27)),('C',(4,22),(10,22),(12,27))],True)
        for x,y in [(20,16),(28,14),(36,18)]:
            s.add_line('crease-'+str(x),(x,y),(x,25))
            s.relate('connect','hand','crease-'+str(x))
