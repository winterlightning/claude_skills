"""lift-hook-box: Clean lifting sling; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c368d189-0003-5241-889d-bf5b16aa99f6'
SOURCE_PATH = 'pictographic-primitives/construction/lift hook box_c368d189-0003-5241-889d-bf5b16aa99f6.svg'
AUTHOR = 'gpt-6'

class LiftHookBox(Solo48):
    icon_id = 'lift-hook-box'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    categories = ('construction', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('solo-ai-full-set', 'lift-hook-box')

    def build(self):
        # Plan: The two sling straps share exact box attachment nodes; remove the retraced top edge.
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
        path('box',(8,23),[('L',(13,23)),('L',(35,23)),('L',(40,23)),('L',(40,44)),('L',(8,44)),('L',(8,23))],True)
        path('sling',(13,23),[('L',(24,10)),('L',(35,23))]);line('hook',(24,4),(24,10));join('sling','box');join('hook','sling')
