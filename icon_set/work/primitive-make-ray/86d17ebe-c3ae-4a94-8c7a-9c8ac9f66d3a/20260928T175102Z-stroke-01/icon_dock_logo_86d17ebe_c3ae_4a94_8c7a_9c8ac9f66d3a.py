"""Circular top ring, central stem and mirrored diagonal arrows, with one shared bottom node; centerline extremes x8..40, y4..44.
Construction: Lucide anchor: one circular ring and actual stem attachments; source retains straight arrow arms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '86d17ebe-c3ae-4a94-8c7a-9c8ac9f66d3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__icon-dock-logo/20260928T175102Z-thuan-mac/reference/icon dock logo_86d17ebe-c3ae-4a94-8c7a-9c8ac9f66d3a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'icon-dock-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('icon dock logo',)

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

        circle('ring',24,10,6)
        line('stem',(24,16),(24,44))
        poly('arms',(8,26),(24,44),(40,26))
        for side in (-1,1):
            x=24+16*side
            poly(f'tip-{side}',(x-side,34),(x,26),(x-7*side,29))
            join('arms',f'tip-{side}')
        join('ring','stem');join('stem','arms')
