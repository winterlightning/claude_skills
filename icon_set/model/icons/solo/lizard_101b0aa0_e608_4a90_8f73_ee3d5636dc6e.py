"""A seated right-facing lizard has a smoothly swept back, broad head, bent foreleg and curled tail. Extrema 4,8,44,40.
Construction: No useful direct Lucide match; original reptile silhouette and coherent supported cubic contours
Reduction: Tiny toe marks omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '101b0aa0-e608-4a90-8f73-ee3d5636dc6e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/31-101b0aa0-e608-4a90-8f73-ee3d5636dc6e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='lizard'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('lizard',)
    def build(self):

        def path(name,start,steps,closed=False):
            here=start;members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
                else:self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m);here=end
            self.add_contour(name,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('outline',(22,40),[('C',(4,30),(10,40),(4,38)),('C',(24,15),(4,23),(15,16)),('C',(34,8),(29,14),(27,8)),('C',(44,14),(40,8),(44,10)),('C',(35,20),(44,18),(39,20)),('L',(30,30)),('L',(36,30))])
        path('tail',(22,40),[('C',(13,34),(17,39),(13,38)),('C',(22,28),(13,30),(18,28)),('L',(24,28)),('L',(24,34)),('L',(29,34))]);join('tail','outline')
