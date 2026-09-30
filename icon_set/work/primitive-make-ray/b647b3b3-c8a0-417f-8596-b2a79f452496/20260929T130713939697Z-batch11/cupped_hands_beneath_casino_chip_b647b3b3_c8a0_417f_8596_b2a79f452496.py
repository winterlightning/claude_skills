'The rejected chip resembles a crosshair and the hands look like prongs.\nSymbol plan: Use a hollow casino-chip ring with four rim ticks above curved cupped palms and inward thumbs.\nConstruction: Shared human hand reference and Lucide hand: open palm curves with natural thumb branches.\nOmissions: Four rim divisions replace eight; omit cuff seams.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b647b3b3-c8a0-417f-8596-b2a79f452496'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cupped-hands-beneath-casino-chip/20260929T125815Z-thuan-mac/reference/casino chip hold_b647b3b3-c8a0-417f-8596-b2a79f452496.svg'
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
    icon_id = 'cupped-hands-beneath-casino-chip'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cupped', 'hands', 'beneath', 'casino', 'chip')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        circle(m,'chip',24,18,12)
        circle(m,'chip-center',24,18,3)
        for name,a,b in [('top',(24,6),(24,15)),('bottom',(24,21),(24,30)),('left',(12,18),(21,18)),('right',(27,18),(36,18))]:
         line(name,a,b);join(name,'chip');join(name,'chip-center')
        for name,sign in [('left-hand',-1),('right-hand',1)]:
         x=lambda a:24+sign*a
         path(m,name,(x(7),42),('C',(x(18),35),(x(7),39),(x(18),40)),('L',(x(18),28)))
         line(name+'-thumb',(x(18),35),(x(12),33));join(name,name+'-thumb')
