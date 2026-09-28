"""christmas-sock: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2717434c-419a-5ee7-81cd-f47a96b06ddc'
SOURCE_PATH = 'pictographic-primitives/holidays/christmas sock_2717434c-419a-5ee7-81cd-f47a96b06ddc.svg'
AUTHOR = 'gpt-6'

class ChristmasSock(Solo48):
    icon_id = 'christmas-sock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('christmas', 'sock', 'holidays', 'solo-ai-next100')

    def build(self):
        # Plan: Retain a broad stocking cuff, long ankle and left-facing rounded toe. A coherent heel curve replaces the wavering trace.
        # Reference: Lucide sock original and atomic-debug construction.

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
        rounded('cuff',16,4,40,13,4)
        path('sock',(20,13),[('L',(20,24)),('L',(12,29)),('C',(8,36),(8,31),(8,33)),('C',(17,44),(8,41),(12,44)),('L',(30,40)),('C',(36,32),(35,39),(36,36)),('L',(36,13))]);join('sock','cuff')
