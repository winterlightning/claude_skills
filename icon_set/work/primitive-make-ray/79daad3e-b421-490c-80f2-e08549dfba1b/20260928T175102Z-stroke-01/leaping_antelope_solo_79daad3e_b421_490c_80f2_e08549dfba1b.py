"""Continuous outlined airborne body, bent foreleg, extended hind hoof, slender neck and swept horn. Preserve intentional forward motion and asymmetry.
Construction: No useful subject match; geometric construction from the supplied original."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '79daad3e-b421-490c-80f2-e08549dfba1b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__leaping-antelope-solo/20260928T175102Z-thuan-mac/reference/deer jump_79daad3e-b421-490c-80f2-e08549dfba1b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'leaping-antelope-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('deer jump',)

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

        path('deer',(4,40),[('L',(8,30)),('L',(12,28)),('L',(12,23)),('C',(27,16),(18,21),(23,18)),('L',(31,10)),('L',(36,10)),('L',(44,15)),('C',(38,18),(45,18),(41,18)),('L',(37,24)),('L',(42,24)),('L',(42,34)),('L',(38,31)),('L',(37,28)),('L',(21,34)),('L',(17,39)),('L',(4,40))],True)
        path('horn',(32,10),[('C',(34,8),(30,8),(31,8)),('L',(42,8))]);join('deer','horn')
        path('tail',(12,23),[('C',(6,20),(9,23),(7,22))]);join('deer','tail')
