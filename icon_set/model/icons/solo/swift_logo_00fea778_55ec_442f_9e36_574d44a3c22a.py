"""swift-logo: Smooth flying bird emblem; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '00fea778-55ec-442f-9e36-574d44a3c22a'
SOURCE_PATH = 'icons-json/logos/swift logo_00fea778-55ec-442f-9e36-574d44a3c22a.json'
AUTHOR = 'gpt-6'

class SwiftLogo(Solo48):
    icon_id = 'swift-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('solo-ai-full-set', 'swift-logo')

    def build(self):
        # Plan: Preserve the swept wings and hooked flying-bird outline; broad returning curves retain the asymmetrical flight gesture.
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
        path('bird',(4,16),[('L',(25,28)),('L',(10,8)),('L',(29,21)),('C',(30,8),(36,23),(34,15)),('C',(39,30),(42,17),(40,24)),('C',(44,39),(43,32),(44,35)),('C',(34,36),(40,36),(37,35)),('C',(22,40),(30,38),(27,40)),('C',(4,32),(14,40),(8,36)),('L',(18,31)),('C',(4,16),(12,27),(7,23))],True)
