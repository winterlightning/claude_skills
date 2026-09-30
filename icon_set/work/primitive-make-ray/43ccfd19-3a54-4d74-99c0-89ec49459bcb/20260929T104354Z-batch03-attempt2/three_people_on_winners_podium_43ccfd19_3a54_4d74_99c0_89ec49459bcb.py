'Restored shoulder spans for all three figures while keeping the raised central podium and symmetric ranking.\nOriginal/current comparison: The rejected winners are reduced to head-and-post marks instead of the people visible in the reference.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/full_body_ref.png: same-scale circular heads and shoulder strokes; each torso begins 8 below its head outline.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '43ccfd19-3a54-4d74-99c0-89ec49459bcb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-people-on-winners-podium/20260929T104354Z-thuan-mac/reference/ranking people first_43ccfd19-3a54-4d74-99c0-89ec49459bcb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-people-on-winners-podium'
    keyshape = Keyshape.SQUARE
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

        poly('podium',(6,32),(9,32),(18,32),(18,28),(24,28),(30,28),(30,32),(39,32),(42,32),(42,42),(6,42),closed=True)
        for i,(x,y,w) in enumerate(((9,13,3),(24,9,4),(39,13,3))):
            circle(f'head-{i}',x,y,3)
            line(f'torso-{i}',(x,y+11),(x,28 if i==1 else 32))
            poly(f'arms-{i}',(x-w,y+11),(x,y+11),(x+w,y+11));join(f'arms-{i}',f'torso-{i}');join(f'torso-{i}','podium')
            self.mark_human_figure(f'person-{i}',head=f'head-{i}',torso=f'torso-{i}',torso_junction='start')
