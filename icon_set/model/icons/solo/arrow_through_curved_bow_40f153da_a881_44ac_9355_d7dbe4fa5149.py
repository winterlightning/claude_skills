"""Arrow Through Curved Bow
Plan: Right-pointing arrow crosses a semicircular bow at its midpoint. The crossing is explicitly shared.
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: No useful exact Lucide match; half-circle and arrowhead.
Reduction: Complete arc and arrow retained.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40f153da-a881-44ac-9355-d7dbe4fa5149'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/diagram arrow bow_40f153da-a881-44ac-9355-d7dbe4fa5149.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arrow-through-curved-bow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bow', 'arrow', 'archery', 'curve', 'shaft', 'point', 'sport')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        path('bow',(4,8),[('A',(24,24),20,16,True),('A',(4,40),20,16,True)])
        self.add_polyline('shaft',(4,24),(24,24),(44,24))
        self.add_polyline('arrowhead',(36,16),(44,24),(36,32))
        for bow in ['bow-0','bow-1']:
            for shaft in ['shaft-1','shaft-2']:self.relate('connect',bow,shaft)
        for head in ['arrowhead-1','arrowhead-2']:self.relate('connect','shaft-2',head)
