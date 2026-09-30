'The rejected face is tiny inside an arch, and the stress marks read as sideways chevrons.\nSymbol plan: Restore a larger circular face, flared bob ends, broad shoulders and two distinct zigzag stress marks.\nConstruction: Shared human bust reference and Lucide user-round: circular jaw with broad shoulders; hair encloses the head naturally.\nOmissions: Reduce three stress marks to two; omit the interior center part and neckline.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9bc95803-ad5e-5ade-9253-3313db652d10'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-with-stress-marks/20260929T125815Z-thuan-mac/reference/user woman stress_9bc95803-ad5e-5ade-9253-3313db652d10.svg'
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
    icon_id = 'woman-with-stress-marks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('woman', 'with', 'stress', 'marks')
    human_construction = 'bust'
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)

        circle(m,'face',24,24,10)
        path(m,'shoulders',(8,44),('A',(40,44),16,6,True));join('face','shoulders')
        line('hair-left',(14,24),(8,30));line('hair-right',(34,24),(40,30))
        join('face','hair-left');join('face','hair-right')
        for name,s in [('left',-1),('right',1)]:
         x=lambda a:24+s*a
         poly('stress-'+name,((x(12),4),(x(16),7),(x(12),10),(x(16),13)))

