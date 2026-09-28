"""Classic Formal Top Hat.

Plan: Tall crown and8-high hatband over broad8-high brim with modest corner radius2.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Reduced brim corner radius to preserve uniform opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c08a3471-5d56-428f-b16c-53278ed963fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/44-c08a3471-5d56-428f-b16c-53278ed963fe.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'formal-top-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('formal', 'top', 'hat')

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
        poly('crown',(12,34),(12,6),(36,6),(36,34))
        line('band',(12,26),(36,26));join('band','crown')
        path('brim',(6,34),[('L',(42,34)),('L',(42,40)),('A',(40,42),2,2,True),('L',(8,42)),('A',(6,40),2,2,True),('L',(6,34))],True);join('brim','crown')
