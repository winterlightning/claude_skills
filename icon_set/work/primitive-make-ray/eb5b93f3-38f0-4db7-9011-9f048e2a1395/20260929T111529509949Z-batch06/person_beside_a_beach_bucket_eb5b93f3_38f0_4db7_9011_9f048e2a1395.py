"""The rejected person is striding and holding the bucket, while the reference shows a standing person beside it. No written feedback. Restored a stationary figure and separated the tapered beach bucket from the arms.
Construction: Human full_body_ref.png: circular head, coherent limbs, exact 4-unit ink gap.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'eb5b93f3-38f0-4db7-9011-9f048e2a1395'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-beside-a-beach-bucket/20260929T110914Z-thuan-mac/reference/beach swim_eb5b93f3-38f0-4db7-9011-9f048e2a1395.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'person-beside-a-beach-bucket'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'beside', 'a', 'beach', 'bucket')
    
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

        circle('head',32,11,5)
        line('torso',(32,24),(32,33))
        poly('arms',(23,28),(26,24),(32,24),(38,24),(42,28));join('arms','torso')
        poly('legs',(27,42),(32,33),(37,42));join('legs','torso')
        poly('bucket',(6,32),(8,42),(16,42),(18,32),(6,32))
        arc('handle',(6,32),(18,32),6,8);join('bucket','handle')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
