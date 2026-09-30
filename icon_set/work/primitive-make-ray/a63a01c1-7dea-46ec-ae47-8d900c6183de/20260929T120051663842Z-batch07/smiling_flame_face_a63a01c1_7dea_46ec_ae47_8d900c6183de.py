"""The current flame has disconnected short upper marks with little upward motion. No written feedback. Restored long flowing outer wisps and an inner curl around the open smiling face.
Construction: Lucide flame: flowing open flame tip; supplied reference owns eyes and open smile.
Plan: VRECT_L SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a63a01c1-7dea-46ec-ae47-8d900c6183de'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-flame-face/20260929T115249Z-thuan-mac/reference/video game mario character_a63a01c1-7dea-46ec-ae47-8d900c6183de.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'smiling-flame-face'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('smiling', 'flame', 'face')
    
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

        path('flame',(16,8),[('C',(8,28),(8,16),(8,21)),('A',(24,44),16,16,False),('A',(40,28),16,16,False),('L',(40,16)),('C',(40,4),(40,10),(37,8))])
        bez('wisp',(26,4),((22,6),(22,10),(22,12)))
        for x in (18,30):self.add_dot('eye'+str(x),(x,18))
        path('mouth',(17,27),[('L',(31,27)),('A',(17,27),7,8,True)],True)
