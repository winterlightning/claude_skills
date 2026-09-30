'The rejected wedding scene has solid-dot heads, tiny fork bodies and a flattened heart ornament.\nSymbol plan: Use visible circular heads and a taller pointed heart, and separate the groom torso and bride gown under the arch.\nConstruction: human_ref/full_body_ref.png: circular heads and detached bodies. Head bottom26 to body34 =8 centerline units /4 ink.\nOmissions: Arms and gown hem simplified at this scale.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '55e06d00-edc0-4555-a59a-bfe50151ffb9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wedding-couple-heart-arch-scene/20260929T122733Z-thuan-mac/reference/wedding couple_55e06d00-edc0-4555-a59a-bfe50151ffb9.svg'
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
    path(m,n,(x-r,y),('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),closed=True)
def oval(m,n,x,y,rx,ry):
    path(m,n,(x-rx,y),('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True),closed=True)
def box(m,n,l,t,r,b,rad):
    path(m,n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)

class Drawing(Solo48):
    icon_id = 'wedding-couple-heart-arch-scene'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wedding', 'couple', 'heart', 'arch', 'scene')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'heart',(24,10),('C',(16,10),(20,2),(16,6)),('C',(24,15),(16,12),(21,14)),('C',(32,10),(27,14),(32,12)),('C',(24,10),(32,6),(28,2)),closed=True)
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         path(m,'arch'+str(side),p(18,42),('L',p(18,22)),('C',p(8,10),p(18,14),p(14,10)))
         join('arch'+str(side),'heart')
        for name,x in [('groom',17),('bride',31)]:circle(m,name+'-head',x,23,3)
        line('groom-torso',(17,34),(17,38));poly('groom-legs',(14,42),(17,38),(20,42));join('groom-torso','groom-legs')
        poly('groom-arms',(13,34),(17,34),(21,34));join('groom-arms','groom-torso')
        poly('bride-gown',(28,42),(31,34),(34,42))
        m.mark_human_figure('groom',head='groom-head',torso='groom-torso',torso_junction='start')
