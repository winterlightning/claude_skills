from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04ec5404-f235-5ca7-ac4c-23f5bc014d24'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/playground globe_04ec5404-f235-5ca7-ac4c-23f5bc014d24.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/playground globe_04ec5404-f235-5ca7-ac4c-23f5bc014d24.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/04-world-globe-on-stand--04ec5404-f235-5ca7-ac4c-23f5bc014d24.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['One equator and one meridian preserve the framework while removing crowded latitude bands.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'globe-framework-on-legs-batch-018-04'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "kids"
    keywords = ('globe', 'framework', 'sphere', 'meridians', 'latitude', 'legs', 'playground', 'world')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('globe-0', (8, 20), (24, 4), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('globe-1', (24, 4), (40, 20), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('globe-2', (40, 20), (24, 36), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('globe-3', (24, 36), (8, 20), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_contour('globe', 'globe-0', 'globe-1', 'globe-2', 'globe-3', closed=True)
        self.add_polyline('equator', (8, 20), (24, 20), (40, 20), closed=False)
        self.add_polyline('meridian', (24, 4), (24, 20), (24, 36), closed=False)
        self.add_polyline('legs', (14, 44), (18, 36), (30, 36), (34, 44), closed=False)
        self.relate("connect", 'globe', 'equator')
        self.relate("connect", 'globe', 'meridian')
        self.relate("connect", 'equator', 'meridian')
