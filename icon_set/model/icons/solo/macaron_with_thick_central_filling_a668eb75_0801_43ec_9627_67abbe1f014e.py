"""French Macaron Cookie.

Plan: Two domed macaron shells and thick filling. Bounds4,10,44,38.
Construction reference: No useful local Lucide match.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a668eb75-0801-43ec-9627-67abbe1f014e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/macaroon_a668eb75-0801-43ec-9627-67abbe1f014e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'macaron-with-thick-central-filling'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('macaron', 'with', 'thick', 'central', 'filling')

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

        path('shell',(4,20),[('C',(24,10),(4,14),(12,10)),('C',(44,20),(36,10),(44,14)),('L',(44,28)),('C',(24,38),(44,34),(36,38)),('C',(4,28),(12,38),(4,34)),('L',(4,20))],True)
        line('top-filling',(4,20),(44,20));line('bottom-filling',(4,28),(44,28));join('shell','top-filling');join('shell','bottom-filling')
