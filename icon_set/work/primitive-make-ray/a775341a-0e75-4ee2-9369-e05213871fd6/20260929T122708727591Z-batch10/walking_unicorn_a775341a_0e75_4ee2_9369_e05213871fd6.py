"""The rejected unicorn was blocky, with an extra left-pointing spike and fused rectangular legs. Restore the single upright horn, long muzzle, rounded back and four separated stepping legs.
Symbol plan: Original unicorn; smooth cubic back and shared leg junctions; simplified mane and tail.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a775341a-0e75-4ee2-9369-e05213871fd6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walking-unicorn/20260929T122443Z-thuan-mac/reference/fantasy unicorn 1_a775341a-0e75-4ee2-9369-e05213871fd6.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'walking-unicorn'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('walking', 'unicorn')

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

        path('horse',(10,18),[('L',(4,20)),('L',(4,16)),('L',(12,10)),('L',(12,8)),('L',(18,12)),('C',(24,22),(21,13),(20,22)),('L',(34,22)),('C',(40,28),(38,22),(40,24)),('L',(44,40)),('L',(36,40)),('L',(32,30)),('L',(23,30)),('L',(20,40)),('L',(12,40)),('L',(16,26)),('L',(10,28)),('L',(10,18))],True)
