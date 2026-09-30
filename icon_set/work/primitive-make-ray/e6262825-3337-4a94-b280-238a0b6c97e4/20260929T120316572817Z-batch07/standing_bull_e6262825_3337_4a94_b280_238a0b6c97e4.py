"""The current bull has a triangular muzzle and tiny uneven horns. No written feedback. Rounded the shoulders and muzzle, widened the body and rebuilt two rising horns above the head; far legs and facial marks are omitted.
Construction: No useful local bull profile; source supplies broad body, lowered muzzle and paired horns.
Plan: HRECT_L SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e6262825-3337-4a94-b280-238a0b6c97e4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-bull/20260929T115249Z-thuan-mac/reference/livestock bull body_e6262825-3337-4a94-b280-238a0b6c97e4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'standing-bull'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('standing', 'bull')
    
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

        path('bull',(4,40),[('L',(4,26)),('A',(14,16),10),('L',(28,16)),('C',(34,12),(28,12),(32,12)),('C',(44,24),(38,12),(42,20)),('L',(37,24)),('C',(30,33),(34,24),(34,30)),('L',(30,40)),('L',(22,40)),('L',(22,31)),('L',(12,31)),('L',(12,40))])
        bez('horn-left',(28,16),((25,14),(25,10),(27,8)))
        bez('horn-right',(34,12),((39,14),(41,11),(40,8)))
        join('bull','horn-left','horn-right')
