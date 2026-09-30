"""The rejected key had a short upright shaft and a pinched heart. Enlarged the heart into an open bow and added a diagonal shaft with a clear perpendicular tooth. Omitted the outer circular ring to preserve a readable heart opening.
Plan: Lucide key-round: diagonal shaft with a terminal tooth. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='a99dc4a0-50a0-4f59-b6d5-d30eb8b0581c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__key-with-heart-shaped-bow-opening/20260929T110722Z-thuan-mac/reference/love heart key_a99dc4a0-50a0-4f59-b6d5-d30eb8b0581c.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='key-with-heart-shaped-bow-opening'
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

        path('heart',(18,12),[('A',(6,12),6,6,False),('C',(18,30),(6,20),(12,26)),('C',(30,12),(24,26),(30,20)),('A',(18,12),6,6,False)],True)
        poly('shaft',(18,30),(30,42),(42,30));join('shaft','heart')
