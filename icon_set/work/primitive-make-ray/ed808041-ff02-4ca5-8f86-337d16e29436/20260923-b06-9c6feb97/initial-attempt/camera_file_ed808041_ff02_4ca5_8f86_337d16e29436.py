"""An upright document with clipped upper-right corner and a camera symbol.
Plan: VRECT_L document contour with clipped corner, enclosing one camera with raised prism and lens point. Asymmetric page corner follows source."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ed808041-ff02-4ca5-8f86-337d16e29436'
SOURCE_PATH = 'icon_set/work/todo-references/camera file_ed808041-ff02-4ca5-8f86-337d16e29436.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCES = ['file-video-camera']
class Drawing(Solo48):
    icon_id = 'camera-file'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('camera', 'file')

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

        self.path("document",(12,4),[("L",(30,4)),("L",(40,14)),
            ("L",(40,40)),("A",(36,44),4,4,True),("L",(12,44)),
            ("A",(8,40),4,4,True),("L",(8,8)),
            ("A",(12,4),4,4,True)],True)
        self.path("camera",(18,22),[("L",(20,22)),("L",(22,18)),
            ("L",(26,18)),("L",(28,22)),("L",(30,22)),
            ("A",(32,24),2,2,True),("L",(32,32)),
            ("A",(30,34),2,2,True),("L",(18,34)),
            ("A",(16,32),2,2,True),("L",(16,24)),
            ("A",(18,22),2,2,True)],True)
        self.add_dot("lens",(24,27))
