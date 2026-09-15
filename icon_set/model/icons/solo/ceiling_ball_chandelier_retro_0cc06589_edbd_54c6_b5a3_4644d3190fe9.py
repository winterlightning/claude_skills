"""ceiling-ball-chandelier-retro: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0cc06589-edbd-54c6-b5a3-4644d3190fe9'
SOURCE_PATH = 'icons-json/lamps/ceiling ball chandelier retro_0cc06589-edbd-54c6-b5a3-4644d3190fe9.json'
AUTHOR = 'gpt-6'

class CeilingBallChandelierRetro(Solo48):
    icon_id = 'ceiling-ball-chandelier-retro'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'lamps'
    aliases = ()
    keywords = ('ceiling', 'ball', 'chandelier', 'retro', 'lamps', 'solo-ai-next100')

    def build(self):
        # Plan: Three round globes hang at equal spacing from one level arm; matched radii keep the fixture balanced.
        # Reference: Lucide lamp-ceiling original and atomic-debug construction.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L":
                    self.add_line(ident, here, end)
                elif kind == "A":
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == "C":
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [("A",(cx+r,cy),r,r,True), ("A",(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ("L",(x1-r,y0)), ("A",(x1,y0+r),r,r,True),
                ("L",(x1,y1-r)), ("A",(x1-r,y1),r,r,True),
                ("L",(x0+r,y1)), ("A",(x0,y1-r),r,r,True),
                ("L",(x0,y0+r)), ("A",(x0+r,y0),r,r,True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate("connect",a,b)
        line('ceiling',(18,8),(30,8));poly('stem',(24,8),(24,20),(24,32));join('stem','ceiling')
        poly('arm',(8,32),(8,20),(24,20),(40,20),(40,32));join('arm','stem')
        for x in (8,24,40):
         path(f'globe-{x}',(x,32),[('A',(x,40),4,4,True),('A',(x,32),4,4,True)],True);join(f'globe-{x}','stem' if x==24 else 'arm')
