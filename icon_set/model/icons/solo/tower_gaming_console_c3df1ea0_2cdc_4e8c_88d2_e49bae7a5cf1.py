"""Modern Tower Gaming Console.

Plan: Three-quarter tower console with diamond top, vertical faces, power dot and slot. Extremes8,4,40,44.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Retain perspective and two separated controls; reduce the narrow vertical slot to a round mark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3df1ea0-2cdc-4e8c-88d2-e49bae7a5cf1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/24-c3df1ea0-2cdc-4e8c-88d2-e49bae7a5cf1.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'tower-gaming-console'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('tower', 'gaming', 'console')

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
        poly('outline',(8,10),(24,4),(40,10),(40,38),(24,44),(8,38),closed=True)
        poly('top',(8,10),(24,16),(40,10));join('outline','top')
        line('edge',(24,16),(24,44));join('top','edge');join('outline','edge')
        self.add_dot('power',(32,24));self.add_dot('slot',(32,32))
