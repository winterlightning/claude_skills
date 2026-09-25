"""A broken tree stump has flared roots and two branch stubs. HRECT extremes (4,8)-(44,40); paired roots frame the face.
Reduction: Reduced the broken edge to one notch and removed crowded bark lines.
Lucide: tree-deciduous
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c4e7360-a9cf-41ec-a007-b010f67f1f4b'
SOURCE_PATH = 'pictographic-primitives/nature/trees hive_0c4e7360-a9cf-41ec-a007-b010f67f1f4b.svg'
AUTHOR = 'gpt-6'

class TreeStump(Solo48):
    icon_id = 'tree-stump'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('stump', 'tree', 'wood', 'trunk', 'forestry', 'deforestation', 'nature', 'log')

    def build(self) -> None:
        points=[(12,26),(12,8),(20,16),(28,8),(36,8),(36,26)]
        for j in range(5):self.add_line(f'top-{j+1}',points[j],points[j+1])
        self.add_arc('root-right',(36,26),(44,40),radius_x=16,radius_y=16,sweep=False)
        self.add_line('base',(44,40),(4,40))
        self.add_arc('root-left',(4,40),(12,26),radius_x=16,radius_y=16,sweep=False)
        self.add_contour('stump','top-1','top-2','top-3','top-4','top-5','root-right','base','root-left',closed=True)
        self.add_line('stub-left',(4,20),(12,26));self.add_line('stub-right',(36,26),(44,20))
        for p in ('top-1','root-left'):self.relate('connect','stub-left',p)
        for p in ('top-5','root-right'):self.relate('connect','stub-right',p)
