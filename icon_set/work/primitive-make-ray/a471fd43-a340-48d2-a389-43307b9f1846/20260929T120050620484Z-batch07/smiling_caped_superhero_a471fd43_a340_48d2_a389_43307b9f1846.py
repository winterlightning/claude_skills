"""The current superhero has a blank small head and a generic arched body. No written feedback. Enlarged the head to restore a smile and rebuilt angular cape shoulders with a simple chest chevron; tiny eyes and the enclosed emblem are omitted for spacing.
Construction: Shared human_ref/user.svg: circular jaw and broad smooth shoulders; the bust uses touching head/body ink. Source supplies facial identity.
Plan: VRECT_L SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a471fd43-a340-48d2-a389-43307b9f1846'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-caped-superhero/20260929T115249Z-thuan-mac/reference/superman_a471fd43-a340-48d2-a389-43307b9f1846.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'smiling-caped-superhero'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('smiling', 'caped', 'superhero')
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

        circle('head',24,14,10)
        bez('smile',(22,14),((23,16),(25,16),(26,14)))
        path('body',(8,44),[('L',(8,38)),('C',(24,28),(8,31),(17,28)),('C',(40,38),(31,28),(40,31)),('L',(40,44))]);join('head','body')
        poly('emblem',(20,38),(24,42),(28,38))
