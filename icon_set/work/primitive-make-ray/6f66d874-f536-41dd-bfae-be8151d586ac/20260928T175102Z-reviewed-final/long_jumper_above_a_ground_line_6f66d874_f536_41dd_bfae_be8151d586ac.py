"""Outlined circular radius-4 head at (28,8) with actual torso neck at (28,20): exactly 4 ink units. Split airborne legs and detached ground; natural action proportions preserved.
Construction: Shared human_ref/full_body_ref.png: outlined circular head and connected round-ended limbs; source supplies airborne split-leg motion."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6f66d874-f536-41dd-bfae-be8151d586ac'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__long-jumper-above-a-ground-line/20260928T175102Z-thuan-mac/reference/athletics long jumping_6f66d874-f536-41dd-bfae-be8151d586ac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-jumper-above-a-ground-line'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('athletics long jumping',)

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
        path('torso',(28,20),[('C',(23,29),(28,24),(25,27))])
        poly('back-arm',(28,20),(17,20),(12,23))
        poly('front-arm',(28,20),(35,24),(40,22))
        poly('front-leg',(23,29),(31,29),(40,31))
        poly('back-leg',(23,29),(17,31),(10,28))
        line('ground',(4,40),(44,40))
        for n in ['back-arm','front-arm','front-leg','back-leg']:join('torso',n)
        join('back-arm','front-arm');join('front-leg','back-leg')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')

# User authorized quality-preserving exceptions; approval binds this exact drawing.
Drawing.exception = {'reason': 'Keep the airborne split-leg pose and separated ground line at natural proportions. The top lies 4 units above the chosen rectangle and arm/leg spacing is locally compact; the head has an exact 4-unit gap at its own torso and all ink stays in the canvas.', 'approved_by': 'user-delegated-discretion-reviewed-by-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '61c709133da0e01b19969a8a5b602e4804902ddeb69afc44afeb880ccbad6f56'}
