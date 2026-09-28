"""Masked Superhero Character Avatar.

Plan: Circular portrait head with identifying face/headwear over touching shoulders. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Reduce eye patches to inward slanted eye strokes; omit costume seam.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8ff3e5fd-b424-551b-a3a5-cf783be1c005'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__masked-spider-hero-bust/20260927T182642Z-thuan-mac-1/reference/spiderman_8ff3e5fd-b424-551b-a3a5-cf783be1c005.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'masked-spider-hero-bust'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('masked', 'spider', 'hero', 'bust')

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
        # A circular mask has a separate central neck, so the shoulders clear its jaw.
        path('head',(11,19),[('A',(24,6),13,13,True),('A',(37,19),13,13,True),
             ('A',(24,32),13,13,True),('A',(11,19),13,13,True)],True)
        self.add_polyline('body',(6,42),(10,40),(24,40),(38,40),(42,42))
        line('neck',(24,32),(24,40));join('head','neck');join('body','neck')
        line('eye-left',(20,18),(20,20));line('eye-right',(28,18),(28,20))
