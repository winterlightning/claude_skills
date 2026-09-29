"""Restore the pipe collar, two curved falling streams and two coherent water-wave rows. Retain the source left-hand pipe and right-hand discharge direction.
Construction reference: Supplied original; smooth coherent wave curves follow shared geometric construction."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dc6d6d2c-1086-4a91-b19c-cf01bbb00c04'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-discharge-pipe-above-two-wave-rows/20260929T033618Z-thuan-mac/reference/pollution faucet water_dc6d6d2c-1086-4a91-b19c-cf01bbb00c04.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-discharge-pipe-above-two-wave-rows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('pollution faucet water',)

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

        poly('pipe',(4,10),(24,10),(24,22),(4,22))
        poly('collar',(24,7),(32,7),(32,25),(24,25),closed=True);join('pipe','collar')
        poly('upper-fitting',(4,4),(12,4),(12,10));join('pipe','upper-fitting')
        path('stream-one',(38,16),[('C',(44,23),(41,17),(43,21))])
        path('stream-two',(38,26),[('C',(41,29),(39,27),(40,28))])
        for name,y in [('wave-top',35),('wave-bottom',44)]:
            path(name,(4,y),[('C',(14,y-3),(9,y+1),(11,y-1)),('C',(24,y),(17,y+1),(20,y+1)),('C',(34,y-3),(28,y+1),(31,y-1)),('C',(44,y),(38,y+1),(41,y+1))])

# User authorized quality-preserving exceptions; approval binds this exact drawing.
Drawing.exception = {'reason': 'Keep the pipe collar, two distinct falling streams and two smooth wave rows. The tall scene envelope and local stream/wave gaps retain the discharge meaning while all ink remains on canvas.', 'approved_by': 'user-delegated-discretion-reviewed-by-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '4d96d6358f689a234d5dcd68722334d70b63f7a703660ccd45b12b83d915090a'}
