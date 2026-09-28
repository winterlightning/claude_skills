"""Fountain Pen Writing a Flourish.
Plan: SQUARE, centerline bounds (6,6)-(42,42), complete standalone subject.
Construction: Lucide pen-tool informs diagonal nib and barrel; original owns the continuous ink flourish. Tiny branching tip mark omitted; a short slit and wider barrel preserve open negative space.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0905b5d5-4129-49a6-8741-6664be7184aa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/ink pen write_0905b5d5-4129-49a6-8741-6664be7184aa.svg'
AUTHOR = "gpt-6"
class Batch05Icon13(Solo48):
    icon_id = 'fountain-pen-writing-a-flourish'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "content"
    categories = ("primitives", "content")
    aliases = ('fountain-pen-writing-a-flourish',)
    keywords = ('fountain', 'pen', 'writing', 'a', 'flourish')
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
        self.add_polyline("barrel",(22,14),(30,6),(38,14),(30,22))
        path("nib",(22,14),[("C",(14,18),(18,12),(15,14)),("L",(14,26)),("L",(24,26)),("C",(30,22),(28,26),(30,24)),("L",(22,14))],True)
        self.relate("connect","barrel","nib")
        self.add_line("slit",(14,26),(20,22));self.relate("connect","slit","nib")
        path("flourish",(14,26),[("L",(10,26)),("A",(6,30),4,4,False),("A",(10,34),4,4,False),("L",(38,34)),("A",(38,42),4,4,True),("L",(6,42))]);self.relate("connect","flourish","nib");self.relate("connect","flourish","slit")
