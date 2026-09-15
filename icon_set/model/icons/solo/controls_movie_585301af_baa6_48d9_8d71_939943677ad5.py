"""controls-movie: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '585301af-baa6-48d9-8d71-939943677ad5'
SOURCE_PATH = 'pictographic-primitives/movies/controls movie_585301af-baa6-48d9-8d71-939943677ad5.svg'
AUTHOR = 'gpt-6'

class ControlsMovie(Solo48):
    icon_id = 'controls-movie'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'movies'
    aliases = ()
    keywords = ('controls', 'movie', 'movies', 'solo-ai-next100')

    def build(self):
        # Plan: Retain the clapperboard and diagonal upper stripes. Regular strip spacing and equal body corners smooth the original.
        # Reference: Lucide clapperboard original and atomic-debug construction.

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
        rounded('body',4,8,44,40,4);line('rim',(4,18),(44,18));join('rim','body')
        for a,b in [((10,18),(20,8)),((28,18),(38,8))]:line(f'stripe-{a[0]}',a,b);join(f'stripe-{a[0]}','body');join(f'stripe-{a[0]}','rim')
        line('lower',(4,32),(44,32));join('lower','body')
