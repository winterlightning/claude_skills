"""Doctor Eggman Character Icon.

Plan: Eggman bald circle, wide sweeping moustache at jaw, curved open shoulders. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Round nose and outward moustache retain the character shorthand; omit polygonal nose facets and jacket seam. Circular face and touching shoulders follow the shared human reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4532bd7-6d77-53a3-bc61-293a36c01f48'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/48-e4532bd7-6d77-53a3-bc61-293a36c01f48.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'doctor-eggman-bust'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('doctor', 'eggman', 'bust')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = "shoulder-top" if name == "body" and index == 1 else f"{name}-{index}"
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
        circle('head',24,18,12)
        path('body',(6,42),[('A',(14,34),8,8,True),('L',(34,34)),('A',(42,42),8,8,True)]);join('head','body')
        circle('nose',24,18,4)
        poly('moustache-left',(6,24),(12,18),(20,18))
        poly('moustache-right',(28,18),(36,18),(42,24))
        for part in ('moustache-left','moustache-right'):
            join('head',part);join('nose',part)
