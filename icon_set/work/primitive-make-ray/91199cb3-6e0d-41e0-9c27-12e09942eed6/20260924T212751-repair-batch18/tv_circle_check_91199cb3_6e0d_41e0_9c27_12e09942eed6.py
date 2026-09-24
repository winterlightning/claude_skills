"""A monitor on a pedestal containing a circled check.
Symbol plan and construction: monitor-check: rounded screen and centered pedestal.
Keyshape: VRECT_L provides the tallest screen and stand arrangement.
Omissions: Tick shortened; ring and pedestal retained.
Review: Blocked: status-ring/check clearance is 4.17126, below 8. Native-size check remains crowded. Six candidates saved."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='91199cb3-6e0d-41e0-9c27-12e09942eed6'
SOURCE_PATH = 'pictographic-primitives/other/tv circle check_91199cb3-6e0d-41e0-9c27-12e09942eed6.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tv-circle-check'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('tv', 'circle', 'check')

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)



    def monitor(self,left=6,top=6,right=42,bottom=34,foot=42):
        # Matched quarter-round corners, bottom wall split at the stand junction.
        r=4;cx=(left+right)//2
        self.add_line('screen-top',(left+r,top),(right-r,top))
        self.add_arc('screen-tr',(right-r,top),(right,top+r),radius_x=r)
        self.add_line('screen-right',(right,top+r),(right,bottom-r))
        self.add_arc('screen-br',(right,bottom-r),(right-r,bottom),radius_x=r)
        self.add_line('screen-bottom-r',(right-r,bottom),(cx,bottom))
        self.add_line('screen-bottom-l',(cx,bottom),(left+r,bottom))
        self.add_arc('screen-bl',(left+r,bottom),(left,bottom-r),radius_x=r)
        self.add_line('screen-left',(left,bottom-r),(left,top+r))
        self.add_arc('screen-tl',(left,top+r),(left+r,top),radius_x=r)
        self.add_contour('screen','screen-top','screen-tr','screen-right','screen-br','screen-bottom-r','screen-bottom-l','screen-bl','screen-left','screen-tl',closed=True)
        self.add_line('stand',(cx,bottom),(cx,foot))
        self.add_polyline('foot',(cx-8,foot),(cx,foot),(cx+8,foot))
        self.relate('connect','stand','screen-bottom-r','screen-bottom-l')
        self.relate('connect','stand','foot')


    def build(self):
        self.monitor(left=8,top=4,right=40,bottom=36,foot=44)
        self.circle('status-ring',24,20,7)
        self.add_polyline('check',(22,20),(24,22),(26,18))
