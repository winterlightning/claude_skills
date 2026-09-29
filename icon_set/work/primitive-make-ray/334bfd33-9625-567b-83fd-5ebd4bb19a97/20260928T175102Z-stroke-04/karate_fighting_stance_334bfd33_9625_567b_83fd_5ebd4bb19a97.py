"""Shared human reference: circular radius-4 head at (24,10), neck at (24,22), exactly four visible units apart. Bent guard and grounded wide stance.
Construction: Shared human_ref/full_body_ref.png: circular head, coherent round-ended limbs; no useful Lucide pose match."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '334bfd33-9625-567b-83fd-5ebd4bb19a97'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__karate-fighting-stance/20260928T175102Z-thuan-mac/reference/martial arts karate_334bfd33-9625-567b-83fd-5ebd4bb19a97.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'karate-fighting-stance'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('martial arts karate',)

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

        circle('head',24,10,4)
        path('torso',(24,22),[('C',(22,30),(24,25),(23,28))])
        path('guard',(24,22),[('L',(33,25)),('L',(38,16)),('L',(42,16))])
        path('other-arm',(24,22),[('L',(16,22)),('L',(10,28)),('L',(16,28))])
        poly('legs',(6,42),(16,32),(22,30),(32,33),(38,42))
        for name in ['guard','other-arm','legs']:join('torso',name)
        join('guard','other-arm')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
