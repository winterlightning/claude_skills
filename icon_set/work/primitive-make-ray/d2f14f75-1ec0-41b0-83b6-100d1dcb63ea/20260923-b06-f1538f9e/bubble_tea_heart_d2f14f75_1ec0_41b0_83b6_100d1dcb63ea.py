"""A tapered bubble-tea cup with straw, horizontal lid and heart motif.
Plan: Cup and centered straw on x=24, mirrored cup walls and heart lobes. VRECT_L gives the upright straw room, extremes 8,4,40,44."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd2f14f75-1ec0-41b0-83b6-100d1dcb63ea'
SOURCE_PATH = 'icon_set/work/todo-references/bubble tea heart_d2f14f75-1ec0-41b0-83b6-100d1dcb63ea.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCES = ['cup-soda', 'heart']
class Drawing(Solo48):
    icon_id = 'bubble-tea-heart'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('bubble', 'tea', 'heart')

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

        self.add_polyline("lid",(8,12),(24,12),(40,12))
        self.add_line("straw",(24,4),(24,12))
        self.relate("connect","straw","lid")
        self.path("cup",(8,12),[("L",(10,40)),
            ("A",(14,44),4,4,False),("L",(34,44)),
            ("A",(38,40),4,4,False),("L",(40,12))])
        self.relate("connect","cup","lid")
        self.path("heart",(24,25),[("A",(18,25),3,3,False),
            ("A",(19,29),6,6,False),("L",(24,35)),
            ("L",(29,29)),("A",(30,25),6,6,False),
            ("A",(24,25),3,3,False)],True)
