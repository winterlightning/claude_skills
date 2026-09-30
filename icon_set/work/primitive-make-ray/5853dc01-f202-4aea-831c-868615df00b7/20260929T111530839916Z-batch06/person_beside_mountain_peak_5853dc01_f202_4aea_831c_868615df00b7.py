"""The current mountain is a plain triangle and the short figure has pointed arms. No written feedback. Restored a jagged mountain ridge and smoother hanging arms, keeping a full standing figure.
Construction: Lucide mountain: recognizable uneven alpine ridge. Human full_body_ref.png: round head and coherent limbs with 4-unit ink gap.
Plan: HRECT_L SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5853dc01-f202-4aea-831c-868615df00b7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-beside-mountain-peak/20260929T110914Z-thuan-mac/reference/camping trekking 1_5853dc01-f202-4aea-831c-868615df00b7.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'person-beside-mountain-peak'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'beside', 'mountain', 'peak')
    
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

        circle('head',10,12,4)
        line('torso',(10,24),(10,32))
        bez('arms',(4,30),((4,27),(7,24),(10,24)),((13,24),(16,27),(16,30)));join('arms','torso')
        poly('legs',(6,40),(10,32),(14,40));join('legs','torso')
        poly('mountain',(24,40),(32,19),(37,28),(40,24),(44,40),closed=True)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
