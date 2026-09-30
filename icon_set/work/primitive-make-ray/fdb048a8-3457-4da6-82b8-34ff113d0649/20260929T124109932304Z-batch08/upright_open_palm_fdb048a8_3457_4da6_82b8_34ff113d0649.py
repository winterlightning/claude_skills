'The rejected palm ends in a broad curved bowl and an arbitrary gap instead of a wrist.\nSymbol plan: Restore two upright wrist sides below the palm, preserving four unequal rounded fingers and the outward thumb.\nConstruction: Lucide hand original and atomic-debug: four rounded fingertips and shared finger creases. Human reference supplies simple anatomy.\nOmissions: Palm crease omitted to preserve finger-to-palm clearance.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fdb048a8-3457-4da6-82b8-34ff113d0649'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__upright-open-palm/20260929T122733Z-thuan-mac/reference/palm_fdb048a8-3457-4da6-82b8-34ff113d0649.svg'
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
    icon_id = 'upright-open-palm'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('upright', 'open', 'palm')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        heights=(14,12,14,20);members=[]
        for i,y in enumerate(heights):
         x=12+i*8
         if i==0:line('rise',(12,28),(12,y));members.append('rise')
         else:line('rise'+str(i),(x,heights[i-1]),(x,y));members.append('rise'+str(i))
         m.add_arc('tip'+str(i),(x,y),(x+8,y),radius_x=4);members.append('tip'+str(i))
        line('side',(44,20),(44,28));m.add_bezier('right-palm',(44,28),((44,34),(36,34),(36,40)))
        m.add_contour('fingers',*members,'side','right-palm')
        path(m,'left-palm',(20,40),('C',(12,36),(20,38),(16,40)),('L',(4,26)),('C',(12,28),(4,18),(8,22)))
        join('left-palm','fingers')
        for i,end in enumerate((24,24,26)):
         x=20+i*8;line('crease'+str(i),(x,max(heights[i],heights[i+1])),(x,end));join('crease'+str(i),'fingers')
