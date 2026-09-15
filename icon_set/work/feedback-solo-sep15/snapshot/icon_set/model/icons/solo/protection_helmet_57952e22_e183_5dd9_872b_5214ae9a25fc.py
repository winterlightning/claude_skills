"""protection-helmet: Smooth open-ridge hard hat; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '57952e22-e183-5dd9-872b-5214ae9a25fc'
SOURCE_PATH = 'pictographic-primitives/protection/protection helmet_57952e22-e183-5dd9-872b-5214ae9a25fc.svg'
AUTHOR = 'gpt-6'

class ProtectionHelmet(Solo48):
    icon_id = 'protection-helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('solo-ai-full-set', 'protection-helmet')

    def build(self):
        # Plan: Keep two separate reinforcing ribs and a broad brim; preserve the open-ridge variant.
        # Reference: Lucide hard-hat: original and atomic-debug geometry.

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
        path('crown',(7,31),[('L',(7,25)),('C',(19,8),(7,17),(13,9)),('L',(29,8)),('C',(41,25),(35,9),(41,17)),('L',(41,31))])
        path('brim',(7,31),[('L',(41,31)),('C',(44,35),(44,31),(44,32)),('C',(40,40),(44,39),(43,40)),('L',(8,40)),('C',(4,35),(5,40),(4,39)),('C',(7,31),(4,32),(4,31))],True);join('crown','brim')
        for x in [19,29]:line(f'rib-{x}',(x,8),(x,22));join(f'rib-{x}','crown')
