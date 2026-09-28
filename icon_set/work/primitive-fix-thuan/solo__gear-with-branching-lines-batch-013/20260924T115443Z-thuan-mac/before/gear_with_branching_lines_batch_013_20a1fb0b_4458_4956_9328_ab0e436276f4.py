"""Settings gear connected to three branching options. Six lobes around a common center, three arms on shared spine; omit tiny unidentifiable dots.
Lucide settings: gear silhouette; supplied branching spine and three arms.
Keyshape HRECT_L on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20a1fb0b-4458-4956-9328-ab0e436276f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/set factor standard_20a1fb0b-4458-4956-9328-ab0e436276f4.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/set factor standard_20a1fb0b-4458-4956-9328-ab0e436276f4.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/set factor standard_20a1fb0b-4458-4956-9328-ab0e436276f4.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'gear-with-branching-lines-batch-013'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface/controls'
    aliases = ()
    keywords = ('gear', 'with', 'branching', 'lines')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_polyline('gear',(14,12),(20,12),(22,18),(28,20),(28,24),(28,28),(22,30),(20,36),(14,36),(12,30),(6,28),(4,24),(6,20),(12,18),closed=True)
        self.add_polyline('spine',(44,8),(36,8),(36,24),(36,40),(44,40))
        self.add_polyline('middle-arm',(28,24),(36,24),(44,24))
        self.relate('connect','gear','middle-arm')
        self.relate('connect','spine','middle-arm')
