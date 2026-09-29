"""Restore an outlined head, forward skating lean, one bent supporting leg, a lifted rear leg, two boot strokes and paired wheel sets.
Construction reference: human_ref/full_body_ref.png: outlined head, flowing torso and connected bent limbs; source requires two visible skates."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '630e00b6-b3a3-4ec4-9e34-5b14d7140829'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__inline-skater/20260929T033618Z-thuan-mac/reference/rollerblades person_630e00b6-b3a3-4ec4-9e34-5b14d7140829.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'inline-skater'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('rollerblades person',)

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

        circle('head',28,8,4)
        path('torso',(28,20),[('C',(21,28),(28,23),(25,26))])
        poly('back-arm',(28,20),(18,20),(12,20));poly('front-arm',(28,20),(35,24),(42,24))
        poly('front-leg',(21,28),(30,32),(28,37));poly('back-leg',(21,28),(15,33),(8,31),(6,35))
        line('front-boot',(27,37),(36,37));line('back-boot',(6,35),(13,37))
        for j,(x,y) in enumerate([(6,41),(13,43),(28,43),(36,43)]):self.add_dot(f'wheel-{j}',(x,y))
        for n in ['back-arm','front-arm','front-leg','back-leg']:join('torso',n)
        join('back-arm','front-arm');join('front-leg','back-leg');join('front-leg','front-boot');join('back-leg','back-boot')
        self.mark_human_figure('skater',head='head',torso='torso-0',torso_junction='start')
