"""The rejected blank-faced woman lost her parted hair and collar shape. Restore a parted fringe below a distinct bun, a circular jaw and broad shoulders touching the jaw.
Symbol plan: human_ref/user.svg circular head and broad shoulders; original bun and parted hair. Jaw bottom36 to shoulders40 gives zero visible gap.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3541dce7-9d7e-4c68-ad5e-dc77e423e461'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-bust-with-bun-and-blank-face/20260929T124732Z-thuan-mac/reference/grandmom_3541dce7-9d7e-4c68-ad5e-dc77e423e461.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'woman-bust-with-bun-and-blank-face'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('woman', 'bust', 'with', 'bun', 'and', 'blank', 'face')
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

        path('hair',(12,24),[('A',(18,14),6,10,True),('L',(18,12)),('A',(30,12),6,8,True),('L',(30,14)),('A',(36,24),6,10,True)])
        self.add_arc('jaw',(12,24),(36,24),radius_x=12,sweep=False);join('hair','jaw')
        path('fringe',(12,24),[('C',(24,20),(18,24),(21,22)),('C',(36,24),(27,22),(30,24))]);join('hair','fringe');join('jaw','fringe')
        path('body',(8,44),[('A',(24,40),16,4,True),('A',(40,44),16,4,True)]);join('jaw','body')
