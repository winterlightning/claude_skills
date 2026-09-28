"""Perfume Bottle with Squeeze Bulb.

Plan: HRECT centerlines (4,8)-(44,40); smoothly shouldered tapered bottle, upright atomizer and a wide oval squeeze bulb joined by a tube. Intentional asymmetry follows the reference.
Construction references: Lucide spray-can: neck/body articulation and coherent bottle shoulders; supplied perfume source controls the squeeze bulb.
Reduction: Omitted minor collar and nozzle subdivisions; preserved the atomizer and bulb.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '78c4cb80-3933-5625-8111-a203c9a17c32'
SOURCE_PATH = 'pictographic-primitives/beauty/body care perfume_78c4cb80-3933-5625-8111-a203c9a17c32.svg'
SOURCE_ICON_IDS = ('78c4cb80-3933-5625-8111-a203c9a17c32',)
SOURCE_PATHS = ('pictographic-primitives/beauty/body care perfume_78c4cb80-3933-5625-8111-a203c9a17c32.svg',)
AUTHOR = 'gpt-6'


class PerfumeBottleWithSqueezeBulb(Solo48):
    icon_id = 'perfume-bottle-with-squeeze-bulb'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('perfume', 'bottle', 'with', 'squeeze', 'bulb')

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

        path("bottle",(28,22),[("L",(36,22)),("C",(44,30),(40,22),(44,26)),("C",(40,40),(44,34),(40,38)),("L",(24,40)),("C",(20,30),(24,38),(20,34)),("C",(28,22),(20,26),(24,22))],True)
        self.add_polyline("atomizer",(28,22),(28,13),(28,8),(36,8),(36,22))
        self.relate("connect","bottle","atomizer")
        path("bulb",(20,13),[("A",(4,13),8,5,True),("A",(20,13),8,5,True)],True)
        self.add_line("tube",(20,13),(28,13))
        self.relate("connect","tube","bulb")
        self.relate("connect","tube","atomizer")
