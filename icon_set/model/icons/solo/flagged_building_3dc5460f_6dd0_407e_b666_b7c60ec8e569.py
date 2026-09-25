"""Building with Flag on Top.

Plan: Flagged building with simple centered8-wide rectangular doorway, roof and notched flag.
Construction: Lucide church: structural roof and facade.
Reduction: Squared doorway and removed ground overhang to retain minimum opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3dc5460f-6dd0-407e-b666-b7c60ec8e569'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/17-3dc5460f-6dd0-407e-b666-b7c60ec8e569.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'flagged-building'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('flagged', 'building')

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
        poly('facade',(8,28),(8,44),(20,44),(20,36),(28,36),(28,44),(40,44),(40,28),(24,20),(8,28))
        line('eaves',(8,28),(40,28));join('eaves','facade')
        poly('pole',(24,20),(24,4),(36,4),(32,8),(36,12),(24,12));join('pole','facade')
