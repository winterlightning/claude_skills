"""Four Section Square Grid.

Plan: Rounded square with equal four cells sharing cross. Bounds6,6,42,42.
Construction reference: No useful local Lucide match.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa25190e-2d55-4604-81e3-31972e3344d4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/cell border horizontal vertical_aa25190e-2d55-4604-81e3-31972e3344d4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-four-cell-grid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('rounded', 'four', 'cell', 'grid')

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

        path('frame',(24,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,24)),('L',(42,38)),('A',(38,42),4,4,True),('L',(24,42)),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,24)),('L',(6,10)),('A',(10,6),4,4,True),('L',(24,6))],True)
        poly('horizontal',(6,24),(24,24),(42,24));poly('vertical',(24,6),(24,24),(24,42));join('horizontal','vertical');join('horizontal','frame');join('vertical','frame')
