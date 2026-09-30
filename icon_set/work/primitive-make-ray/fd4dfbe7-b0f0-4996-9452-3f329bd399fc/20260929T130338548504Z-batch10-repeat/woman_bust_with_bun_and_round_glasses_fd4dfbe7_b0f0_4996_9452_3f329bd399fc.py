"""The rejected glasses merged into the face rim. Restore two visibly round lenses, a separate bridge and ample cheek clearance beneath the rounded bun.
Symbol plan: Round lenses use the small circle exception; rounded jaw and shoulders based on human_ref/user.svg, with jaw34 and shoulder38 touching ink.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fd4dfbe7-b0f0-4996-9452-3f329bd399fc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-bust-with-bun-and-round-glasses/20260929T124732Z-thuan-mac/reference/grandma_fd4dfbe7-b0f0-4996-9452-3f329bd399fc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'woman-bust-with-bun-and-round-glasses'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('woman', 'bust', 'with', 'bun', 'and', 'round', 'glasses')
    human_construction = "bust"
    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('hair',(6,20),[('C',(16,12),(6,14),(11,12)),('A',(32,12),8,6,True),('C',(42,20),(37,12),(42,14))])
        line('side-left',(6,20),(6,28));line('side-right',(42,20),(42,28))
        path('jaw',(6,28),[('A',(24,34),18,6,False),('A',(42,28),18,6,False)])
        for n in ('side-left','side-right'):join(n,'hair');join(n,'jaw')
        circle('lens-left',17,20,3);circle('lens-right',31,20,3)
        line('bridge',(20,20),(28,20));join('bridge','lens-left');join('bridge','lens-right')
        path('body',(6,42),[('A',(24,38),18,4,True),('A',(42,42),18,4,True)]);join('jaw','body')
