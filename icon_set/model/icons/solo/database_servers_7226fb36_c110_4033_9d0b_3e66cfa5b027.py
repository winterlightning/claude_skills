"""database-servers: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7226fb36-c110-4033-9d0b-3e66cfa5b027'
SOURCE_PATH = 'icons-json/servers/database_7226fb36-c110-4033-9d0b-3e66cfa5b027.json'
AUTHOR = 'gpt-6'

class DatabaseServers(Solo48):
    icon_id = 'database-servers'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'servers'
    aliases = ()
    keywords = ('database', 'servers', 'solo-ai-next100')

    def build(self):
        # Plan: Preserve the stacked cylindrical database, with level elliptical rings and exact side contacts. Ring count and rim depth retain its source structure.
        # Reference: Lucide database original and atomic-debug construction.

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
        path('top',(8,10),[('A',(40,10),16,6,True),('A',(8,10),16,6,True)],True)
        path('body',(8,10),[('L',(8,38)),('A',(40,38),16,6,False),('L',(40,10))]);join('body','top')
        for y in [26]:
         path(f'ring-{y}',(8,y),[('A',(40,y),16,6,False)]);join(f'ring-{y}','body')
