"""tools-palette-spatula: Smooth broad spatula; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18b1c5aa-cd32-5607-b7e3-25fee7ebcc4d'
SOURCE_PATH = 'icons-json/tools/tools palette spatula_18b1c5aa-cd32-5607-b7e3-25fee7ebcc4d.json'
AUTHOR = 'gpt-6'

class ToolsPaletteSpatula(Solo48):
    icon_id = 'tools-palette-spatula'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('solo-ai-full-set', 'tools-palette-spatula')

    def build(self):
        # Plan: Preserve the broad flat blade and narrow rounded grip, with balanced shoulders and one shared blade edge.
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
        path('tool',(8,4),[('L',(40,4)),('L',(35,21)),('L',(33,27)),('L',(28,31)),('L',(30,40)),('C',(24,44),(31,43),(28,44)),('C',(18,40),(20,44),(17,43)),('L',(20,31)),('L',(15,27)),('L',(13,21)),('L',(8,4))],True)
        line('edge',(13,21),(35,21));join('edge','tool')
