"""satellite: Smooth satellite dish; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '89743831-f496-4d64-9252-39621b32abcc'
SOURCE_PATH = 'pictographic-primitives/tv/satellite_89743831-f496-4d64-9252-39621b32abcc.svg'
AUTHOR = 'gpt-6'

class Satellite(Solo48):
    icon_id = 'satellite'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    aliases = ()
    keywords = ('solo-ai-full-set', 'satellite')

    def build(self):
        # Plan: Preserve the diagonal bowl, feed and triangular pedestal. Split the bowl at two exact stand attachments.
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
        path('dish',(12,6),[('L',(24,18)),('L',(42,36)),('C',(25,32),(36,36),(31,35)),('C',(14,28),(21,31),(17,30)),('C',(6,20),(9,25),(6,23)),('C',(12,6),(6,14),(8,10))],True)
        poly('base',(14,28),(6,42),(30,42),(25,32));join('base','dish')
        line('feed',(24,18),(34,10));path('receiver',(34,10),[('A',(38,6),4,4,True),('A',(42,10),4,4,True),('A',(38,14),4,4,True),('A',(34,10),4,4,True)],True);join('receiver','feed');join('feed','dish')
