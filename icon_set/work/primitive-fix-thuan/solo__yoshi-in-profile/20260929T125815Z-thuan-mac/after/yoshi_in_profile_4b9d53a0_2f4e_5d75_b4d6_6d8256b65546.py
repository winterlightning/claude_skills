'The rejected dinosaur has a blocky foot and loses the forward arm and curved back of Yoshi.\nSymbol plan: Round the muzzle, belly and forward foot, with a clear curved back and upturned tail.\nConstruction: No useful Lucide match; asymmetric coherent silhouette preserves the character profile.\nOmissions: Omit tiny facial marks, saddle inset and small arm to keep the compact silhouette open.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4b9d53a0-2f4e-5d75-b4d6-6d8256b65546'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__yoshi-in-profile/20260929T125815Z-thuan-mac/reference/mario yoshi_4b9d53a0-2f4e-5d75-b4d6-6d8256b65546.svg'
AUTHOR = 'gpt-6'

def path(m,n,start,*steps,closed=False):
    names=[]; here=start
    for j,(kind,end,*args) in enumerate(steps):
        k=f'{n}-{j}'
        if kind=='L':m.add_line(k,here,end)
        elif kind=='C':m.add_bezier(k,here,(args[0],args[1],end))
        elif kind=='A':m.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
        names.append(k);here=end
    m.add_contour(n,*names,closed=closed)
def circle(m,n,x,y,r):
    path(m,n,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)
def oval(m,n,x,y,rx,ry):
    path(m,n,(x-rx,y),('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True),closed=True)
def box(m,n,l,t,r,b,rad):
    path(m,n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)

class Drawing(Solo48):
    icon_id = 'yoshi-in-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('yoshi', 'in', 'profile')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'body',(20,14),('L',(20,10)),('A',(28,10),4,4,True),('L',(34,10)),('A',(42,18),8,8,True),('A',(34,26),8,8,True),('L',(29,25)),('C',(27,34),(27,27),(26,31)),('C',(34,38),(31,34),(34,35)),('A',(30,42),4,4,True),('L',(18,42)),('L',(18,36)),('C',(6,24),(10,36),(6,30)),('L',(17,28)),('C',(16,20),(14,26),(13,22)),('C',(20,14),(18,20),(20,18)),closed=True)
