"""Restore the complete circular face, a matched pair of inward eye spirals and a short straight mouth.
Construction reference: Supplied face reference; repeated spirals share one construction."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e67e67e8-fb33-47eb-a330-05cfafa37994'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hypnotized-face/20260929T033618Z-thuan-mac/reference/hypnotized_e67e67e8-fb33-47eb-a330-05cfafa37994.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hypnotized-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('hypnotized',)

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

        circle('face',24,24,20)
        for j,cx in enumerate((16,32)):
            path(f'spiral-{j}',(cx-3,26),[('C',(cx,15),(cx-8,24),(cx-8,15)),('C',(cx+1,25),(cx+8,15),(cx+8,25)),('C',(cx+2,20),(cx-2,25),(cx-2,20))])
        line('mouth',(20,35),(28,35))
