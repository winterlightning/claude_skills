"""Unrolled paper: rejected curl looks like a folded corner; top paper lip is absent. Restore a full-height roll and separated top edge. Make the rolled paper span the full height and restore a top paper lip.
Symbol plan: Original rolled right edge and top lip; use shared radii and broad paper interior.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0f4ecb94-3a73-4380-95f8-a8bd0a7bf26d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__unrolled-paper-right-curl/20260929T115456Z-thuan-mac/reference/blueprint 1_0f4ecb94-3a73-4380-95f8-a8bd0a7bf26d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'unrolled-paper-right-curl'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('unrolled', 'paper', 'right', 'curl')

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

        path('sheet',(36,8),[('L',(4,8)),('L',(4,40)),('L',(36,40)),('A',(44,32),8,8,False),('L',(44,16)),('A',(36,8),8,8,False)],True)
        path('roll',(36,8),[('A',(28,16),8,8,False),('L',(28,32)),('L',(36,32)),('A',(44,32),4,4,False)]);join('roll','sheet')
        line('lip',(4,16),(28,16));join('lip','sheet');join('lip','roll')
