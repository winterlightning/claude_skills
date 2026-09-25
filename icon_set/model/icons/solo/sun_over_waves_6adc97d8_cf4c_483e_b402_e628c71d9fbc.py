"""A half sun with three rays sits on the horizon above waves. HRECT extremes (4,8)-(44,40); sun and rays mirror about x=24.
Reduction: Reduced five rays to three and made the upper water line a flat horizon.
Lucide construction: sun, sunrise, waves-horizontal
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6adc97d8-cf4c-483e-b402-e628c71d9fbc'
SOURCE_PATH = 'pictographic-primitives/nature/outdoors water sun_6adc97d8-cf4c-483e-b402-e628c71d9fbc.svg'
AUTHOR = 'gpt-6'


class SunOverWaves(Solo48):
    icon_id = 'sun-over-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('sun', 'sea', 'waves', 'sunset', 'sunrise', 'ocean', 'beach', 'summer')

    def build(self) -> None:
        self.add_arc("sun",(14,28),(34,28),radius_x=10)
        self.add_polyline("horizon",(4,28),(14,28),(34,28),(44,28))
        for i in range(1,4):self.relate("connect","sun",f"horizon-{i}")
        self.add_line("ray-top",(24,8),(24,10))
        self.add_line("ray-left",(8,10),(12,14))
        self.add_line("ray-right",(40,10),(36,14))
        names=[]
        for i in range(4):
            n=f"wave-{i}"
            self.add_arc(n,(4+10*i,38),(14+10*i,38),radius_x=5,radius_y=2,sweep=i%2==0)
            names.append(n)
        self.add_contour("water",*names)

# Additional original reference represented by this completed drawing.
SOURCE_REFERENCES = globals().get("SOURCE_REFERENCES", []) + [('4023feef-7c65-4098-bea2-7cac808cd9ca', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/sun haze_4023feef-7c65-4098-bea2-7cac808cd9ca.svg')]
