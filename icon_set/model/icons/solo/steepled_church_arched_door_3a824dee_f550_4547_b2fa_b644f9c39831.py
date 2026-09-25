"""Church Building with Steeple.

Plan: Church with narrow steeple and broad nave, arched door; x8..40 y4..44.
Construction: Lucide church: central tower, sloping shoulders, arched doorway.
Reduction: Removed small tower window to keep steeple and nave openings clear.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a824dee-f550-4547-b2fa-b644f9c39831'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/36-3a824dee-f550-4547-b2fa-b644f9c39831.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'steepled-church-arched-door'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('steepled', 'church', 'arched', 'door')

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
        poly('church',(8,44),(8,30),(18,24),(18,16),(24,4),(30,16),(30,24),(40,30),(40,44),(8,44))
        line('steeple-base',(18,16),(30,16));join('steeple-base','church')
        path('door',(19,44),[('L',(19,36)),('A',(29,36),5,5,True),('L',(29,44))]);join('door','church')
