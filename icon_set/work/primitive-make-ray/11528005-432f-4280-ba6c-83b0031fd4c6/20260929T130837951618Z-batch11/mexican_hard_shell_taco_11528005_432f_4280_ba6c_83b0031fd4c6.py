'The rejected taco shell is too narrow and reads as a leaf rather than a broad half-round shell.\nSymbol plan: Broaden the diagonal shell into a substantial semicircle and keep a scalloped filling edge.\nConstruction: Lucide sandwich informs separate shell and filling owners sharing real endpoints; diagonal orientation follows the reference.\nOmissions: Reduce filling lobes to three large scallops.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '11528005-432f-4280-ba6c-83b0031fd4c6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mexican-hard-shell-taco/20260929T125815Z-thuan-mac/reference/tacos_11528005-432f-4280-ba6c-83b0031fd4c6.svg'
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
    icon_id = 'mexican-hard-shell-taco'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('mexican', 'hard', 'shell', 'taco')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'shell',(16,42),('C',(14,20),(8,36),(8,28)),('C',(42,16),(22,10),(34,8)),('L',(16,42)),closed=True)
        path(m,'filling',(16,42),('C',(6,32),(7,43),(6,38)),('C',(10,18),(6,25),(6,20)),('C',(22,6),(8,10),(15,6)),('C',(34,10),(28,6),(31,6)),('C',(42,16),(39,9),(42,12)))
        join('shell','filling')
