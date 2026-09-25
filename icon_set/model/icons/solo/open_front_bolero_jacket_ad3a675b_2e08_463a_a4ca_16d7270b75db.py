"""Short Bolero Jacket.

Plan: Retained the bolero’s open curved front, cropped panels and long sleeves. Widened the cuffs and center opening.
Construction reference: Lucide shirt shoulder construction; source-specific open bolero front.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad3a675b-2e08-463a-a4ca-16d7270b75db'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bolero_ad3a675b-2e08-463a-a4ca-16d7270b75db.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-front-bolero-jacket'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('open', 'front', 'bolero', 'jacket')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        line('neck',(18,10),(30,10))
        for name,mirror in [('left',False),('right',True)]:
         def p(x,y):return (48-x if mirror else x,y)
         path(name,p(18,10),[('C',p(6,18),p(10,10),p(7,12)),('L',p(4,38)),('L',p(14,38)),('C',p(18,30),p(14,30),p(18,36)),('C',p(18,10),p(22,24),p(18,18))]);join(name,'neck')
