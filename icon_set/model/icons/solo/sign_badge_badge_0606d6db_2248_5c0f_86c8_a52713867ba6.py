"""sign-badge-badge: Smooth shield shoulders; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0606d6db-2248-5c0f-86c8-a52713867ba6'
SOURCE_PATH = 'icons-json/maps/sign badge badge_0606d6db-2248-5c0f-86c8-a52713867ba6.json'
AUTHOR = 'gpt-6'

class SignBadgeBadge(Solo48):
    icon_id = 'sign-badge-badge'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('solo-ai-full-set', 'sign-badge-badge')

    def build(self):
        # Plan: Keep the crown and curved shield base; broaden the crown shoulders without narrowing the side scallops.
        # Reference: Lucide shield: original and atomic-debug geometry.

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
        path('shield',(8,10),[('L',(12,4)),('L',(18,8)),('L',(24,4)),('L',(30,8)),('L',(36,4)),('L',(40,10)),('C',(37,19),(38,14),(37,16)),('C',(40,29),(37,23),(40,25)),('C',(24,44),(40,36),(31,41)),('C',(8,29),(17,41),(8,36)),('C',(11,19),(8,25),(11,23)),('C',(8,10),(11,16),(10,14))],True)
