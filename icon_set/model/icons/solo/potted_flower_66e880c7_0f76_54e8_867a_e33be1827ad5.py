"""A five-lobed flower with an upright stem. VRECT extremes (8,4)-(40,44).
Reduction: Removed the centre ring so five broad petal lobes remain clear. Removed the separate rim band.
Lucide construction: flower-2, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66e880c7-0f76-54e8-867a-e33be1827ad5'
SOURCE_PATH = 'pictographic-primitives/nature/flower pot_66e880c7-0f76-54e8-867a-e33be1827ad5.svg'
AUTHOR = 'gpt-6'


class PottedFlower(Solo48):
    icon_id = 'potted-flower'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('flower', 'pot', 'potted', 'plant', 'bloom', 'houseplant', 'garden', 'decor')

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
        self.add_line("stem",(24,20),(24,34))
        self.relate("connect","stem","bloom-2")
        self.relate("connect","stem","bloom-3")
        self.add_polyline("pot",(8,34),(24,34),(40,34),(36,44),(12,44),closed=True)
        self.relate("connect","stem","pot-1")
        self.relate("connect","stem","pot-2")
