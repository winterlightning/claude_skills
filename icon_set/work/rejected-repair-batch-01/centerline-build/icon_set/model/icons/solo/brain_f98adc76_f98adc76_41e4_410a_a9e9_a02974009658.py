"""brain-f98adc76: Rounded anatomical lobes; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f98adc76-41e4-410a-a9e9-a02974009658'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain_f98adc76-41e4-410a-a9e9-a02974009658.svg'
AUTHOR = 'gpt-6'

class BrainF98adc76(Solo48):
    icon_id = 'brain-f98adc76'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('solo-ai-next50-refine', 'solo-ai-next50', 'brain-f98adc76')

    def build(self):
        # Plan: The original side-view brain retains its high lobed crown, small lower-left lobe and larger right lobe. Two curved sulci describe those masses instead of generic vertical slots. Deliberate anatomical asymmetry.
        # Reference: Lucide brain: original and atomic-debug geometry.

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
        path('brain',(6,28),[
         ('C',(11,18),(6,23),(7,20)),
         ('C',(20,7),(11,11),(14,7)),
         ('C',(25,9),(22,7),(24,8)),
         ('C',(31,6),(27,7),(29,6)),
         ('C',(37,14),(35,6),(37,10)),
         ('C',(42,25),(41,15),(42,20)),
         ('C',(39,34),(42,29),(39,30)),
         ('C',(33,42),(39,39),(37,42)),
         ('C',(27,39),(30,42),(28,40)),
         ('C',(22,41),(25,41),(24,41)),
         ('C',(16,37),(19,41),(17,39)),
         ('C',(12,38),(14,38),(13,38)),
         ('C',(6,28),(8,38),(6,34))],True)
        path('upper-fold',(25,9),[('C',(21,22),(22,12),(21,18))]);join('upper-fold','brain')
        path('lower-fold',(27,39),[('C',(29,24),(24,33),(26,27))]);join('lower-fold','brain')
