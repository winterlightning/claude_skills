"""Greek Head with Laurel Wreath.

Plan: Right-facing classical head with diagonal laurel branch integrated into crown; alternating attached leaf strokes; bounds (8,4)-(40,44).
Construction: Shared human user.svg guides rounded head; deliberate classical profile, laurel branch crosses the crown.
Reduction: Fine laurel foliage reduced to alternating broad attached strokes; branch shares crown contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2f7b8c2-0fe1-4df7-acc9-6ea542c9ad2e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/38-a2f7b8c2-0fe1-4df7-acc9-6ea542c9ad2e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'laurel-crowned-head-in-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('laurel', 'crowned', 'head', 'in', 'profile')

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
        path('head',(13,44),[('L',(13,33)),('C',(8,23),(9,29),(8,27)),('L',(8,16)),('L',(16,12)),('L',(24,8)),('C',(32,16),(29,8),(32,11)),('L',(40,26)),('L',(32,26)),('L',(32,34)),('A',(26,40),6,6,True),('L',(26,44))])
        poly('leaf-one',(12,4),(16,12),(20,20));line('leaf-two',(24,8),(24,4));join('head','leaf-one');join('head','leaf-two')
