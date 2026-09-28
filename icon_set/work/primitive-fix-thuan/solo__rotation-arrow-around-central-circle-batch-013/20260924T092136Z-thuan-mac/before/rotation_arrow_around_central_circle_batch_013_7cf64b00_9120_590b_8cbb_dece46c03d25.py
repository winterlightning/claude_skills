"""Counterclockwise sweeping refresh arrow around a circular pivot. Concentric radii20 and5 leave generous clearance; arrowhead tangent to left terminal.
Lucide refresh-cw: circular sweep and open arrowhead.
Keyshape CIRCLE on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7cf64b00-9120-590b-8cbb-dece46c03d25'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/synchronize arrow 2_7cf64b00-9120-590b-8cbb-dece46c03d25.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/synchronize arrow 2_7cf64b00-9120-590b-8cbb-dece46c03d25.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/synchronize arrow 2_7cf64b00-9120-590b-8cbb-dece46c03d25.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'rotation-arrow-around-central-circle-batch-013'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface/controls'
    aliases = ()
    keywords = ('rotation', 'arrow', 'around', 'central', 'circle')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_arc('sweep',(24,44),(4,24),radius_x=20,large_arc=True,sweep=False)
        self.add_polyline('arrowhead',(4,24),(10,18))
        self.add_line('arrow-wing',(4,24),(10,30))
        self.relate('connect','arrowhead','arrow-wing')
        self.relate('connect','sweep','arrow-wing')
        self.relate('connect','sweep','arrowhead')
        circle('pivot',24,24,5)
