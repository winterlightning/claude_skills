"""sawmill: Clear sawmill blade; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e168add6-d08c-5ea9-9a91-bf194256b3a5'
SOURCE_PATH = 'pictographic-primitives/tools/sawmill_e168add6-d08c-5ea9-9a91-bf194256b3a5.svg'
AUTHOR = 'gpt-6'

class Sawmill(Solo48):
    icon_id = 'sawmill'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('solo-ai-full-set', 'sawmill')

    def build(self):
        # Plan: Preserve the irregular cutting teeth and lower opening. Use broad teeth rather than many thin spikes.
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
        path('blade',(9,42),[('L',(9,33)),('L',(6,25)),('L',(14,25)),('L',(11,15)),('L',(20,19)),('L',(21,6)),('L',(29,16)),('L',(35,10)),('L',(36,23)),('L',(40,42))])
        path('base',(6,42),[('L',(9,42)),('L',(17,42)),('L',(30,42)),('L',(40,42)),('L',(42,42))]);join('base','blade')
        path('opening',(17,42),[('C',(24,27),(17,31),(20,27)),('C',(30,42),(27,27),(30,31))]);join('opening','base')
