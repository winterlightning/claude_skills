"""arrow-circle-bottom-4: Smooth open ring arrow; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '114deb1b-00c7-5f63-92e5-a85bd467378b'
SOURCE_PATH = 'icons-json/arrows/arrow circle bottom 4_114deb1b-00c7-5f63-92e5-a85bd467378b.json'
AUTHOR = 'gpt-6'

class ArrowCircleBottom4(Solo48):
    icon_id = 'arrow-circle-bottom-4'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('solo-ai-full-set', 'arrow-circle-bottom-4')

    def build(self):
        # Plan: Lucide circle-arrow-down: coherent circular arcs and a mirrored arrowhead. Keep the attached shaft; the free ring end is ten centerline units from it, and the tip is ten units from the opposite rim.

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
        def pt(x,y):return (48-y,x) if 'down'=='left' else (x,y)
        path('ring',pt(24,6),[('A',pt(6,24),18,18,False),('A',pt(24,42),18,18,False),('A',pt(42,24),18,18,False),('C',pt(34,9),pt(42,17),pt(39,11))])
        line('shaft',pt(24,6),pt(24,32));join('shaft','ring')
        path('head',pt(17,25),[('L',pt(24,32)),('L',pt(31,25))]);join('head','shaft')
