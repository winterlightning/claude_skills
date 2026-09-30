"""The rejected bob haircut is reduced to two outward ticks and the face has no eyes. No written feedback. Rebuilt a parted rounded hair crown, larger circular jaw, eyes and smile above a broad bust.
Construction: Shared human_ref/user.svg: circular jaw and broad smooth shoulders; the bust uses touching head/body ink. Source supplies facial identity.
Plan: VRECT_L SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b1cd8630-2ca9-4687-b648-01183e12f3af'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-bob-hair-woman-bust/20260929T115249Z-thuan-mac/reference/grandparent_b1cd8630-2ca9-4687-b648-01183e12f3af.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'smiling-bob-hair-woman-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('smiling', 'bob', 'hair', 'woman', 'bust')
    human_construction = "bust"
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

        arc('jaw',(10,18),(38,18),14,14,False)
        path('hair',(10,18),[('C',(18,4),(10,9),(12,4)),('C',(24,9),(21,4),(22,9)),('C',(30,4),(26,9),(27,4)),('C',(38,18),(36,4),(38,9))]);join('jaw','hair')
        for x in (18,30):self.add_dot('eye'+str(x),(x,15))
        bez('smile',(22,23),((23,24),(25,24),(26,23)))
        arc('body-left',(8,44),(24,36),16,8);arc('body-right',(24,36),(40,44),16,8)
        join('jaw','body-left');join('jaw','body-right')
