"""tank-top: Balanced sleeveless top; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '39361dc4-7a27-511a-8675-7fff10adc8f5'
SOURCE_PATH = 'icons-json/clothes/tank top_39361dc4-7a27-511a-8675-7fff10adc8f5.json'
AUTHOR = 'gpt-6'

class TankTop(Solo48):
    icon_id = 'tank-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('solo-ai-full-set', 'tank-top')

    def build(self):
        # Plan: Equal shoulder straps and armholes; preserve the neckline and gently flared source hem.
        # Reference: Lucide shirt: original and atomic-debug geometry.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
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
        commands=[('L',(20,4))]
        if 'round'=='round':commands += [('C',(28,4),(20,18),(28,18))]
        else:commands += [('L',(24,18)),('L',(28,4))]
        commands += [('L',(36,4)),('C',(40,20),(36,15),(36,16))]
        if 'curve'=='curve':commands += [('C',(40,42),(37,30),(38,34)),('C',(24,44),(36,44),(30,44)),('C',(8,42),(18,44),(12,44)),('C',(8,20),(10,34),(11,30))]
        else:commands += [('L',(40,44)),('L',(8,44)),('L',(8,20))]
        commands += [('C',(12,4),(12,16),(12,15))]
        path('top',(12,4),commands,True)
