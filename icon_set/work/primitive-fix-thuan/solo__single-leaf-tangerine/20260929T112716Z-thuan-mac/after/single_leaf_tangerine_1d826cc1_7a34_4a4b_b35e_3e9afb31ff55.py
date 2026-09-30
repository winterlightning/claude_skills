"""The rejected tangerine was flattened beneath a large leaf. Made the fruit rounder by narrowing its width and increasing its height, with a compact broad leaf and short stem.
Plan: Lucide sprout: broad pointed leaf attached to stem. Keyshape VRECT_M; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='1d826cc1-7a34-4a4b-b35e-3e9afb31ff55'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__single-leaf-tangerine/20260929T112716Z-thuan-mac/reference/tangerine_1d826cc1-7a34-4a4b-b35e-3e9afb31ff55.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='single-leaf-tangerine'
    keyshape=Keyshape.VRECT_M
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

        path('fruit',(24,22),[('A',(38,33),14,11,True),('A',(24,44),14,11,True),('A',(10,33),14,11,True),('A',(24,22),14,11,True)],True)
        poly('stem',(24,22),(20,14),(16,6));join('stem','fruit')
        path('leaf',(20,14),[('C',(38,4),(20,4),(28,4)),('C',(20,14),(38,14),(28,14))],True);join('leaf','stem')
