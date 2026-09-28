"""Infinity Loop.
Plan: Continuous symmetric figure-eight, smooth center crossing and broad lobes. Extremes (4,8)-(44,40).
Construction reference: local Lucide infinity, original and atomic-debug.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '44b0abb4-e46a-5a2e-a6a8-e05bdc85c901'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__infinity-loop/20260927T145836Z-thuan-mac-1/reference/loop_44b0abb4-e46a-5a2e-a6a8-e05bdc85c901.svg'
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
    icon_id = 'infinity-loop'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('infinity', 'loop', 'endless', 'symbol', 'continuous', 'eight')
    def build(self):
        # Give both lobes more vertical room so the crossing opens at 48px.
        path(self,"loop",(4,24),[("C",(4,15),(8,8),(14,8)),("C",(19,8),(20,19),(24,24)),("C",(28,29),(29,40),(34,40)),("C",(40,40),(44,33),(44,24)),("C",(44,15),(40,8),(34,8)),("C",(29,8),(28,19),(24,24)),("C",(20,29),(19,40),(14,40)),("C",(8,40),(4,33),(4,24))],True)
