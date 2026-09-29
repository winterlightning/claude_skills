"""Two figures with matching radius-4 heads. Therapist neck (15,22) lies 12 below head (15,10); patient neck (30,32) lies 12 left of head (42,32). Bent leg joins the reclined torso and therapist hand.
Construction: Shared human_ref/full_body_ref.png: equal circular heads and coherent torso/limb runs; source supplies the interacting pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4a608386-d726-47bd-b174-b25be1ff2bcc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__leg-massage-therapy-4a608386/20260928T175102Z-thuan-mac/reference/thai massage leg_4a608386-d726-47bd-b174-b25be1ff2bcc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'leg-massage-therapy-4a608386'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('thai massage leg',)

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

        circle('therapist-head',15,10,4)
        line('therapist-torso',(15,22),(15,31))
        poly('therapist-leg',(15,31),(8,40),(4,40))
        path('therapist-arm',(15,22),[('L',(23,26)),('L',(26,22))])
        circle('patient-head',42,32,4)
        line('patient-torso',(30,32),(23,32))
        poly('raised-leg',(23,32),(26,22),(21,18))
        path('resting-leg',(23,32),[('L',(16,37)),('L',(25,40))])
        join('therapist-torso','therapist-leg');join('therapist-torso','therapist-arm')
        join('therapist-arm','raised-leg');join('patient-torso','raised-leg');join('patient-torso','resting-leg');join('raised-leg','resting-leg')
        self.mark_human_figure('therapist',head='therapist-head',torso='therapist-torso',torso_junction='start')
        self.mark_human_figure('patient',head='patient-head',torso='patient-torso',torso_junction='start')
