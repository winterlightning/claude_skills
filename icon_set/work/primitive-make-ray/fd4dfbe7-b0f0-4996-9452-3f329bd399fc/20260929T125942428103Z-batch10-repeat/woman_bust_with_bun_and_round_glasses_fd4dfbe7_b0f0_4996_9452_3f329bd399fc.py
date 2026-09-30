"""The rejected glasses merged into the face rim. Restore two small round lenses, a distinct bridge and cheek clearances beneath the bun; retain a circular lower jaw and touching shoulders.
Symbol plan: human_ref/user.svg circular jaw and broad shoulders; radius15 lower jaw has bottom37, shoulders41, so ink touches. Small lens circles follow the contract exception.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fd4dfbe7-b0f0-4996-9452-3f329bd399fc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-bust-with-bun-and-round-glasses/20260929T124732Z-thuan-mac/reference/grandma_fd4dfbe7-b0f0-4996-9452-3f329bd399fc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'woman-bust-with-bun-and-round-glasses'
    keyshape = Keyshape.VRECT_L
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

        path('hair',(8,16),[('C',(16,10),(8,12),(12,10)),('A',(32,10),8,6,True),('C',(40,16),(36,10),(40,12))])
        for side,x,end in [('left',8,(12,31)),('right',40,(36,31))]:
         line(f'side-{side}',(x,16),(x,24));join(f'side-{side}','hair')
         line(f'cheek-{side}',(x,24),end);join(f'side-{side}',f'cheek-{side}')
        self.add_arc('jaw',(12,31),(36,31),radius_x=15,sweep=False);join('jaw','cheek-left');join('jaw','cheek-right')
        circle('lens-left',18,22,2);circle('lens-right',30,22,2)
        line('bridge',(20,22),(28,22));join('bridge','lens-left');join('bridge','lens-right')
        path('body',(8,44),[('A',(24,41),16,3,True),('A',(40,44),16,3,True)]);join('jaw','body')
