'The rejected cleaver blade is a square diamond and its hanging hole is a filled central dot.\nSymbol plan: Elongate the blade, move the hollow hanging hole toward the tip and round the diagonal handle.\nConstruction: Lucide axe informs a broad blade and narrower handle with shared corners.\nOmissions: Omit tiny handle rivet.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cfcfcb82-64f9-4889-b3e8-32939823d9d7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-cleaver-with-hanging-hole/20260929T125815Z-thuan-mac/reference/chops_cfcfcb82-64f9-4889-b3e8-32939823d9d7.svg'
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
    icon_id = 'diagonal-cleaver-with-hanging-hole'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('diagonal', 'cleaver', 'with', 'hanging', 'hole')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)

        poly('blade',((27,6),(42,21),(25,38),(10,23),(27,6)))
        path(m,'handle',(14,27),('L',(6,35)),('L',(6,38)),('A',(10,42),4,4,False),('L',(13,42)),('L',(22,35)))
        join('handle','blade')
        circle(m,'hole',26,22,3)

