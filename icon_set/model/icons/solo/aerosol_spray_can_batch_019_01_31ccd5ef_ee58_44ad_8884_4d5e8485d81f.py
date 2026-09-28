from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31ccd5ef-ee58-44ad-8884-4d5e8485d81f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/spray can_31ccd5ef-ee58-44ad-8884-4d5e8485d81f.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/spray can_31ccd5ef-ee58-44ad-8884-4d5e8485d81f.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/01-aerosol-spray-can--31ccd5ef-ee58-44ad-8884-4d5e8485d81f.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'spray-can: clear nozzle/body hierarchy.'

class BatchIcon(Solo48):
    icon_id = 'aerosol-spray-can-batch-019-01'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives-generate", "state", "other")
    keywords = ('spray', 'aerosol', 'can', 'nozzle', 'bottle', 'mist', 'container', 'cleaning')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_line('can-0', (12, 16), (26, 16))
        self.add_arc('can-1', (26, 16), (30, 20), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('can-2', (30, 20), (30, 40))
        self.add_arc('can-3', (30, 40), (26, 44), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('can-4', (26, 44), (12, 44))
        self.add_arc('can-5', (12, 44), (8, 40), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('can-6', (8, 40), (8, 20))
        self.add_arc('can-7', (8, 20), (12, 16), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('can', 'can-0', 'can-1', 'can-2', 'can-3', 'can-4', 'can-5', 'can-6', 'can-7', closed=True)
        self.add_polyline('nozzle', (14, 16), (14, 4), (24, 4), (24, 16), closed=False)
        self.add_line('spray-up', (34, 8), (40, 4))
        self.add_line('spray-down', (38, 16), (40, 20))
