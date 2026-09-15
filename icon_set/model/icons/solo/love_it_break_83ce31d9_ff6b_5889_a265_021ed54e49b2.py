"""love-it-break: Smooth broken heart; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '83ce31d9-ff6b-5889-a265-021ed54e49b2'
SOURCE_PATH = 'pictographic-primitives/social/love it break_83ce31d9-ff6b-5889-a265-021ed54e49b2.svg'
AUTHOR = 'gpt-6'

class LoveItBreak(Solo48):
    icon_id = 'love-it-break'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('solo-ai-full-set', 'love-it-break')

    def build(self):
        # Plan: Preserve the broad heart and attached zigzag crack; mirror the outer lobes with a roomy middle.
        # Reference: Lucide heart-crack: original and atomic-debug geometry.

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
        path('heart',(24,12),[('C',(14,8),(21,9),(18,8)),('C',(4,19),(7,8),(4,12)),('C',(24,40),(4,27),(18,36)),('C',(44,19),(30,36),(44,27)),('C',(34,8),(44,12),(41,8)),('C',(24,12),(30,8),(27,9))],True)
        path('crack',(24,12),[('L',(19,19)),('L',(25,25)),('L',(20,30))]);join('crack','heart')
