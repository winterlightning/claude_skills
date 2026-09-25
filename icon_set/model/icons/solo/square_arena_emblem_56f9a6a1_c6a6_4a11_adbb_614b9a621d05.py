"""League of Legends Game Logo.

Plan: Opposing angular corner brackets and two diagonal slashes around square center. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Keep the central square, opposing angular corner brackets and two diagonal slashes. Remove short inner returns to clear the square.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56f9a6a1-c6a6-4a11-adbb-614b9a621d05'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/18-56f9a6a1-c6a6-4a11-adbb-614b9a621d05.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'square-arena-emblem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('square', 'arena', 'emblem')

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
        poly('upper',(6,26),(6,6),(26,6),(14,14))
        poly('lower',(42,22),(42,42),(22,42),(34,34))
        rect('center',20,20,8,8)
        line('slash-a',(6,42),(14,34));line('slash-b',(34,14),(42,6))
