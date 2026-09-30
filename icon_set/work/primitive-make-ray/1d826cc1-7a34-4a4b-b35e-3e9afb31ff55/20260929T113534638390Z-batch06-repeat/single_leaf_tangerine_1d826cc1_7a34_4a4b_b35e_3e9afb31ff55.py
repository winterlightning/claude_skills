"""The rejected tangerine was a very flat oval beneath an oversized leaf. Enlarged the fruit vertically and reduced the leaf and stem to restore a rounder fruit-dominant silhouette.
Plan: Lucide sprout: pointed leaf attached at a stem node. Keyshape VRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='1d826cc1-7a34-4a4b-b35e-3e9afb31ff55'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__single-leaf-tangerine/20260929T112716Z-thuan-mac/reference/tangerine_1d826cc1-7a34-4a4b-b35e-3e9afb31ff55.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='single-leaf-tangerine'
    keyshape=Keyshape.VRECT_L
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

        path('fruit',(24,20),[('A',(40,32),16,12,True),('A',(24,44),16,12,True),('A',(8,32),16,12,True),('A',(24,20),16,12,True)],True)
        poly('stem',(24,20),(24,12),(20,4));join('stem','fruit')
        path('leaf',(24,12),[('C',(40,4),(26,4),(34,4)),('C',(24,12),(38,10),(30,12))],True);join('leaf','stem')
