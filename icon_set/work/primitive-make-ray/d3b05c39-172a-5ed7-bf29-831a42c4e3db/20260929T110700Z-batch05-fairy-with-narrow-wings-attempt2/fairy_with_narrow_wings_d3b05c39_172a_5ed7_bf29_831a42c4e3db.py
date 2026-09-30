'Enlarged the circular head and replaced the triangular wings with mirrored flowing wing contours.\nOriginal/current comparison: The rejected rigid triangular wings look like a bow tie and the head is undersized relative to the wings.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/full_body_ref.png: circular head and simple body; actual gap 24-(11+5)=8 centerline/4 ink. Mirrored wings follow source fairy silhouette.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd3b05c39-172a-5ed7-bf29-831a42c4e3db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fairy-with-narrow-wings/20260929T110700Z-thuan-mac/reference/fairy_d3b05c39-172a-5ed7-bf29-831a42c4e3db.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fairy-with-narrow-wings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('fairy', 'with', 'narrow', 'wings')

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

        circle('head',24,11,5)
        poly('torso',(24,24),(24,26),(24,34))
        self.mark_human_figure('fairy',head='head',torso='torso-1',torso_junction='start')
        for side,s in [('left',-1),('right',1)]:
            def p(x,y):return (24+s*x,y)
            path('wing-'+side,p(0,26),[('C',p(18,18),p(8,22),p(14,24)),('L',p(18,30)),('C',p(0,26),p(11,31),p(6,28))],True)
            join('wing-'+side,'torso')
        join('wing-left','wing-right')
        poly('skirt',(16,42),(24,34),(32,42),closed=True);join('skirt','torso')
