"""Medium Temperature Thermometer.
Plan: (8,4)-(40,44). Broad tube and bulb permit one interior mercury stem; identical shape with different liquid level. Three right ticks.
References: supplied original source; Lucide thermometer: connected rounded tube and bulb.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8ab1cb04-f795-4ebc-818d-6255c2998131'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__medium-temperature-thermometer-8ab1cb04/20260927T165437Z-thuan-mac-1/reference/temperature thermometer medium_8ab1cb04-f795-4ebc-818d-6255c2998131.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'medium-temperature-thermometer-8ab1cb04'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('medium-temperature-thermometer',)
    keywords = ('medium', 'temperature', 'thermometer')

    def build(self):

        def stroke(name, start, segments, closed=False):
            members=[]
            for j,s in enumerate(segments):
                member=f"{name}-{j}"
                if len(s)==1: self.add_line(member,start,s[0])
                else: self.add_arc(member,start,s[0],radius_x=s[1],radius_y=s[2],sweep=s[3],large_arc=s[4] if len(s)>4 else False)
                members.append(member);start=s[0]
            self.add_contour(name,*members,closed=closed)
        def circle(name,cx,cy,r):
            stroke(name,(cx-r,cy),[((cx+r,cy),r,r,True),((cx-r,cy),r,r,True)],True)
        stroke("outline",(10,28),[((10,13),),((28,13),9,9,True),((28,28),),((30,33),2,5,True),((19,44),11,11,True),((8,33),11,11,True),((10,28),2,5,True)],True)
        self.add_line("level",(19,18),(19,34))
        # Give the three temperature marks readable lengths instead of dots.
        for y in (8,16,24):self.add_line(f"tick-{y}",(37,y),(40,y))
