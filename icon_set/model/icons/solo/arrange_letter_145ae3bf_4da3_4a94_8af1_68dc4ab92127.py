"""arrange-letter: Clear A-to-Z sorting mark; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '145ae3bf-4da3-4a94-8af1-68dc4ab92127'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/arrange letter_145ae3bf-4da3-4a94-8af1-68dc4ab92127.svg'
AUTHOR = 'gpt-6'

class ArrangeLetter(Solo48):
    icon_id = 'arrange-letter'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('solo-ai-full-set', 'arrange-letter')

    def build(self):
        # Plan: Preserve the downward arrow and A/Z letters; enlarge the A counter and share its crossbar nodes.
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
        line('arrow',(13,10),(13,35));path('head',(8,29),[('L',(13,35)),('L',(18,29))]);join('arrow','head')
        path('a',(26,18),[('L',(28,14)),('L',(33,4)),('L',(38,14)),('L',(40,18))]);line('bar',(28,14),(38,14));join('bar','a')
        poly('z',(26,29),(40,29),(26,44),(40,44))
