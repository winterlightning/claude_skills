'Calendar with math equation.\nPlan: HRECT_L allocates width to 2+1 in the original order. Shared plus intersection and repeated bindings.\nReference: calendar; Even binding rhythm and enclosing calendar.\nChanges: Numeral 1 loses its short lead-in; corners are square; plus is very compact.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '14b5dacf-2ae7-4b43-b032-7129b3d49037'
SOURCE_PATH = 'pictographic-primitives/other/calendar math_14b5dacf-2ae7-4b43-b032-7129b3d49037.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'calendar-math'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
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
        top = [("L",(x,12)) for x in rings] + [("L",(40,12)),
            ("A",(44,14),4,4,True),("L",(44,18))]
        self.path("calendar-top",(4,18),[("L",(4,14)),
            ("A",(8,12),4,4,True)]+top)
        self.path("calendar-body",(44,18),[("L",(44,36)),
            ("A",(40,40),4,4,True),("L",(8,40)),
            ("A",(4,36),4,4,True),("L",(4,18))])
        self.relate("connect","calendar-top","calendar-body")
        for x in rings:
            name=f"binding-{x}"
            self.add_line(name,(x,8),(x,12))
            self.relate("connect",name,"calendar-top")
        if header:
            self.add_line("header",(4,18),(44,18))
            for name in ("calendar-top","calendar-body"):
                self.relate("connect",name,"header")

    def build(self):
        # Wide frame owns the 2+1 row. Narrow one is a straight numeral.
        self.add_polyline('calendar-body',(4,12),(14,12),(24,12),(34,12),(44,12),(44,40),(4,40),closed=True)
        for x in (14,24,34):
            self.add_line(f'binding-{x}',(x,8),(x,12))
            self.relate('connect',f'binding-{x}','calendar-body')
        self.path('two',(13,23),[('A',(18,23),3,3,True),('L',(13,31)),('L',(18,31))])
        self.add_polyline('plus-horizontal',(26,27),(27,27),(28,27))
        self.add_polyline('plus-vertical',(27,25),(27,27),(27,29))
        self.relate('connect','plus-horizontal','plus-vertical')
        self.add_line('one',(36,21),(36,31))

PARENT_MODULE = 'icon_set/model/icons/solo/calendar_math_14b5dacf_2ae7_4b43_b032_7129b3d49037.py'

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'b020531a2d105b6b9535d9c7bc7077a4b2108f30e4a4588e053ea26c40db5213', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '14b5dacf-2ae7-4b43-b032-7129b3d49037'}
