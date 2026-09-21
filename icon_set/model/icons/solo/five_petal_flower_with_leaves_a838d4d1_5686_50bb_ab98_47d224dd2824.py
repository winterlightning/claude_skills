"""A five-lobed flower with an upright stem. VRECT extremes (8,4)-(40,44).
Reduction: Removed the centre ring so five broad petal lobes remain clear. Opened the leaf interiors.
Lucide construction: flower-2, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a838d4d1-5686-50bb-ab98-47d224dd2824'
SOURCE_PATH = 'pictographic-primitives/nature/flower_a838d4d1-5686-50bb-ab98-47d224dd2824.svg'
AUTHOR = 'gpt-6'


class FivePetalFlowerWithLeaves(Solo48):
    icon_id = 'five-petal-flower-with-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-01"
    aliases = ()
    keywords = ('flower', 'daisy', 'petals', 'bloom', 'stem', 'leaves', 'garden', 'nature')

    def build(self) -> None:
        # Five rounded lobes share the top petal axis and mirrored side nodes.
        nodes=[(20,8),(28,8),(30,16),(24,20),(18,16)]
        radii=[4,5,4,4,5]
        members=[]
        for i,a in enumerate(nodes):
            name=f"bloom-{i}"
            self.add_arc(name,a,nodes[(i+1)%5],radius_x=radii[i],large_arc=i in (1,2,3,4))
            members.append(name)
        self.add_contour("flower",*members,closed=True)
        self.add_line("stem",(24,20),(24,44))
        self.relate("connect","stem","bloom-2")
        self.relate("connect","stem","bloom-3")
        # Paired open leaf strokes retain broad negative space at the stem.
        self.add_arc("leaf-left", (8,34), (24,44), radius_x=16, radius_y=10)
        self.add_arc("leaf-right", (24,44), (40,34), radius_x=16, radius_y=10)
        self.relate("connect", "stem", "leaf-left")
        self.relate("connect", "stem", "leaf-right")

SOURCE_REFERENCES = (('2b341bc8-cb9a-4490-9129-7339b9080d7e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/lilac_2b341bc8-cb9a-4490-9129-7339b9080d7e.svg'),)
