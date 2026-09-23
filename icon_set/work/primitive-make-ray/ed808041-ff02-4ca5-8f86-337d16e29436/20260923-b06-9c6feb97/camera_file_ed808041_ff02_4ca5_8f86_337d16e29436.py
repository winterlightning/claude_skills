"""An upright document with clipped upper-right corner and a camera symbol.
Plan: SQUARE document contour with clipped corner gives the enclosed camera more width; camera retains raised prism and lens point. Asymmetric page corner follows source."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ed808041-ff02-4ca5-8f86-337d16e29436'
SOURCE_PATH = 'icon_set/work/todo-references/camera file_ed808041-ff02-4ca5-8f86-337d16e29436.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCES = ['file-video-camera']
class Drawing(Solo48):
    icon_id = 'camera-file'
    keyshape = Keyshape.SQUARE
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

        self.path("document-upper",(10,6),[("L",(34,6)),("L",(42,14)),
            ("L",(42,38)),("A",(38,42),4,4,True)])
        self.add_line("document-bottom",(38,42),(10,42))
        self.path("document-left",(10,42),[("A",(6,38),4,4,True),
            ("L",(6,10)),("A",(10,6),4,4,True)])
        self.relate("connect","document-upper","document-left")
        self.relate("connect","document-upper","document-bottom")
        self.relate("connect","document-left","document-bottom")
        self.path("camera",(17,18),[("L",(20,18)),("L",(22,15)),
            ("L",(26,15)),("L",(28,18)),("L",(31,18)),
            ("A",(33,20),2,2,True),("L",(33,32)),
            ("A",(31,34),2,2,True),("L",(17,34)),
            ("A",(15,32),2,2,True),("L",(15,20)),
            ("A",(17,18),2,2,True)],True)
        self.add_dot("lens",(24,25))
