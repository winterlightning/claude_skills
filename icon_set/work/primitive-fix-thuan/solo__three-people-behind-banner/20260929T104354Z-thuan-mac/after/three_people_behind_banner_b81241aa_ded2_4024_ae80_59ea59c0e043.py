'Added equal shoulder spans above the banner, with three circular heads and short visible legs.\nOriginal/current comparison: The rejected figures have only posts for torsos, losing the visible shoulders of the original demonstrators.\nPlan: HRECT_L, bounds (2, 6, 46, 42); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/full_body_ref.png: repeated heads and shoulder strokes; 22-(11+3)=8 exact detached gap.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b81241aa-ded2-4024-ae80-59ea59c0e043'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-people-behind-banner/20260929T104354Z-thuan-mac/reference/protester 1_b81241aa-ded2-4024-ae80-59ea59c0e043.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-people-behind-banner'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('three', 'people', 'behind', 'banner')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):arc(n+str(j),a,b,r)
            con(n,*(n+str(j) for j in range(4)),closed=True)
        def path(n,start,steps,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{i}';members.append(m)
                if kind=='L': line(m,here,end)
                elif kind=='A': arc(m,here,end,*args)
                elif kind=='C': bez(m,here,(args[0],args[1],end))
                here=end
            con(n,*members,closed=closed)
        def rect(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad),('L',(r,b-rad)),('A',(r-rad,b),rad),('L',(l+rad,b)),('A',(l,b-rad),rad),('L',(l,t+rad)),('A',(l+rad,t),rad)],True)

        poly('banner',(4,30),(8,30),(24,30),(40,30),(44,30),(44,38),(40,38),(24,38),(8,38),(4,38),closed=True)
        for i,x in enumerate((8,24,40)):
            circle(f'head-{i}',x,11,3)
            line(f'torso-{i}',(x,22),(x,30))
            poly(f'arms-{i}',(x-4,22),(x,22),(x+4,22));join(f'arms-{i}',f'torso-{i}')
            line(f'legs-{i}',(x,38),(x,40));join(f'torso-{i}','banner');join(f'legs-{i}','banner')
            self.mark_human_figure(f'person-{i}',head=f'head-{i}',torso=f'torso-{i}',torso_junction='start')
