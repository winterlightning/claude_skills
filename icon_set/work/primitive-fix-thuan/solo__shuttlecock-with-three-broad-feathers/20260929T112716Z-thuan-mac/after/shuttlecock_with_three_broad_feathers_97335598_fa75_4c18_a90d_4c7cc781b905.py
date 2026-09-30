"""The rejected shuttlecock had a flat fan edge and short internal stubs. Rounded the three feather tips, extended the feather separations and retained the rounded cork. Kept an upright arrangement for clear spacing.
Plan: No useful direct Lucide shuttlecock match; repeated rounded feather tips follow the original. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='97335598-fa75-4c18-a90d-4c7cc781b905'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__shuttlecock-with-three-broad-feathers/20260929T112716Z-thuan-mac/reference/shuttlecock_97335598-fa75-4c18-a90d-4c7cc781b905.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='shuttlecock-with-three-broad-feathers'
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

        path('fan',(6,10),[('A',(18,10),6,4,True),('A',(30,10),6,4,True),('A',(42,10),6,4,True),('L',(30,36)),('L',(18,36)),('L',(6,10))],True)
        line('feather-left',(18,10),(20,20));line('feather-right',(30,10),(28,20));join('feather-left','fan');join('feather-right','fan')
        path('cork',(18,36),[('A',(30,36),6,6,False)]);join('cork','fan')
