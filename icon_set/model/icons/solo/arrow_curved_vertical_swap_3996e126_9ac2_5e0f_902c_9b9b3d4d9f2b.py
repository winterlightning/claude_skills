"""Vertical Curved Swap Arrows.

Plan: Centerline4,8,44,40. Winding curve with left downward and right upward arrowheads.
Construction: No useful direct Lucide match; continuous winding line follows the original direction.
Reduction: No identifying parts omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3996e126-9ac2-5e0f-902c-9b9b3d4d9f2b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/21-3996e126-9ac2-5e0f-902c-9b9b3d4d9f2b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'arrow-curved-vertical-swap'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('arrow', 'curved', 'vertical', 'swap')

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
        path('shaft',(10,32),[('L',(10,17)),('A',(26,17),8,9,True),('L',(26,31)),('A',(38,31),6,9,False),('L',(38,16))])
        poly('down',(4,26),(10,32),(16,26));poly('up',(32,22),(38,16),(44,22));join('down','shaft');join('up','shaft')
