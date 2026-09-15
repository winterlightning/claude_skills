"""signature-sign-interface-essential: Flowing signature stroke; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c8c50287-9505-4d7a-9b3a-91b9a790ffa6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/signature sign_c8c50287-9505-4d7a-9b3a-91b9a790ffa6.svg'
AUTHOR = 'gpt-6'

class SignatureSignInterfaceEssential(Solo48):
    icon_id = 'signature-sign-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('solo-ai-full-set', 'signature-sign-interface-essential')

    def build(self):
        # Plan: Retain the tall first loop and smaller finishing loop; broaden their separation without changing the handwriting direction.
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
        path('signature',(4,40),[('L',(15,14)),('C',(23,8),(18,8),(20,8)),('C',(21,24),(29,8),(24,17)),('C',(19,40),(17,33),(16,40)),('C',(33,24),(24,40),(29,24)),('C',(37,31),(39,19),(40,24)),('C',(39,40),(34,37),(36,40)),('C',(44,35),(42,40),(43,37))])
