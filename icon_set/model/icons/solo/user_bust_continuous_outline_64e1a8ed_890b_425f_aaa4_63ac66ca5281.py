"""User Profile Avatar.

Plan: Circular face arcs and continuous neck into rounded shoulders; bounds8,4,40,44. Preserve source continuous outline and open bottom; no detached-head gap applies.
Construction reference: human_ref/user.svg.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64e1a8ed-890b-425f-aaa4-63ac66ca5281'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/person_64e1a8ed-890b-425f-aaa4-63ac66ca5281.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'user-bust-continuous-outline'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('user', 'bust', 'continuous', 'outline')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('bust',(8,44),[('C',(18,30),(8,36),(18,36)),('L',(18,22)),('A',(14,14),10,10,True),('A',(24,4),10,10,True),('A',(34,14),10,10,True),('A',(30,22),10,10,True),('L',(30,30)),('C',(40,44),(30,36),(40,36))])
