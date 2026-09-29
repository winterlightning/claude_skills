"""Clipped rounded tag enclosing a wide outlined diagonal arrow; retain the distinctive source composition.
Construction: No useful subject match; geometric construction from the supplied original."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f303a1ac-9387-43d7-9138-b3796c7f22b5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__imgur-logo/20260928T175102Z-thuan-mac/reference/imgur logo_f303a1ac-9387-43d7-9138-b3796c7f22b5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'imgur-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('imgur logo',)

    def build(self):

        def path(name, start, commands, closed=False):
            members = []
            here = start
            for i, cmd in enumerate(commands):
                kind, end, *args = cmd
                if kind == 'L' and end == here:
                    continue
                key = f'{name}-{i}'
                if kind == 'L': self.add_line(key, here, end)
                elif kind == 'A':
                    rx, ry, sweep = args
                    self.add_arc(key, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == 'C': self.add_bezier(key, here, (args[0], args[1], end))
                members.append(key)
                here = end
            self.add_contour(name, *members, closed=closed)
        def oval(name, x, y, rx, ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): oval(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)

        path('tag',(20,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,28)),('L',(28,42)),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,20)),('L',(20,6))],True)
        path('arrow',(22,14),[('L',(34,14)),('L',(34,26)),('L',(29,21)),('L',(22,28)),('A',(16,22),4,4,True),('L',(23,15)),('L',(22,14))],True)

# User authorized quality-preserving exceptions; approval binds this exact drawing.
Drawing.exception = {'reason': 'Retain the broad diagonal arrow inside its clipped tag. The local 3.07-unit ink gap at the arrow tip is visibly open at 48 px.', 'approved_by': 'user-delegated-discretion-reviewed-by-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'd03bbcbc465306dcf1e55e48f1b85f5aae284239324e436c9e87cc58a2316117'}
