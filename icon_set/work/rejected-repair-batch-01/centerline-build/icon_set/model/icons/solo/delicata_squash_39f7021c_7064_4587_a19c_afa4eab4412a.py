"""delicata-squash: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '39f7021c-7064-4587-a19c-afa4eab4412a'
SOURCE_PATH = 'pictographic-primitives/food/delicata squash_39f7021c-7064-4587-a19c-afa4eab4412a.svg'
AUTHOR = 'gpt-6'

class DelicataSquash(Solo48):
    icon_id = 'delicata-squash'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('delicata', 'squash', 'food', 'solo-ai-next100')

    def build(self):
        # Plan: Preserve the diagonal oval squash and single lengthwise rib. A smooth oval with pointed poles replaces the irregular trace.
        # Reference: No useful exact Lucide match; supplied original silhouette.

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
        path('squash',(6,42),[('C',(38,10),(6,20),(21,6)),('C',(6,42),(42,25),(27,42))],True)
        poly('rib',(6,42),(38,10),(42,6));join('rib','squash')
