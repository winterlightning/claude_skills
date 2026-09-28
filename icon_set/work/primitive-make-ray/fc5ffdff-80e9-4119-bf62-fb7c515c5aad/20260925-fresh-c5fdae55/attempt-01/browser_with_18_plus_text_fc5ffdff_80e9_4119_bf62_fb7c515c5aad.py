"""A two-binding calendar-like browser displaying 18+ as in the source.
Plan: Calendar enclosure contains hand-authored 1, two circular lobes of 8 and plus; all three characters retained."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fc5ffdff-80e9-4119-bf62-fb7c515c5aad'
SOURCE_PATH = 'pictographic-primitives/other/browser with 18+ text_fc5ffdff-80e9-4119-bf62-fb7c515c5aad.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = ['calendar']
PLAN = 'Retain bindings, header and horizontal 18+; rebalance digit and operator spacing without dropping characters.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/fc5ffdff-80e9-4119-bf62-fb7c515c5aad/20260923-b06-a3379238/result.json'

class Drawing(Solo48):
    icon_id = 'browser-with-18-plus-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('browser', 'with', '18+', 'text')

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
        # Broader enclosure and enlarged counters retain all three characters.
        self.add_polyline('calendar',(4,16),(4,10),(16,10),(32,10),(44,10),(44,40),(4,40),closed=True)
        for x in (16,32):
            self.add_line('binding-'+str(x),(x,8),(x,10));self.relate('connect','calendar','binding-'+str(x))
        self.add_line('header',(4,18),(44,18));self.relate('connect','calendar','header')
        self.add_line('one',(12,27),(12,35))
        self.circle('eight-top',24,26,4);self.circle('eight-bottom',24,34,4);self.relate('connect','eight-top','eight-bottom')
        self.add_polyline('plus-h',(36,30),(39,30),(42,30));self.add_polyline('plus-v',(39,27),(39,30),(39,33));self.relate('connect','plus-h','plus-v')

