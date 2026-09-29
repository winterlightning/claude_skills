"""Rounded square enclosing a small dot, italic i and smooth n with a finishing hook; lettering remains an intentional compact logo exception if required.
Construction: No useful subject match; geometric construction from the supplied original."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6742b2e4-0a48-4b9c-a3b9-fddbfa96da87'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__invision-logo/20260928T175102Z-thuan-mac/reference/invision logo_6742b2e4-0a48-4b9c-a3b9-fddbfa96da87.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'invision-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('invision logo',)

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

        rounded('frame',6,6,42,42,5)
        self.add_dot('dot',(17,15))
        path('i',(16,23),[('L',(13,32)),('C',(18,33),(12,36),(16,36))])
        path('n',(22,34),[('L',(25,23)),('C',(34,27),(30,19),(36,21)),('L',(32,32)),('C',(37,33),(31,36),(35,36))])

# User authorized quality-preserving exceptions; approval binds this exact drawing.
Drawing.exception = {'reason': 'Retain the complete rounded-square InVision logo and compact italic lettering. The frame, i dot and n are legible at 48 px; logo-specific inner spacing is accepted.', 'approved_by': 'user-delegated-discretion-reviewed-by-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'b5289f9bcd92f9e6f468245bc15a2acc7c96041e690ce665327a605cf502629c'}
