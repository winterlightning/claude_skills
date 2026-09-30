"""The rejected orangutan had a single circular muzzle resembling one eye and tiny knee rings. Restored the broad two-lobed muzzle and long seated arms. Omitted ear loops and tiny knee rings to give the face room.
Plan: No useful direct Lucide ape match; original pear-shaped muzzle and long-arm silhouette. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='014fc7d1-8818-495c-9f61-d1612dae4e23'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__seated-orangutan-front-view/20260929T112544Z-thuan-mac/reference/orangutan_014fc7d1-8818-495c-9f61-d1612dae4e23.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='seated-orangutan-front-view'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                members.append(member);here=end
            self.add_contour(name,*members,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*pts): self.add_polyline(name,*pts)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r): path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('body',(6,42),[('L',(6,32)),('C',(10,24),(6,28),(8,26)),('L',(10,20)),('A',(24,6),14,14,True),('A',(38,20),14,14,True),('L',(38,24)),('C',(42,32),(40,26),(42,28)),('L',(42,42)),('L',(6,42))],True)
        path('muzzle',(24,17),[('C',(18,20),(20,14),(18,16)),('L',(18,24)),('A',(30,24),6,6,False),('L',(30,20)),('C',(24,17),(30,16),(28,14))],True)
        poly('left-arm',(14,36),(14,42));join('left-arm','body')
        poly('right-arm',(34,36),(34,42));join('right-arm','body')
