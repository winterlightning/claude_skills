"""Five-Lobed Cannabis Leaf with Straight Stem.

Plan: SQUARE centerlines (6,6)-(42,42); one mirrored pointed leaf contour with a tall central lobe, paired spreading lobes and a shared stem junction. Exact named lobe count is retained.
Construction references: Lucide cannabis: a single coherent contour of curved pointed lobes around a shared stem.
Reduction: Unified matching sources; omitted fine veins and serrations absent from the brief. Curved-stem variant deliberately bends left.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '7e7d7c92-f9e5-4489-ac39-03198408b0de'
SOURCE_PATH = 'pictographic-primitives/cannabis/cannabis 1_7e7d7c92-f9e5-4489-ac39-03198408b0de.svg'
SOURCE_ICON_IDS = ('7e7d7c92-f9e5-4489-ac39-03198408b0de', '75ca4f8a-309a-4fe3-b039-3e34bdf81ef3', '8be10246-6ae7-43c7-bc9e-c25a3d070fe3')
SOURCE_PATHS = ('pictographic-primitives/cannabis/cannabis 1_7e7d7c92-f9e5-4489-ac39-03198408b0de.svg', 'pictographic-primitives/cannabis/cannabis_75ca4f8a-309a-4fe3-b039-3e34bdf81ef3.svg', 'pictographic-primitives/cannabis/cannabis_8be10246-6ae7-43c7-bc9e-c25a3d070fe3.svg')
AUTHOR = 'gpt-6'


class FiveLobedCannabisLeafWithStraightStem(Solo48):
    icon_id = 'five-lobed-cannabis-leaf-with-straight-stem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'cannabis'
    aliases = ()
    keywords = ('five-lobed', 'cannabis', 'leaf', 'with', 'straight', 'stem', 'sub icon')

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
        commands=[("C",(28,22),(28,12),(29,17)),("C",(40,14),(32,17),(36,14)),("C",(32,28),(39,20),(36,25)),("C",(42,32),(36,28),(40,30)),("C",(34,36),(40,34),(37,36))]
        commands.append(("L",(24,36)))

        # Reflect and reverse the exact curve sequence about the shared axis.
        segments=[];here=(axis,6)
        for c in commands:segments.append((here,c));here=c[1]
        mirror=lambda p:(48-p[0],p[1])
        for start,c in reversed(segments):
            if c[0]=="C":commands.append(("C",mirror(start),mirror(c[3]),mirror(c[2])))
            else:commands.append(("L",mirror(start)))
        path("leaf",(axis,6),commands,True)
        self.add_line("stem",(24,36),(24,42))
        self.relate("connect","leaf","stem")


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('75ca4f8a-309a-4fe3-b039-3e34bdf81ef3', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/cannabis/cannabis_75ca4f8a-309a-4fe3-b039-3e34bdf81ef3.svg')]
