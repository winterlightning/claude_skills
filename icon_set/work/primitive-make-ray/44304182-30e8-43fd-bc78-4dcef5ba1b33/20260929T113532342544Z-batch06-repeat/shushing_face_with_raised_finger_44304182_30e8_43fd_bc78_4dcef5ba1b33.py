"""The rejected shushing hand was a squared arch with a rigid wrist. Tilted the raised index finger slightly and rounded the curled hand to restore the natural shushing gesture. Kept the lower face open around the hand.
Plan: Human user.svg: round head vocabulary; source-specific raised finger construction. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='44304182-30e8-43fd-bc78-4dcef5ba1b33'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__shushing-face-with-raised-finger/20260929T112716Z-thuan-mac/reference/face shush_44304182-30e8-43fd-bc78-4dcef5ba1b33.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='shushing-face-with-raised-finger'
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

        path('head',(6,24),[('A',(42,24),18,18,True),('C',(38,40),(42,32),(40,36))])
        path('left-cheek',(6,24),[('C',(14,40),(6,34),(10,40))]);join('head','left-cheek')
        path('hand',(22,42),[('L',(24,30)),('A',(32,30),4,4,True),('L',(32,36)),('L',(34,36)),('A',(38,40),4,4,True),('L',(38,42))]);join('hand','head')
        self.add_dot('eye-left',(17,18));self.add_dot('eye-right',(31,18))
