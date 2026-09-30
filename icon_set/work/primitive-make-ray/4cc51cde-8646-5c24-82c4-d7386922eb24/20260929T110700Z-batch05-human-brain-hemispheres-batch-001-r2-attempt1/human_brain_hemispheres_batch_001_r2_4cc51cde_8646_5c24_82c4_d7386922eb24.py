'Broadened the paired hemispheres and restored three distinct outer lobes around a centered fissure.\nOriginal/current comparison: The rejected narrow hemispheres resemble two capsules and lose the original scalloped brain outline.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide brain original and atomic-debug: mirrored lobes, central fissure and distinct outer scallops. Fine folds omitted for native-size clarity.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4cc51cde-8646-5c24-82c4-d7386922eb24'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__human-brain-hemispheres-batch-001-r2/20260929T110700Z-thuan-mac/reference/brain_4cc51cde-8646-5c24-82c4-d7386922eb24.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'human-brain-hemispheres-batch-001-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('human', 'brain', 'hemispheres', 'batch', '001', 'r2')

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

        for side,s in [('left',-1),('right',1)]:
            def p(x,y):return (24+s*x,y)
            bez(side,p(0,14),
                (p(0,8),p(5,6),p(10,6)),
                (p(14,6),p(16,10),p(14,14)),
                (p(18,14),p(18,19),p(18,24)),
                (p(18,29),p(16,32),p(14,32)),
                (p(16,38),p(12,42),p(8,42)),
                (p(4,42),p(0,38),p(0,34)))
        line('fissure',(24,14),(24,34));join('left','right');join('left','fissure');join('right','fissure')
