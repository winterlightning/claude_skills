"""Restore a tall ankle boot, shaped toe, short buckle and four evenly spaced outlined wheels mounted beneath its sole.
Construction reference: Supplied inline skate reference; repeated circles share one radius and spacing."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a010f79f-3ca0-5f51-8cbf-bd0c35154343'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__inline-skate/20260929T033618Z-thuan-mac/reference/rollerblades_a010f79f-3ca0-5f51-8cbf-bd0c35154343.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'inline-skate'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('rollerblades',)

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

        path('boot',(8,6),[('L',(24,6)),('L',(24,18)),('C',(31,23),(24,22),(26,23)),('L',(34,23)),('C',(42,28),(39,23),(42,25)),('C',(36,32),(42,31),(40,32)),('L',(12,32)),('C',(6,26),(8,32),(6,30)),('L',(8,6))],True)
        line('buckle',(18,14),(24,14));join('boot','buckle')
        for j,x in enumerate((6,18,30,42)):circle(f'wheel-{j}',x,42,3)
