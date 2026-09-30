'Restored shoulder spans for all three figures while keeping the raised central podium and symmetric ranking.\nOriginal/current comparison: The rejected winners are reduced to head-and-post marks instead of the people visible in the reference.\nPlan: HRECT_L, bounds (2, 6, 46, 42); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/full_body_ref.png: same-scale circular heads and shoulder strokes; each torso begins 8 below its head outline.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '43ccfd19-3a54-4d74-99c0-89ec49459bcb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-people-on-winners-podium/20260929T104354Z-thuan-mac/reference/ranking people first_43ccfd19-3a54-4d74-99c0-89ec49459bcb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-people-on-winners-podium'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('three', 'people', 'on', 'winners', 'podium')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
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

        poly('podium',(4,32),(7,32),(17,32),(17,26),(24,26),(31,26),(31,32),(41,32),(44,32),(44,40),(4,40),closed=True)
        for i,(x,y,w) in enumerate(((7,17,3),(24,11,4),(41,17,3))):
            circle(f'head-{i}',x,y,3)
            line(f'torso-{i}',(x,y+11),(x,26 if i==1 else 32))
            poly(f'arms-{i}',(x-w,y+11),(x,y+11),(x+w,y+11));join(f'arms-{i}',f'torso-{i}');join(f'torso-{i}','podium')
            self.mark_human_figure(f'person-{i}',head=f'head-{i}',torso=f'torso-{i}',torso_junction='start')
