"""classical-piano: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a53bd27a-5806-5a97-81ac-1e6b26e8a953'
SOURCE_PATH = 'icons-json/music/classical piano_a53bd27a-5806-5a97-81ac-1e6b26e8a953.json'
AUTHOR = 'gpt-6'

class ClassicalPiano(Solo48):
    icon_id = 'classical-piano'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'music'
    aliases = ()
    keywords = ('classical', 'piano', 'music', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the asymmetric grand-piano lid and broad keyboard, with level legs and a smooth shoulder.
        # Reference: Lucide piano original and atomic-debug construction.

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
        path('lid',(12,26),[('L',(12,6)),('L',(20,6)),('C',(32,16),(24,6),(23,16)),('L',(36,16)),('A',(42,22),6,6,True),('L',(42,26))])
        poly('keys',(10,26),(42,26),(42,36),(6,36),(10,26));join('keys','lid')
        for x in (12,36):line(f'leg-{x}',(x,36),(x,42));join(f'leg-{x}','keys')
