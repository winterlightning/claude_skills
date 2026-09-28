"""Greek Head with Laurel Wreath.

Plan: Right-facing classical head with diagonal laurel branch integrated into crown; alternating attached leaf strokes; bounds (8,4)-(40,44).
Construction: Shared human user.svg guides rounded head; deliberate classical profile, laurel branch crosses the crown.
Reduction: Fine laurel foliage reduced to alternating broad attached strokes; branch shares crown contour.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a2f7b8c2-0fe1-4df7-acc9-6ea542c9ad2e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__laurel-crowned-head-in-profile/20260927T164305Z-thuan-mac-1/reference/greek god head wreath 1_a2f7b8c2-0fe1-4df7-acc9-6ea542c9ad2e.svg'
AUTHOR = "gpt-6"


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
        # Round skull and stepped face profile follow the original bust silhouette.
        path('head',(14,44),[('L',(14,34)),('C',(8,26),(10,31),(8,29)),('L',(8,20)),('C',(24,4),(8,11),(16,4)),('C',(35,14),(32,4),(35,8)),('L',(40,25)),('L',(33,25)),('L',(33,32)),('A',(27,38),6,6,True),('L',(26,38)),('L',(26,44))])
        poly('laurel-branch',(8,20),(17,18),(26,16),(35,14));join('head','laurel-branch')
        line('laurel-leaf-one',(17,18),(19,26));join('laurel-branch','laurel-leaf-one')
        line('laurel-leaf-two',(26,16),(28,23));join('laurel-branch','laurel-leaf-two')
