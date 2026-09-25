"""Camera Lens Hood.

Plan: Flared hood over three progressively narrowing lens tiers; all tier heights 8 or more.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Squared barrel tiers; retained flared hood.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac3f2390-87a4-4d4b-bd61-0ecc678e6a52'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/24-ac3f2390-87a4-4d4b-bd61-0ecc678e6a52.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'lens-with-flared-hood'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('lens', 'with', 'flared', 'hood')

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
        path('hood',(8,12),[('L',(12,12)),('C',(16,4),(16,12),(16,8)),('L',(32,4)),('C',(36,12),(32,8),(32,12)),('L',(40,12)),('L',(38,20)),('L',(10,20)),('L',(8,12))],True)
        poly('barrel',(12,20),(12,28),(16,28),(16,36),(20,36),(20,44),(28,44),(28,36),(32,36),(32,28),(36,28),(36,20));join('barrel','hood')
        line('tier-1',(12,28),(36,28));join('tier-1','barrel')
        line('tier-2',(16,36),(32,36));join('tier-2','barrel')
