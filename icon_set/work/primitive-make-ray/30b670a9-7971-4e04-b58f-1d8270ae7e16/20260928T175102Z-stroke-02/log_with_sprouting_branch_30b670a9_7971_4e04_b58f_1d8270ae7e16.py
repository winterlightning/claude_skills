"""Circular cut end with a concentric growth ring, cylindrical log body and a short open branch stump. Retain the asymmetry of a real branch.
Construction: No useful subject match; geometric construction from the supplied original."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '30b670a9-7971-4e04-b58f-1d8270ae7e16'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__log-with-sprouting-branch/20260928T175102Z-thuan-mac/reference/tree log_30b670a9-7971-4e04-b58f-1d8270ae7e16.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'log-with-sprouting-branch'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('tree log',)

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

        circle('cut-face',16,28,12)
        circle('growth-ring',16,28,3)
        path('body',(16,16),[('L',(26,16)),('C',(30,13),(28,16),(29,15)),('L',(33,8)),('L',(42,8)),('L',(37,18)),('C',(44,28),(42,20),(44,24)),('C',(32,40),(44,35),(39,40)),('L',(16,40))])

        join('cut-face','body')
