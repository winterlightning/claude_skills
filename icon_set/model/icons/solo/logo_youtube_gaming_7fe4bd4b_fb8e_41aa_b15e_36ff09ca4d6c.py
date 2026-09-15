"""logo-youtube-gaming: Smooth broad gaming heart; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7fe4bd4b-fb8e-41aa-b15e-36ff09ca4d6c'
SOURCE_PATH = 'icons-json/video-games/logo youtube gaming_7fe4bd4b-fb8e-41aa-b15e-36ff09ca4d6c.json'
AUTHOR = 'gpt-6'

class LogoYoutubeGaming(Solo48):
    icon_id = 'logo-youtube-gaming'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('solo-ai-full-set', 'logo-youtube-gaming')

    def build(self):
        # Plan: Preserve the flattened side walls and shallow notch that distinguish this emblem.
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
        path('outline',(24,13),[('C',(34,8),(28,10),(29,8)),('C',(44,18),(40,8),(44,12)),('L',(44,23)),('C',(41,27),(44,25),(43,26)),('L',(24,40)),('L',(7,27)),('C',(4,23),(5,26),(4,25)),('L',(4,18)),('C',(14,8),(4,12),(8,8)),('C',(24,13),(19,8),(20,10))],True)
