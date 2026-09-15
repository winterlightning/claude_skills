"""lock-interface-essential: Even lock body and shackle; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '386cb547-821f-4d23-a0b8-bb7f43205473'
SOURCE_PATH = 'pictographic-primitives/interface-essential/lock_386cb547-821f-4d23-a0b8-bb7f43205473.svg'
AUTHOR = 'gpt-6'

class LockInterfaceEssential(Solo48):
    icon_id = 'lock-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('solo-ai-full-set', 'lock-interface-essential')

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
        path('body',(11,19),[('L',(12,19)),('L',(36,19)),('L',(38,19)),('A',(40,21),2,2,True),('L',(40,42)),('A',(38,44),2,2,True),('L',(10,44)),('A',(8,42),2,2,True),('L',(8,21)),('A',(10,19),2,2,True),('L',(11,19))],True)
        path('shackle',(12,19),[('L',(12,16)),('A',(36,16),12,12,True),('L',(36,19))]);join('shackle','body')
        line('slot',(24,28),(24,33))
