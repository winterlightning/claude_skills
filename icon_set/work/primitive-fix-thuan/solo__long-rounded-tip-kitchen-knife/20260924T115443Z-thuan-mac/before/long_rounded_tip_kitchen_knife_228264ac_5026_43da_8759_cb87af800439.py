"""Sharp Kitchen Knife.

Plan: Retained the diagonal kitchen blade, rounded tip, bolster boundary and rounded handle. Widened the handle to keep its opening clear.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '228264ac-5026-43da-8759-cb87af800439'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blade_228264ac-5026-43da-8759-cb87af800439.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-rounded-tip-kitchen-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('long', 'rounded', 'tip', 'kitchen', 'knife')

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

        path('blade',(20,26),[('L',(42,6)),('C',(36,28),(42,16),(42,20)),('L',(26,36)),('L',(20,26))],True)
        path('handle',(20,26),[('L',(8,34)),('C',(6,38),(6,35),(6,37)),('A',(10,42),4,4,False),('L',(26,36))]);join('handle','blade')
