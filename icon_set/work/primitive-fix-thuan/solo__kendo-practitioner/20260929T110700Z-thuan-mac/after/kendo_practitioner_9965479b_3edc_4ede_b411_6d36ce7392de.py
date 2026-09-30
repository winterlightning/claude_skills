'Reduced the head and lengthened the robe, retaining the two-handed sword junction and split lower garment.\nOriginal/current comparison: The rejected oversized head and short triangular robe make the practitioner look like a bust rather than the full martial artist in the reference.\nPlan: VRECT_L, bounds (6, 2, 42, 46); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/full_body_ref.png: circular head and coherent body; actual detached gap 24-(10+6)=8 centerline/4 ink. Fine helmet band omitted to restore full-body proportions.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9965479b-3edc-4ede-b411-6d36ce7392de'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kendo-practitioner/20260929T110700Z-thuan-mac/reference/kendo_9965479b-3edc-4ede-b411-6d36ce7392de.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kendo-practitioner'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('kendo', 'practitioner')

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

        circle('head',18,10,6)
        bez('torso',(18,24),((18,28),(21,30),(24,30)))
        poly('robe',(24,30),(30,30),(34,44),(22,44),(8,44),(10,30),(18,24));join('torso','robe')
        line('robe-split',(22,44),(22,36));join('robe-split','robe')
        line('sword',(24,30),(40,14));join('sword','torso');join('sword','robe')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
