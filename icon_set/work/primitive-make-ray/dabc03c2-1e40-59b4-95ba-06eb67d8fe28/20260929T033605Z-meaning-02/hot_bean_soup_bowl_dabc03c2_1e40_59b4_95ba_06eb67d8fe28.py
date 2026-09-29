"""Restore a broad oval soup rim, closed curved bowl with a foot, two distinct beans and two steam wisps. Keep the beans on the soup surface.
Construction reference: Lucide soup: curved bowl and coherent steam strokes; original supplies oval surface, beans and bowl foot."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dabc03c2-1e40-59b4-95ba-06eb67d8fe28'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hot-bean-soup-bowl/20260929T033618Z-thuan-mac/reference/bean soup_dabc03c2-1e40-59b4-95ba-06eb67d8fe28.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hot-bean-soup-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('bean soup',)

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

        oval('rim',24,23,20,7)
        path('bowl',(4,23),[('C',(24,38),(5,33),(12,38)),('C',(44,23),(36,38),(43,33))]);join('rim','bowl')
        line('foot',(16,44),(32,44))
        path('bean-left',(15,24),[('C',(19,22),(14,22),(17,20))])
        path('bean-right',(28,22),[('C',(33,24),(28,25),(31,25))])
        for j,x in enumerate((18,30)):
            path(f'steam-{j}',(x,4),[('C',(x,10),(x-3,6),(x+3,8))])
