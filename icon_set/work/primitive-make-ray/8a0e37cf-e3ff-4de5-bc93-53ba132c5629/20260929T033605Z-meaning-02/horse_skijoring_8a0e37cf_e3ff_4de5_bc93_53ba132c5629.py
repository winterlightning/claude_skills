"""Separate a crouching skier behind the horse, with a long ski and a taut tow line to the horse harness. Restore the horse muzzle, curved neck, body and two legs.
Construction reference: human_ref/full_body_ref.png: circular head, bent limbs; source defines the ski/tow-line/horse relationship."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8a0e37cf-e3ff-4de5-bc93-53ba132c5629'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horse-skijoring/20260929T033618Z-thuan-mac/reference/skijoring_8a0e37cf-e3ff-4de5-bc93-53ba132c5629.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horse-skijoring'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('skijoring',)

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

        circle('head',10,7,3)
        path('torso',(10,18),[('C',(7,27),(10,21),(8,24))])
        poly('arm',(10,18),(16,23),(20,23))
        poly('skier-leg',(7,27),(13,31),(11,40))
        path('ski',(3,40),[('L',(11,40)),('L',(17,40)),('A',(20,37),3,3,False)])
        line('tow-rope',(20,23),(32,26))
        path('horse',(24,40),[('L',(24,30)),('C',(28,26),(24,27),(26,26)),('L',(32,26)),('C',(37,15),(33,20),(33,16)),('L',(40,14)),('L',(39,18)),('L',(45,23)),('L',(40,24)),('L',(38,30)),('L',(38,40))])
        line('belly',(24,33),(38,33))
        for n in ['arm','skier-leg']:join('torso',n)
        join('arm','tow-rope');join('horse','belly');join('tow-rope','horse');join('skier-leg','ski')
        self.mark_human_figure('skier',head='head',torso='torso-0',torso_junction='start')
