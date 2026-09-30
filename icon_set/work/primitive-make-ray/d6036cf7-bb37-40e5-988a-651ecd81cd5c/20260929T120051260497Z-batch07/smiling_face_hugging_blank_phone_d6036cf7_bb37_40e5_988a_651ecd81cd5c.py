"""The rejected upright phone and short hand mark lose the hugging gesture. No written feedback. Tilted the phone and rebuilt the cheek and forearm as a continuous embracing contour while retaining the happy face.
Construction: Source establishes tilted device and hug. Shared circular facial vocabulary; no useful local smile reference was found.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd6036cf7-bb37-40e5-988a-651ecd81cd5c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-face-hugging-blank-phone/20260929T115249Z-thuan-mac/reference/emoji gaming lover hug iphone_d6036cf7-bb37-40e5-988a-651ecd81cd5c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'smiling-face-hugging-blank-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('smiling', 'face', 'hugging', 'blank', 'phone')
    
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

        path('face-hand',(8,16),[('C',(24,6),(11,9),(17,6)),('C',(42,24),(34,6),(42,14)),('C',(30,42),(42,34),(38,42)),('C',(22,36),(24,42),(22,40)),('C',(30,32),(22,32),(27,32))])
        poly('phone',(6,24),(18,24),(22,36),(24,42),(12,42),closed=True);join('phone','face-hand')
        for x in (20,30):self.add_dot('eye'+str(x),(x,16))
        bez('smile',(27,25),((29,27),(31,27),(33,24)))
