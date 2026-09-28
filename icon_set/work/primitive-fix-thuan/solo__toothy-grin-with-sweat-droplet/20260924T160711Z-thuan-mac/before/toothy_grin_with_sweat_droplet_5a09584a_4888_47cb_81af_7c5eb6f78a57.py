"""Grinning Face with Sweat Drop.

Plan: Sweating grin with upper-right rim open behind droplet; circular face center24 radius20; asymmetric mouth balances droplet.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Right eye and tooth dividers omitted to make room for the sweat drop; open rim preserves legal separation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a09584a-4888-47cb-81af-7c5eb6f78a57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/41-5a09584a-4888-47cb-81af-7c5eb6f78a57.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'toothy-grin-with-sweat-droplet'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('toothy', 'grin', 'with', 'sweat', 'droplet')

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
        path('face',(24,4),[('A',(4,24),20,20,False),('A',(24,44),20,20,False),('A',(40,36),20,20,False),('C',(43,30),(41,34),(42,32))])
        path('sweat',(36,8),[('C',(32,16),(34,12),(32,14)),('A',(40,16),4,4,False),('C',(36,8),(40,14),(38,12))],True)
        path('eye',(16,19),[('A',(20,19),2,2,True)])
        path('mouth',(14,28),[('L',(30,28)),('A',(14,28),8,7,True)],True)
