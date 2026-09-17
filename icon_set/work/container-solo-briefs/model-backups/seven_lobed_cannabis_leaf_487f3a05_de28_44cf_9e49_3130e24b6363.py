"""Seven-Lobed Cannabis Leaf.

Plan: SQUARE centerlines (6,6)-(42,42); one mirrored pointed leaf contour with a tall central lobe, paired spreading lobes and a shared stem junction. Exact named lobe count is retained.
Construction references: Lucide cannabis: a single coherent contour of curved pointed lobes around a shared stem.
Reduction: Unified matching sources; omitted fine veins and serrations absent from the brief. Curved-stem variant deliberately bends left.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '487f3a05-de28-44cf-9e49-3130e24b6363'
SOURCE_PATH = 'pictographic-primitives/cannabis/cannabis_487f3a05-de28-44cf-9e49-3130e24b6363.svg'
SOURCE_ICON_IDS = ('487f3a05-de28-44cf-9e49-3130e24b6363',)
SOURCE_PATHS = ('pictographic-primitives/cannabis/cannabis_487f3a05-de28-44cf-9e49-3130e24b6363.svg',)
AUTHOR = 'gpt-6'


class SevenLobedCannabisLeaf(Solo48):
    icon_id = 'seven-lobed-cannabis-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'cannabis'
    aliases = ()
    keywords = ('seven-lobed', 'cannabis', 'leaf')

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

        axis=24
        commands=[("C",(28,20),(28,12),(29,16)),("C",(40,12),(32,16),(36,12)),("C",(32,24),(39,19),(36,22)),("C",(42,28),(36,23),(40,26)),("C",(32,32),(40,33),(36,33)),("C",(34,41),(34,35),(34,39)),("C",(24,37),(30,41),(27,39))]

        # Reflect and reverse the exact curve sequence about the shared axis.
        segments=[];here=(axis,6)
        for c in commands:segments.append((here,c));here=c[1]
        mirror=lambda p:(48-p[0],p[1])
        for start,c in reversed(segments):
            if c[0]=="C":commands.append(("C",mirror(start),mirror(c[3]),mirror(c[2])))
            else:commands.append(("L",mirror(start)))
        path("leaf",(axis,6),commands,True)
        self.add_line("stem",(24,37),(24,42))
        self.relate("connect","leaf","stem")
