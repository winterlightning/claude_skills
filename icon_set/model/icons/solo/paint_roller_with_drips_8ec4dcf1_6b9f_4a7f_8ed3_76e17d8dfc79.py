"""A broad roller sleeve with a hanging paint drip and bent handle. Square envelope preserves tool proportions. Source supplies integrated drip; extra narrow drip strokes and handle double outline omitted. Lucide paint-roller supplies rounded sleeve and bent support construction. Drip is part of sleeve contour; support meets split right sleeve edge."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ec4dcf1-6b9f-4a7f-8ed3-76e17d8dfc79'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/paint roller_8ec4dcf1-6b9f-4a7f-8ed3-76e17d8dfc79.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'paint-roller-with-drips'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Paint Roller with Drips',)
    keywords = ('roller', 'paint', 'drips', 'decorating', 'handle', 'tool')
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
        path('sleeve',(32,12),[('L',(32,10)),('A',(28,6),4,4,False),('L',(10,6)),('A',(6,10),4,4,False),('L',(6,14)),('A',(10,18),4,4,False),('L',(12,18)),('L',(12,22)),('A',(20,22),4,4,False),('L',(20,18)),('L',(28,18)),('A',(32,14),4,4,False),('L',(32,12))],True)
        path('support-handle',(32,12),[('L',(38,12)),('A',(42,16),4,4,True),('L',(42,24)),('A',(38,28),4,4,True),('L',(34,28)),('A',(30,32),4,4,False),('L',(30,42))])
        join('sleeve','support-handle')
