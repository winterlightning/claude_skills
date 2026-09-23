"""A three-binding calendar showing the arithmetic expression 2+1.
Plan: Three evenly repeated bindings with no header divider, matching the source. Hand-authored 2, plus and 1 remain in source order."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '14b5dacf-2ae7-4b43-b032-7129b3d49037'
SOURCE_PATH = 'icon_set/work/todo-references/calendar math_14b5dacf-2ae7-4b43-b032-7129b3d49037.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCES = ['calendar']
class Drawing(Solo48):
    icon_id = 'calendar-math'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('calendar', 'math')

    def path(self, name, start, commands, closed=False):
        members = []
        point = start
        for i, command in enumerate(commands):
            member = f"{name}-{i}"
            target = command[1]
            if command[0] == "L":
                self.add_line(member, point, target)
            else:
                self.add_arc(member, point, target, radius_x=command[2],
                             radius_y=command[3], sweep=command[4])
            members.append(member)
            point = target
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), [("A",(x+r,y),r,r,True),
                                  ("A",(x-r,y),r,r,True)], True)

    def browser(self):
        # VRECT_L gives the enclosed marks a taller content area.
        self.path("browser-top", (8,12), [("L",(8,8)),
            ("A",(12,4),4,4,True),("L",(36,4)),
            ("A",(40,8),4,4,True),("L",(40,12))])
        self.path("browser-right", (40,12), [("L",(40,40)),
            ("A",(36,44),4,4,True)])
        self.add_line("browser-bottom",(36,44),(12,44))
        self.path("browser-left", (12,44), [
            ("A",(8,40),4,4,True),("L",(8,12))])
        self.add_line("header",(8,12),(40,12))
        for name in ("browser-right","browser-left"):
            self.relate("connect",name,"browser-bottom")
            self.relate("connect",name,"browser-top")
        for name in ("browser-top","browser-right","browser-left"):
            self.relate("connect", name, "header")

    def calendar(self, header=True, three=False):
        # Repeated bindings terminate at the top rim; retain exact 8-unit header.
        rings = (14,24,34) if three else (14,34)
        top = [("L",(x,10)) for x in rings] + [("L",(38,10)),
            ("A",(42,14),4,4,True),("L",(42,18))]
        self.path("calendar-top",(6,18),[("L",(6,14)),
            ("A",(10,10),4,4,True)]+top)
        self.path("calendar-body",(42,18),[("L",(42,38)),
            ("A",(38,42),4,4,True),("L",(10,42)),
            ("A",(6,38),4,4,True),("L",(6,18))])
        self.relate("connect","calendar-top","calendar-body")
        for x in rings:
            name=f"binding-{x}"
            self.add_line(name,(x,6),(x,10))
            self.relate("connect",name,"calendar-top")
        if header:
            self.add_line("header",(6,18),(42,18))
            for name in ("calendar-top","calendar-body"):
                self.relate("connect",name,"header")

    def build(self):

        self.calendar(header=False,three=True)
        self.path("two",(12,23),[("A",(20,23),4,4,True),
            ("A",(18,27),5,5,True),("L",(12,34)),("L",(20,34))])
        self.add_polyline("plus-horizontal",(24,27),(28,27),(32,27))
        self.add_polyline("plus-vertical",(28,23),(28,27),(28,31))
        self.relate("connect","plus-horizontal","plus-vertical")
        self.add_polyline("one",(34,22),(37,20),(37,34))
