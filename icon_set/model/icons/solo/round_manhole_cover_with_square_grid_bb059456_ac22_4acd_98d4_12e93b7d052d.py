"""Round Sewer Manhole Cover.

Plan: Manhole cover outer radius20, inner radius11, four crossed grid lines. Grid reduced to central cross to avoid undersized cells.
Construction reference: Lucide circle: concentric circular construction
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb059456-ac22-4acd-98d4-12e93b7d052d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/manhole_bb059456-ac22-4acd-98d4-12e93b7d052d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-manhole-cover-with-square-grid'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('round', 'manhole', 'cover', 'with', 'square', 'grid')

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

        circle('outer',24,24,20);circle('inner',24,24,11)
        poly('vertical',(24,13),(24,24),(24,35));poly('horizontal',(13,24),(24,24),(35,24));join('vertical','inner');join('horizontal','inner');join('vertical','horizontal')
