"""Low Temperature Thermometer.
Plan: (8,4)-(40,44). Broad tube and bulb permit one interior mercury stem; identical shape with different liquid level. Three right ticks.
References: supplied original source; Lucide thermometer: connected rounded tube and bulb.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a11530f-6d64-4f60-a914-f2d1cfcc821f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/temperature thermometer low_2a11530f-6d64-4f60-a914-f2d1cfcc821f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'low-temperature-thermometer-2a11530f'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('low-temperature-thermometer',)
    keywords = ('low', 'temperature', 'thermometer')

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
        self.add_line("level",(19,30),(19,34))
        for y in (8,18,28):self.add_line(f"tick-{y}",(38,y),(40,y))

