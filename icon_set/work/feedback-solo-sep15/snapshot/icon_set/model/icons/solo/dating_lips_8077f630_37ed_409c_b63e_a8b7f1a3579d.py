"""dating-lips: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8077f630-37ed-409c-b63e-a8b7f1a3579d'
SOURCE_PATH = 'pictographic-primitives/romance/dating lips_8077f630-37ed-409c-b63e-a8b7f1a3579d.svg'
AUTHOR = 'gpt-6'

class DatingLips(Solo48):
    icon_id = 'dating-lips'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('dating', 'lips', 'romance', 'solo-ai-next100')

    def build(self):
        # Plan: Keep a cupid-bow mouth with a broad lower lip and slight center dip. Mirror the lip halves for a natural balanced smile.
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
        path('lips',(4,24),[('C',(18,8),(9,16),(13,8)),('C',(24,11),(21,8),(22,11)),('C',(30,8),(26,11),(27,8)),('C',(44,24),(35,8),(39,16)),('C',(24,40),(39,34),(33,40)),('C',(4,24),(15,40),(9,34))],True)
        path('mouth',(4,24),[('L',(16,24)),('C',(24,26),(20,24),(20,26)),('C',(32,24),(28,26),(28,24)),('L',(44,24))]);join('mouth','lips')
