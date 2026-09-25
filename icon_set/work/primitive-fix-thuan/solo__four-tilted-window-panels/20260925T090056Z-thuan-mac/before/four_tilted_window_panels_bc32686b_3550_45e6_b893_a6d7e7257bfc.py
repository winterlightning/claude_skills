"""Four Tilted Window Panes.

Plan: Four repeated slanted panes with open cross; intentional perspective. Bounds6,6,42,42.
Construction reference: No useful local Lucide match.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc32686b-3550-45e6-b893-a6d7e7257bfc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/microsoft logo_bc32686b-3550-45e6-b893-a6d7e7257bfc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-tilted-window-panels'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('four', 'tilted', 'window', 'panels')

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

        poly('top-left',(6,10),(19,8),(19,20),(6,22),closed=True)
        poly('top-right',(29,7),(42,6),(42,18),(29,20),closed=True)
        poly('bottom-left',(6,32),(19,30),(19,40),(6,42),closed=True)
        poly('bottom-right',(29,30),(42,28),(42,38),(29,40),closed=True)
