"""Bound Notebook.
Plan: SQUARE, centerline bounds (6,6)-(42,42), complete standalone subject.
Construction: Lucide notebook informs repeated binding marks. Source owns the left inset binding line and three short crossbars; equally spaced by9.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '16275d53-14c4-4703-9919-0a8c59efc967'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/archive_16275d53-14c4-4703-9919-0a8c59efc967.svg'
AUTHOR = "gpt-6"
class Batch05Icon10(Solo48):
    icon_id = 'bound-notebook'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "content"
    aliases = ('bound-notebook',)
    keywords = ('bound', 'notebook')
    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for i, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{i}"
                if kind == "L": self.add_line(member, here, end)
                elif kind == "A": self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == "C": self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, radius):
            path(name,(cx,cy-radius),[("A",(cx+radius,cy),radius,radius,True),("A",(cx,cy+radius),radius,radius,True),("A",(cx-radius,cy),radius,radius,True),("A",(cx,cy-radius),radius,radius,True)],True)
        path("cover",(12,6),[("L",(20,6)),("L",(36,6)),("A",(42,12),6,6,True),("L",(42,36)),("A",(36,42),6,6,True),("L",(12,42)),("A",(6,36),6,6,True),("L",(6,12)),("A",(12,6),6,6,True)],True)
        self.add_polyline("binding",(20,6),(20,14),(20,23),(20,32));self.relate("connect","binding","cover")
        for i,y in enumerate((14,23,32)):
            k=f"ring-{i}";self.add_polyline(k,(14,y),(20,y),(26,y));self.relate("connect",k,"binding")
