"""ship: Smooth sailboat and waves; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6c02307a-7888-4391-827e-bb44ee69f25b'
SOURCE_PATH = 'icons-json/transportation/ship_6c02307a-7888-4391-827e-bb44ee69f25b.json'
AUTHOR = 'gpt-6'

class Ship(Solo48):
    icon_id = 'ship'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('solo-ai-full-set', 'ship')

    def build(self):
        # Plan: Preserve the curved sail and wave-shaped hull; draw the shared waterline once and attach the sail at exact deck nodes.
        # Reference: Original subject; preserve the distinctive silhouette and proportions.

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
        path('hull',(10,28),[('L',(18,28)),('L',(25,28)),('L',(38,28)),('L',(36,36)),('C',(24,40),(32,36),(28,40)),('C',(12,36),(20,40),(16,36)),('L',(10,28))],True)
        path('sail',(18,28),[('C',(18,8),(22,19),(20,12)),('C',(36,20),(28,8),(34,14)),('L',(25,28))]);join('sail','hull')
        path('wave-left',(4,40),[('C',(12,36),(8,40),(8,36))]);path('wave-right',(36,36),[('C',(44,40),(40,36),(40,40))]);join('wave-left','hull');join('wave-right','hull')
