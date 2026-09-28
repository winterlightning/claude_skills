"""Sailor Avatar with Cap.

Plan: Retained the broad sailor cap, circular lower face, curved shoulders and uniform center seam. Removed the narrow neck and collar. Face radius 8 at (24,14), jaw bottom 22 and shoulder top 26 give zero visible ink gap.
Construction reference: human_ref/user.svg: circular head and broad curved shoulders; avatar contact rule.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2089a768-c666-4889-b84d-c0fcb7502528'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/sailor_2089a768-c666-4889-b84d-c0fcb7502528.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sailor-bust-with-broad-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('sailor', 'bust', 'with', 'broad', 'cap')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member="body-top" if name=="body" and index==1 else f"{name}-{index}"
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

        self.add_arc('face',(16,14),(32,14),radius_x=8,radius_y=8,sweep=False)
        poly('cap',(16,14),(12,6),(24,4),(36,6),(32,14),(16,14),closed=True);join('cap','face')
        path('body',(8,44),[('L',(8,42)),('A',(24,26),16,16,True),('A',(40,42),16,16,True),('L',(40,44))]);join('body','face')
        line('seam',(24,36),(24,44))
