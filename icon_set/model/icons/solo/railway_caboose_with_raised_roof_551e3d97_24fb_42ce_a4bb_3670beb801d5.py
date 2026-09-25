"""Railway Caboose Car.

Plan: Caboose bounds4,8,44,40. Raised roof, two windows and two wheels. Reduce roof thickness and window frames to U-shaped structural openings.
Construction reference: Lucide car: round wheels and continuous structural body
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '551e3d97-24fb-42ce-a4bb-3670beb801d5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/caboose_551e3d97-24fb-42ce-a4bb-3670beb801d5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'railway-caboose-with-raised-roof'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('railway', 'caboose', 'with', 'raised', 'roof')

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

        poly('roof',(4,16),(16,16),(16,8),(32,8),(32,16),(44,16))
        poly('body',(8,16),(8,32),(16,32),(32,32),(40,32),(40,16));join('body','roof')
        poly('window-left',(8,24),(16,24),(16,16));poly('window-right',(32,16),(32,24),(40,24));join('window-left','body');join('window-left','roof');join('window-right','body');join('window-right','roof')
        circle('wheel-left',16,36,4);circle('wheel-right',32,36,4);join('wheel-left','body');join('wheel-right','body')
