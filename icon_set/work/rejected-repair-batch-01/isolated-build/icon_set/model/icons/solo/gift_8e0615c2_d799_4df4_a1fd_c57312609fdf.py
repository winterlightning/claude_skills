"""gift: Smooth bow gift; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8e0615c2-d799-4df4-a1fd-c57312609fdf'
SOURCE_PATH = 'pictographic-primitives/holidays/gift_8e0615c2-d799-4df4-a1fd-c57312609fdf.svg'
AUTHOR = 'gpt-6'

class Gift(Solo48):
    icon_id = 'gift'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('solo-ai-full-set', 'gift')

    def build(self):
        # Plan: Preserve the plain box and two-loop bow. Mirror rounded loops and share their meeting point with the lid.
        # Reference: Lucide gift: original and atomic-debug geometry.

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
        path('box',(10,17),[('L',(24,17)),('L',(38,17)),('L',(38,44)),('L',(10,44)),('L',(10,17))],True)
        path('lid',(8,17),[('L',(10,17)),('L',(24,17)),('L',(38,17)),('L',(40,17))]);join('lid','box')
        path('left',(24,17),[('C',(12,9),(17,17),(12,15)),('C',(17,4),(12,6),(14,4)),('C',(24,17),(22,4),(24,12))],True)
        path('right',(24,17),[('C',(31,4),(24,12),(26,4)),('C',(36,9),(34,4),(36,6)),('C',(24,17),(36,15),(31,17))],True)
        join('left','right');join('left','box');join('right','box');join('left','lid');join('right','lid')
