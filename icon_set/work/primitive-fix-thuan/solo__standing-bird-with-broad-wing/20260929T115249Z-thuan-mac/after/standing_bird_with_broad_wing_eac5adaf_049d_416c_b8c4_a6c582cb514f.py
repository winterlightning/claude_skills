"""The current head is squat and the pointed wing dominates the round body. No written feedback. Gave the bird a taller round head and neck, a broad smoothly folded wing and two aligned legs.
Construction: Lucide bird: coherent head/body and a broad folded wing; source supplies long neck and wing arrangement.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'eac5adaf-049d-416c-b8c4-a6c582cb514f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-bird-with-broad-wing/20260929T115249Z-thuan-mac/reference/gamebird_eac5adaf-049d-416c-b8c4-a6c582cb514f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'standing-bird-with-broad-wing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('standing', 'bird', 'with', 'broad', 'wing')
    
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

        path('bird',(6,26),[('C',(25,16),(12,20),(20,16)),('L',(25,13)),('A',(32,6),7),('A',(39,13),7),('L',(42,15)),('L',(38,18)),('C',(26,34),(40,27),(34,34)),('C',(6,26),(18,34),(12,31))],True)
        bez('wing',(25,16),((32,24),(24,30),(6,26)));join('wing','bird')
        for x in (22,32):line('leg'+str(x),(x,34),(x,42));join('leg'+str(x),'bird')
        poly('foot',(20,42),(22,42),(32,42),(36,42));join('foot','leg22','leg32')
