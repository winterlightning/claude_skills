"""An oval message bubble with a lower-left tail and PM lettering.
Plan: One coherent oval-and-tail contour surrounds a round-bow P and angular M. Tail asymmetry follows the reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '39d51711-cb0a-4cf4-bdca-37c1fe832458'
SOURCE_PATH = 'icon_set/work/todo-references/bubble message pm text_39d51711-cb0a-4cf4-bdca-37c1fe832458.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCES = ['message-square']
PLAN = 'Retain oval speech bubble and PM; use a broader P bowl and narrower shared-axis M.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/39d51711-cb0a-4cf4-bdca-37c1fe832458/20260923-b06-3f8fd87f/result.json'

class Drawing(Solo48):
    icon_id = 'bubble-message-pm-text'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('bubble', 'message', 'pm', 'text')

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

        self.path("bubble",(6,22),[("A",(24,6),18,16,True),
            ("A",(42,22),18,16,True),("A",(24,38),18,16,True),
            ("L",(18,37)),("L",(8,42)),("L",(11,32)),
            ("A",(6,22),18,16,True)],True)
        self.add_polyline("p-stem",(14,28),(14,24),(14,16))
        self.path("p-bow",(14,16),[("L",(17,16)),
            ("A",(17,24),4,4,True),("L",(14,24))])
        self.relate("connect","p-stem","p-bow")
        self.add_polyline("m",(29,28),(29,17),(32,24),(35,17),(35,28))
