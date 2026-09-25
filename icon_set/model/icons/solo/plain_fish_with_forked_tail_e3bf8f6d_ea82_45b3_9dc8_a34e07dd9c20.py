"""Plain Fish with Forked Tail
Plan: Pointed head, full body, curved gill and forked tail; original facing direction retained.
Keyshape: HRECT_M; exact inset SOLO48 envelope.
Construction: Lucide fish: coherent body curves and paired fins.
Reduction: Gill extended to body edges for a readable curve."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3bf8f6d-ea82-45b3-9dc8-a34e07dd9c20'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blackfish_e3bf8f6d-ea82-45b3-9dc8-a34e07dd9c20.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-fish-with-forked-tail'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('fish', 'sea', 'aquatic', 'tail', 'gill', 'animal', 'swimming')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('fish',(4,24),[('C',(22,14),(8,17),(14,14)),('C',(34,20),(27,14),(31,18)),('L',(44,10)),('L',(40,24)),('L',(44,38)),('L',(34,28)),('C',(22,34),(31,30),(27,34)),('C',(4,24),(14,34),(8,31))],True)
        path('gill',(22,14),[('C',(22,34),(26,18),(26,30))]);self.relate('connect','fish','gill')
