"""Restore a curved horse back, sloping neck, muzzle, pointed ear and bent foreleg. Draw a separate circular rider head, leaning torso and bent seated leg, preserving the source close crop.
Construction reference: human_ref/full_body_ref.png: outlined head and coherent bent limbs; source defines equestrian action."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '932e176d-8abb-4412-94f0-22f2542b288a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horse-rider/20260929T033618Z-thuan-mac/reference/sport horse riding_932e176d-8abb-4412-94f0-22f2542b288a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horse-rider'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('sport horse riding',)

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

        path('horse',(4,33),[('C',(15,27),(6,28),(10,27)),('L',(28,27)),('L',(33,17)),('L',(36,14)),('L',(36,18)),('L',(44,25)),('C',(41,28),(46,27),(43,29)),('L',(35,26)),('L',(30,35)),('L',(35,39)),('L',(34,44))])
        poly('foreleg',(30,35),(27,39),(26,44));join('horse','foreleg')
        circle('head',24,8,4)
        path('torso',(24,20),[('C',(18,27),(24,23),(20,24))])
        poly('arm',(24,20),(29,25),(33,24))
        poly('rider-leg',(18,27),(22,33),(18,39))
        join('torso','arm');join('torso','rider-leg');join('rider-leg','horse')
        self.mark_human_figure('rider',head='head',torso='torso-0',torso_junction='start')
