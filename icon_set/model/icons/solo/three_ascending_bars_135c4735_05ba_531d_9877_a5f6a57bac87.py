"""Three Ascending Bars.

Plan: HRECT centerlines (4,8)-(44,40); three equal-width rectangular bars share a baseline and increase by 10 units in height.
Construction references: Lucide chart-no-axes-column-increasing: shared baseline, equal pitch, rising height.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '135c4735-05ba-531d-9877-a5f6a57bac87'
SOURCE_PATH = 'pictographic-primitives/business/bars_135c4735-05ba-531d-9877-a5f6a57bac87.svg'
SOURCE_ICON_IDS = ('135c4735-05ba-531d-9877-a5f6a57bac87',)
SOURCE_PATHS = ('pictographic-primitives/business/bars_135c4735-05ba-531d-9877-a5f6a57bac87.svg',)
AUTHOR = 'gpt-6'


class ThreeAscendingBars(Solo48):
    icon_id = 'three-ascending-bars'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('three', 'ascending', 'bars')

    def build(self) -> None:
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[("A",(x,y+r),r,r,True),("A",(x,y-r),r,r,True)],True)

        width,step,base=8,16,40
        for i,height in enumerate((12,22,32)):
            x=4+i*step
            self.add_polyline(f"bar-{i}",(x,base),(x,base-height),(x+width,base-height),(x+width,base),closed=True)
            if i:
                self.add_line(f"baseline-{i}",(x-step+width,base),(x,base))
                self.relate("connect",f"baseline-{i}",f"bar-{i-1}")
                self.relate("connect",f"baseline-{i}",f"bar-{i}")
