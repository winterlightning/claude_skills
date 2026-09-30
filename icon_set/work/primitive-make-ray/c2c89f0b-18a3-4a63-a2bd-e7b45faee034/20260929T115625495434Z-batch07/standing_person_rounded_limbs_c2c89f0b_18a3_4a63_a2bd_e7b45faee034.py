"""The rejected figure has sharp elbows and widely splayed legs, unlike the still reference. No written feedback. Rebuilt smooth hanging arms and two parallel standing legs around a simple torso.
Construction: Shared human full_body_ref.png: round head and coherent limbs; head bottom16 to neck24 gives exact 4-unit ink gap.
Plan: VRECT_L SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c2c89f0b-18a3-4a63-a2bd-e7b45faee034'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-person-rounded-limbs/20260929T115249Z-thuan-mac/reference/omnivore_c2c89f0b-18a3-4a63-a2bd-e7b45faee034.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'standing-person-rounded-limbs'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('standing', 'person', 'rounded', 'limbs')
    
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

        circle('head',24,10,6)
        line('torso',(24,24),(24,32))
        bez('arms',(8,33),((8,27),(14,24),(24,24)),((34,24),(40,27),(40,33)));join('arms','torso')
        path('legs',(18,44),[('L',(18,36)),('A',(24,32),6,4,True),('A',(30,36),6,4,True),('L',(30,44))]);join('torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
