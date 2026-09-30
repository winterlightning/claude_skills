"""The rejected hairline was an angular hook and its bottom joined the neck into a solid wedge. Restored the swept fringe, rounded ear turn and separate flared hair end behind the neck.
Plan: Human user.svg: head proportions; supplied reference owns profile and swept hair. Keyshape VRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='479da84f-9f73-458f-9606-5fa1f1bd0088'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-in-profile-with-swept-hair/20260929T111229Z-thuan-mac/reference/redhead_479da84f-9f73-458f-9606-5fa1f1bd0088.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-in-profile-with-swept-hair'
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

        path('outline',(24,44),[('L',(24,36)),('L',(32,36)),('A',(36,32),4,4,False),('L',(36,28)),('L',(40,26)),('L',(36,20)),('L',(36,16)),('C',(24,4),(36,9),(31,4)),('C',(10,18),(16,4),(10,10)),('L',(10,30)),('C',(8,40),(10,35),(8,37)),('L',(16,40))])
        path('hairline',(36,16),[('C',(22,22),(34,21),(27,22)),('C',(16,32),(18,22),(16,26)),('L',(16,40))]);join('hairline','outline')
