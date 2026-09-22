"""A looped soft pretzel with two broad dough lobes and a diagonal opening.
HRECT_L keeps the broad dough silhouette. Source supplies opposing lobes and
angled hole; tiny end seams omitted for spacing. No Lucide pretzel match found.
Outer lobe curves share horizontal extrema; intentional diagonal hole asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '68369691-77d6-4ea8-94e8-beffbe094ced'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/outdoors bird_68369691-77d6-4ea8-94e8-beffbe094ced.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'looped-soft-pretzel'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ('Twisted Soft Pretzel',)
    keywords = ('pretzel', 'bread', 'loop', 'dough', 'snack', 'food')
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
        path('dough',(14,8),[('C',(24,12),(18,8),(21,10)),('C',(34,8),(27,10),(30,8)),('C',(44,24),(40,8),(44,16)),('C',(34,40),(44,32),(40,40)),('C',(24,39),(30,40),(27,39)),('C',(14,40),(21,39),(18,40)),('C',(4,24),(8,40),(4,32)),('C',(14,8),(4,16),(8,8))],True)
        path('opening',(16,24),[('C',(24,22),(16,18),(20,18)),('L',(30,28)),('C',(16,24),(32,31),(16,31))],True)
