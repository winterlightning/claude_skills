"""lock-8eddc674: Even lock body and shackle; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8eddc674-39c0-4593-ad1f-6dac5d32c78c'
SOURCE_PATH = 'pictographic-primitives/interface-essential/lock_8eddc674-39c0-4593-ad1f-6dac5d32c78c.svg'
AUTHOR = 'gpt-6'

class Lock8eddc674(Solo48):
    icon_id = 'lock-8eddc674'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'lock-8eddc674')

    def build(self):
        # Plan: Match body corner radii and center the key slot; preserve the rounded U-shaped shackle.
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
        path('body',(11,18),[('L',(12,18)),('L',(36,18)),('L',(37,18)),('A',(40,21),3,3,True),('L',(40,41)),('A',(37,44),3,3,True),('L',(11,44)),('A',(8,41),3,3,True),('L',(8,21)),('A',(11,18),3,3,True),('L',(11,18))],True)
        path('shackle',(12,18),[('L',(12,16)),('A',(36,16),12,12,True),('L',(36,18))]);join('shackle','body')
        line('slot',(24,28),(24,33))
