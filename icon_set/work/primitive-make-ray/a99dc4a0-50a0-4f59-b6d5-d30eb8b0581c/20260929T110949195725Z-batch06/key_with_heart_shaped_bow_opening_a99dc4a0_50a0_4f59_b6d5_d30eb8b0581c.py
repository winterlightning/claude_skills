"""The rejected key had a very short upright shaft and a pinched tiny heart. Enlarged the heart-shaped opening into the bow and restored a diagonal shaft. Simplified the outer circular ring.
Plan: Lucide key-round: diagonal shaft attached to a rounded bow. Keyshape SQUARE; shared contour nodes and dimensions.
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

        path('heart',(22,20),[('A',(6,20),8,8,False),('C',(22,42),(6,28),(14,36)),('C',(38,20),(30,36),(38,28)),('A',(22,20),8,8,False)],True)
        poly('shaft',(34,12),(40,6),(42,6));join('shaft','heart')
