"""Chemical Molecular Structure.

Plan: Central r4 node and three r4 outer nodes with actual shared bond endpoints; upper node at24,10 and center24,26.
Construction: Lucide network: attached branches and node hierarchy.
Reduction: Equalized node sizes to reserve bond clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90c0c06b-4d60-42f2-a3b6-cce0458bb3a4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/33-90c0c06b-4d60-42f2-a3b6-cce0458bb3a4.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'four-node-molecular-diagram'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('four', 'node', 'molecular', 'diagram')

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
        circle('center',24,26,4)
        circle('top',24,10,4)
        circle('left',10,38,4)
        circle('right',38,38,4)
        line('bond-top',(24,14),(24,22));join('bond-top','top');join('bond-top','center')
        line('bond-left',(20,26),(10,34));join('bond-left','left');join('bond-left','center')
        line('bond-right',(28,26),(38,34));join('bond-right','right');join('bond-right','center')
