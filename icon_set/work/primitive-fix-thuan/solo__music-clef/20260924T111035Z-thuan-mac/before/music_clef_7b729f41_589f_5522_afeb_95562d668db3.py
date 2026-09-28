"""music-clef: Flowing treble clef; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7b729f41-589f-5522-afeb-95562d668db3'
SOURCE_PATH = 'pictographic-primitives/music/music clef_7b729f41-589f-5522-afeb-95562d668db3.svg'
AUTHOR = 'gpt-6'

class MusicClef(Solo48):
    icon_id = 'music-clef'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'music'
    aliases = ()
    keywords = ('solo-ai-full-set', 'music-clef')

    def build(self):
        # Plan: Preserve the upper loop, broad lower loop and hooked stem. Use coherent sweeps with real crossing nodes.
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
        path('stem',(24,25),[('L',(19,7)),('C',(30,4),(21,4),(26,4)),('C',(33,11),(36,4),(37,8)),('C',(24,19),(31,14),(27,16)),('C',(8,29),(16,22),(8,24)),('C',(24,34),(8,33),(17,34)),('C',(40,29),(31,34),(40,33)),('C',(24,25),(40,23),(31,24)),('L',(28,41)),('C',(18,44),(28,44),(22,44)),('L',(18,44))])
