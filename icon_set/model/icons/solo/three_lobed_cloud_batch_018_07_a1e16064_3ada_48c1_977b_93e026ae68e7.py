from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1e16064-3ada-48c1-977b-93e026ae68e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/logos/microsoft onedrive logo_a1e16064-3ada-48c1-977b-93e026ae68e7.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/microsoft onedrive logo_a1e16064-3ada-48c1-977b-93e026ae68e7.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/07-simple-cloud-storage-icon--a1e16064-3ada-48c1-977b-93e026ae68e7.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'cloud: coherent dome and side-lobe contour.'

class BatchIcon(Solo48):
    icon_id = 'three-lobed-cloud-batch-018-07'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('cloud', 'sky', 'storage', 'weather', 'onedrive', 'rounded', 'dome', 'outline')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('left', (14, 38), (14, 18), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('dome', (14, 18), (34, 18), radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('right', (34, 18), (34, 38), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('base', (34, 38), (14, 38))
        self.add_contour('cloud', 'left', 'dome', 'right', 'base', closed=True)
