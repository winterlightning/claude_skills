"""Fantasy Creature with Pointed Ears.

Plan: Elongated oval face with paired slanted eyes and pointed ears. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Reduce ear outlines to pointed strokes; preserve long featureless face and narrow eyes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e0912be3-3c0a-5d39-b8ba-b235a007db37'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pointed-ear-creature-head/20260927T170540Z-thuan-mac-1/reference/goblin_e0912be3-3c0a-5d39-b8ba-b235a007db37.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'pointed-ear-creature-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('pointed', 'ear', 'creature', 'head')

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
        path('face',(11,24),[('A',(37,24),13,18,True),('A',(11,24),13,18,True)],True)
        for s in (-1,1):
         x=lambda v:24+s*v
         line(f'ear-{s}',(x(13),24),(x(18),18));join('face',f'ear-{s}')
         line(f'eye-{s}',(x(4),22),(x(4),23))
