"""A browser window containing a circular user head and open shoulder bust.
Plan: Square browser encloses a detached user bust; mirrored shoulders about x=24. Head bottom y=27, shoulder top y=35 gives exactly 4 ink units."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3a3e4d85-115c-4ccb-82d1-46fd45222b3a'
SOURCE_PATH = 'icon_set/work/todo-references/browser person_3a3e4d85-115c-4ccb-82d1-46fd45222b3a.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCES = ['panels-top-left', 'human_ref/user.svg']
class Drawing(Solo48):
    icon_id = 'browser-person'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('browser', 'person')

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
        # Shared enclosure: 36-square, r=4, 8-unit header; top dots omitted.
        self.path("browser-top", (6,14), [("L",(6,10)),
            ("A",(10,6),4,4,True),("L",(38,6)),
            ("A",(42,10),4,4,True),("L",(42,14))])
        self.path("browser-body", (42,14), [("L",(42,38)),
            ("A",(38,42),4,4,True),("L",(10,42)),
            ("A",(6,38),4,4,True),("L",(6,14))])
        self.add_line("header",(6,14),(42,14))
        self.relate("connect","browser-top","browser-body")
        for name in ("browser-top","browser-body"):
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

        self.browser()
        # Shared human_ref/user.svg: circular head, smooth broad open shoulders.
        self.circle("head",24,24,3)
        self.path("shoulders",(16,38),[("A",(24,35),8,3,True),
            ("A",(32,38),8,3,True)])
