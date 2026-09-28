"""Human Skull.
Plan: Mirrored rounded cranium and narrower jaw; paired eye circles, open nose and teeth. Circular envelope: radius 22 about (24,24).
Construction reference: local Lucide skull, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a67d3cf1-4982-5700-98f0-85805691176b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/skull_a67d3cf1-4982-5700-98f0-85805691176b.svg'
AUTHOR = 'gpt-6'

def circle(icon,name,cx,cy,r):
    icon.add_arc(name+"-top",(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+"-bottom",(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+"-top",name+"-bottom",closed=True)

def path(icon,name,start,commands,closed=False):
    point=start;members=[]
    for i,command in enumerate(commands):
        member=f"{name}-{i}"; kind=command[0]; end=command[-1]
        if kind=="L":icon.add_line(member,point,end)
        elif kind=="A":icon.add_arc(member,point,end,radius_x=command[1],radius_y=command[2],sweep=command[3])
        else:icon.add_bezier(member,point,(command[1],command[2],end))
        members.append(member);point=end
    icon.add_contour(name,*members,closed=closed)

class Drawing(Solo48):
    icon_id = 'human-skull'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('skull', 'bones', 'head', 'eyes', 'anatomy', 'skeleton')
    def build(self):
        # Circular keyshape gives both 6-unit eye loops genuine spacing margin.
        # The cranium is a radius-20 semicircle, centered at (24,24).
        path(self,"outline",(4,24),[("A",20,20,True,(44,24)),("C",(44,29),(38,31),(34,34)),("L",(34,38)),("A",4,4,True,(30,42)),("L",(28,42)),("L",(20,42)),("L",(18,42)),("A",4,4,True,(14,38)),("L",(14,34)),("C",(10,31),(4,29),(4,24))],True)
        for x in (17,31):circle(self,"eye-"+str(x),x,21,3)
        self.add_polyline("nose",(22,32),(24,30),(26,32))
        for x in (20,28):
            self.add_line("tooth-"+str(x),(x,40),(x,42))
            self.relate("connect","tooth-"+str(x),"outline")
