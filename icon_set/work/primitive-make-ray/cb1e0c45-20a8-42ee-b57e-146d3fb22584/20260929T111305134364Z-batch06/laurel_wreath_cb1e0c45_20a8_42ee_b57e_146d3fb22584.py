"""The current wreath has only two bulky loops per branch, losing the laurel leaf rhythm. No written feedback. Rebuilt paired curved branches with three tapered leaves each and crossed stems; reduced the source leaf count for native readability.
Construction: Lucide sprout: pointed leaves and curved stems; mirrored branches.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cb1e0c45-20a8-42ee-b57e-146d3fb22584'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__laurel-wreath/20260929T110914Z-thuan-mac/reference/laurel wreath_cb1e0c45-20a8-42ee-b57e-146d3fb22584.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'laurel-wreath'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('laurel', 'wreath')
    
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

        for side in (-1,1):
         def p(x,y):return (24+side*(x-24),y)
         # Each branch owns three consistently pointed leaf contours.
         bez(f'branch{side}',p(14,6),(p(7,17),p(9,31),p(27,42)))
         for j,(a,c1,c2,b) in enumerate([((14,6),(6,6),(6,15),(10,18)),((10,18),(6,20),(6,29),(14,30)),((14,30),(13,38),(19,38),(23,39))]):
          n=f'leaf{side}-{j}'
          bez(n,p(*a),(p(*c1),p(*c2),p(*b)))
          join(n,f'branch{side}')
        join('branch-1','branch1')
