"""apostrophe: Smooth broad comma; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '62e2b2e8-283f-4653-a82c-ce0d21a9c989'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/apostrophe_62e2b2e8-283f-4653-a82c-ce0d21a9c989.svg'
AUTHOR = 'gpt-6'

class Apostrophe(Solo48):
    icon_id = 'apostrophe'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('solo-ai-full-set', 'apostrophe')

    def build(self):
        # Plan: Retain the rounded head and tail; make the inner scoop broad enough to read at native size.
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
        path('mark',(12,44),[('C',(40,17),(31,41),(40,31)),('C',(24,4),(40,7),(32,4)),('C',(8,15),(14,4),(8,8)),('C',(24,23),(8,24),(19,21)),('C',(12,44),(31,29),(22,40))],True)
