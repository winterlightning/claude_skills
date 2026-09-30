"""The rejected grapes are six isolated tiny rings. No written feedback. Rebuilt a connected six-berry bunch with larger circular upper berries, rounded lower lobes and a forked stem; no berry is dropped.
Construction: Lucide grape: connected berry cluster and a curved stem; source supplies the 3/2/1 grouping.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '595ebb35-2692-477a-a87b-7507db3ad2a5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__six-grape-bunch/20260929T115249Z-thuan-mac/reference/grape_595ebb35-2692-477a-a87b-7507db3ad2a5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'six-grape-bunch'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('six', 'grape', 'bunch')
    
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*ps,closed=False): self.add_polyline(n,*ps,closed=closed)
        def bez(n,a,*ss): self.add_bezier(n,a,*ss)
        def arc(n,a,b,rx,ry=None,s=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=s)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'a',n+'b',closed=True)
        def path(n,a,commands,closed=False):
            members=[]
            for j,c in enumerate(commands):
                k,b,*args=c; name=n+str(j)
                if k=='L': line(name,a,b)
                elif k=='A': arc(name,a,b,*args)
                elif k=='C': bez(name,a,(args[0],args[1],b))
                members.append(name);a=b
            self.add_contour(n,*members,closed=closed)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r),('L',(x+r,y+h)),('A',(x,y+h-r),r),('L',(x,y+r)),('A',(x+r,y),r)],True)
        def join(*ns): self.relate('connect',*ns)

        for j,x in enumerate((12,24,36)):circle('grape'+str(j),x,22,6)
        join('grape0','grape1');join('grape1','grape2')
        arc('lower-left',(24,28),(12,28),6,7)
        arc('lower-right',(36,28),(24,28),6,7)
        join('lower-left','grape0','grape1');join('lower-right','grape1','grape2')
        arc('bottom',(30,35),(18,35),6,7)
        join('bottom','lower-left','lower-right')
        path('stem',(24,16),[('L',(24,12)),('C',(16,6),(24,8),(20,6))]);join('stem','grape1')
        bez('stem-right',(24,12),((24,8),(28,6),(32,6)));join('stem-right','stem')
