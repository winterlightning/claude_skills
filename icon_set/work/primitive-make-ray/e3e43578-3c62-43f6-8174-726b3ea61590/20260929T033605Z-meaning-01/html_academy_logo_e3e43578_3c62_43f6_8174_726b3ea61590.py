"""Restore the tall shield outline, diamond face, lower center seam and two diagonal face marks that distinguish the HTML Academy logo.
Construction reference: Supplied original; no useful local Lucide subject match."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e3e43578-3c62-43f6-8174-726b3ea61590'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__html-academy-logo/20260929T033618Z-thuan-mac/reference/html academy logo_e3e43578-3c62-43f6-8174-726b3ea61590.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'html-academy-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('html academy logo',)

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

        poly('shield',(8,8),(24,4),(40,8),(40,24),(40,34),(24,44),(8,34),(8,24),closed=True)
        poly('face',(8,24),(24,14),(40,24),(24,34),closed=True)
        line('seam',(24,34),(24,44));line('code-upper',(22,22),(27,25));line('code-lower',(20,27),(24,30))
        join('shield','face');join('shield','seam');join('face','seam')
