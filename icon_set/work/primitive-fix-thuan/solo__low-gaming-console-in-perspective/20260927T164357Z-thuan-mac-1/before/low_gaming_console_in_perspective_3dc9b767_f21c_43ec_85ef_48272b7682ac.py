"""PlayStation Four Gaming Console.

Plan: Low perspective gaming console with sloped top and a circular power control. Extremes4,8,44,40.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit the small power circle; retain the low slanted console and both side faces.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3dc9b767-f21c-43ec-85ef-48272b7682ac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/34-3dc9b767-f21c-43ec-85ef-48272b7682ac.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'low-gaming-console-in-perspective'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('low', 'gaming', 'console', 'in', 'perspective')

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
        poly('outline',(4,22),(28,8),(44,18),(40,30),(20,40),(4,30),closed=True)
        poly('top-seam',(4,22),(20,28),(44,18));join('outline','top-seam')
        line('corner',(20,28),(20,40));join('top-seam','corner');join('outline','corner')
        
