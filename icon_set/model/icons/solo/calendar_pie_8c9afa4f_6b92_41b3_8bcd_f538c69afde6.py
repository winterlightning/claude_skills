'Calendar with pie chart.\nPlan: SQUARE balances three bindings and the centered pie. Shared radial junction with unequal sectors.\nReference: calendar; Three repeated bindings and rounded frame.\nChanges: No parts omitted; pie rim adjusted to clear the frame and diagonal spoke.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8c9afa4f-6b92-41b3-8bcd-f538c69afde6'
SOURCE_PATH = 'pictographic-primitives/other/calendar pie_8c9afa4f-6b92-41b3-8bcd-f538c69afde6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'calendar-pie'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('calendar', 'pie')

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
        # Shallower top rim increases the circular chart's available height.
        self.path('frame',(10,8),[('L',(14,8)),('L',(24,8)),('L',(34,8)),('L',(38,8)),('A',(42,12),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,12)),('A',(10,8),4,4,True)],True)
        for x in (14,24,34):
            self.add_line(f'binding-{x}',(x,6),(x,8))
            self.relate('connect',f'binding-{x}','frame')
        self.add_bezier('pie-tr',(24,17),((29,17),(33,21),(33,25)))
        self.add_bezier('pie-br',(33,25),((33,30),(29,33),(24,33)))
        self.add_bezier('pie-bl-a',(24,33),((22,33),(19,32),(18,31)))
        self.add_bezier('pie-bl-b',(18,31),((16,29),(15,27),(15,25)))
        self.add_bezier('pie-tl',(15,25),((15,21),(19,17),(24,17)))
        self.add_contour('pie','pie-tr','pie-br','pie-bl-a','pie-bl-b','pie-tl',closed=True)
        for n,end in [('up',(24,17)),('right',(33,25)),('diagonal',(18,31))]:
            self.add_line('spoke-'+n,(24,25),end)
            self.relate('connect','spoke-'+n,'pie')
        self.relate('connect','spoke-up','spoke-right','spoke-diagonal')

PARENT_MODULE = 'icon_set/model/icons/solo/calendar_pie_8c9afa4f_6b92_41b3_8bcd_f538c69afde6.py'
