"""The rejected knives are bare rods and the block reads as a quarter circle. No written feedback. Restored two outlined handles with diagonal placement and a broad sloping block; omitted wood grain.
Construction: No useful exact Lucide match; reference composition and geometric construction.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '00074a61-3ed9-40d1-8059-4735820ac11b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__knife-block-two-knives/20260929T110914Z-thuan-mac/reference/knives set_00074a61-3ed9-40d1-8059-4735820ac11b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'knife-block-two-knives'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('knife', 'block', 'two', 'knives')
    
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

        poly('block',(6,24),(15,26),(24,28),(33,30),(42,32),(42,42),(6,42),closed=True)
        path('left-handle',(6,24),[('L',(18,8)),('A',(26,14),5),('L',(15,26))]);join('left-handle','block')
        path('right-handle',(24,28),[('L',(33,16)),('A',(41,22),5),('L',(33,30))]);join('right-handle','block')
