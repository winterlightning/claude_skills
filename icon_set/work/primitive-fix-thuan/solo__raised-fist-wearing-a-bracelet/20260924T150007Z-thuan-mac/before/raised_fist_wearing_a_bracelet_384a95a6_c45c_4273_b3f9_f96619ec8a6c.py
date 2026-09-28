"""Raised Clenched Fist with Bracelet.

Plan: Upright fist with broad bracelet; bounds8,4,40,44. Three knuckles retain fist rhythm without crowded detail.
Construction reference: Lucide hand: round knuckles and simple palm
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '384a95a6-c45c-4273-b3f9-f96619ec8a6c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/romance pride lgbt bracelet fist_384a95a6-c45c-4273-b3f9-f96619ec8a6c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'raised-fist-wearing-a-bracelet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('raised', 'fist', 'wearing', 'a', 'bracelet')

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

        path('fist',(14,36),[('L',(14,30)),('C',(8,20),(9,26),(8,24)),('L',(8,16)),('L',(8,8)),('A',(16,8),4,4,True),('A',(24,8),4,4,True),('A',(32,8),4,4,True),('A',(40,8),4,4,True),('L',(40,12)),('L',(40,22)),('C',(34,32),(40,27),(34,28)),('L',(34,36))])
        path('thumb',(8,16),[('L',(20,16)),('A',(24,20),4,4,True),('C',(20,26),(24,24),(22,25))]);join('thumb','fist')
        rect('bracelet',8,36,32,8,4);join('bracelet','fist')
