"""Stacked Landscape Photo Gallery.

Plan: Centerline6,6,42,42. Offset rear photo behind a large front image; mountain contour attaches at lower corners.
Construction: No useful direct Lucide match; photo layers with source-specific landscape.
Reduction: Secondary small peak omitted; mountain expanded to connect to frame and preserve open interior.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '206fa313-37ee-4826-b03f-bda05b9a6f9d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/39-206fa313-37ee-4826-b03f-bda05b9a6f9d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'stacked-landscape-photo-gallery'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('stacked', 'landscape', 'photo', 'gallery')

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
        path('rear',(6,31),[('L',(6,10)),('A',(10,6),4,4,True),('L',(27,6)),('A',(31,10),4,4,True),('L',(31,15))])
        path('front',(19,15),[('L',(31,15)),('L',(38,15)),('A',(42,19),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(19,42)),('A',(15,38),4,4,True),('L',(15,19)),('A',(19,15),4,4,True)],True)
        poly('mountain',(15,38),(28,25),(42,38));join('rear','front');join('mountain','front')
