"""Square Face Digital Smartwatch.

Plan: Blank rounded-square face in front of rear loop; bounds6,6,42,42. Preserve right opening and two real strap attachments.
Construction reference: watch.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c04a7e9-5ff0-4256-a6b8-3fa7b45bce9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/watch 1_5c04a7e9-5ff0-4256-a6b8-3fa7b45bce9a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-face-smartwatch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('square', 'face', 'smartwatch')

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

        path('face',(10,15),[('L',(14,15)),('L',(20,15)),('A',(24,19),4,4,True),('L',(24,29)),('A',(20,33),4,4,True),('L',(14,33)),('L',(10,33)),('A',(6,29),4,4,True),('L',(6,19)),('A',(10,15),4,4,True)],True)
        path('strap-top',(14,15),[('L',(14,10)),('A',(18,6),4,4,True),('L',(30,6)),('A',(42,18),12,12,True)]);join('face','strap-top')
        path('strap-bottom',(42,30),[('A',(30,42),12,12,True),('L',(18,42)),('A',(14,38),4,4,True),('L',(14,33))]);join('face','strap-bottom')
