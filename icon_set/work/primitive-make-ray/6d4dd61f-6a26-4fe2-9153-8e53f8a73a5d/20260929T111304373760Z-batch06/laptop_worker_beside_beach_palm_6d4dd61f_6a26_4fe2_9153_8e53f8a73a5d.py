"""The rejected palm is a Y and the person is only a detached shoulder arc. No written feedback. Added a third drooping frond, a curved trunk, and a clearer seated upper body beside a tilted laptop; omitted the screen logo and waves.
Construction: Human full_body_ref.png: round head and 4-unit detached gap. Lucide laptop: simple panel.
Plan: HRECT_L SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6d4dd61f-6a26-4fe2-9153-8e53f8a73a5d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__laptop-worker-beside-beach-palm/20260929T110914Z-thuan-mac/reference/digital nomad beach_6d4dd61f-6a26-4fe2-9153-8e53f8a73a5d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'laptop-worker-beside-beach-palm'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('laptop', 'worker', 'beside', 'beach', 'palm')
    
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

        circle('head',34,13,5)
        bez('torso',(34,26),((40,26),(44,33),(44,40)))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        poly('laptop',(4,30),(23,30),(27,40),(8,40),closed=True)
        bez('frond-left',(4,8),((8,8),(11,9),(13,13)))
        bez('frond-right',(13,13),((16,8),(19,8),(21,8)))
        bez('frond-down',(13,13),((18,13),(21,17),(21,20)))
        bez('trunk',(13,13),((10,17),(10,20),(10,22)))
        join('frond-left','frond-right','frond-down','trunk')
