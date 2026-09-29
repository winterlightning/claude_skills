"""Radius-4 head at (17,8); upper torso starts (17,20), initially vertical, then bends into the hip. Head-to-neck ink gap exactly 4. Raised right leg and bent guard.
Construction: Shared human_ref/full_body_ref.png: circular outlined head and simple bent limbs; source pose supplies the high kick."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8ec365ec-24ce-4d98-9b7f-1d62e79035fa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__karate-high-kick/20260928T175102Z-thuan-mac/reference/karate_8ec365ec-24ce-4d98-9b7f-1d62e79035fa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'karate-high-kick'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('karate',)

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

        circle('head',17,8,4)
        path('torso',(17,20),[('C',(26,32),(17,25),(21,29))])
        poly('guard',(17,20),(27,18),(29,13))
        poly('arm',(17,20),(8,28),(13,32))
        poly('legs',(26,44),(26,32),(40,8))
        for name in ['guard','arm','legs']:join('torso',name)
        join('guard','arm')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
