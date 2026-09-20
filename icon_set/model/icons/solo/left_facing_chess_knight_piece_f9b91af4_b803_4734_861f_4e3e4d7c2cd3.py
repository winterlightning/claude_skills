"""Chess Knight Piece.

Plan: Continuous left-facing knight silhouette with solid shared plinth edge and broad muzzle; x8..40 y4..44.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Broadened muzzle and removed duplicated plinth line; no eye added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9b91af4-b803-4734-861f-4e3e4d7c2cd3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/34-f9b91af4-b803-4734-861f-4e3e4d7c2cd3.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'left-facing-chess-knight-piece'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('left', 'facing', 'chess', 'knight', 'piece')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('horse',(16,36),[('C',(24,23),(15,31),(22,27)),('L',(12,26)),('L',(8,20)),('L',(22,10)),('L',(22,4)),('C',(36,20),(33,7),(38,12)),('C',(34,36),(33,26),(31,31))])
        poly('plinth',(16,36),(12,36),(8,44),(40,44),(36,36),(34,36));join('plinth','horse')
        line('base-top',(16,36),(34,36));join('base-top','horse');join('base-top','plinth')
