"""A rounded text-entry field with a tall hooked cursor.
Symbol plan and construction: text-cursor-input: round field corners and a continuous cursor hook.
Keyshape: HRECT_L gives the field its horizontal span and the cursor vertical room.
Omissions: None.
Review: Hook radius enlarged to eight; deliberate right-side cursor placement follows the source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='54b02242-5568-41c3-a69f-a06ca068bbf9'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/type cursor_54b02242-5568-41c3-a69f-a06ca068bbf9.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='type-cursor'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('type', 'cursor')






    def build(self):
        # Split both horizontal field walls where the cursor passes through them.
        self.add_polyline('field-top',(8,16),(34,16),(40,16))
        self.add_arc('field-tr',(40,16),(44,20),radius_x=4)
        self.add_line('field-right',(44,20),(44,28))
        self.add_arc('field-br',(44,28),(40,32),radius_x=4)
        self.add_polyline('field-bottom',(40,32),(34,32),(8,32))
        self.add_arc('field-bl',(8,32),(4,28),radius_x=4)
        self.add_line('field-left',(4,28),(4,20))
        self.add_arc('field-tl',(4,20),(8,16),radius_x=4)
        self.add_contour('field','field-top-1','field-top-2','field-tr','field-right','field-br','field-bottom-1','field-bottom-2','field-bl','field-left','field-tl',closed=True)
        self.add_polyline('cursor',(34,8),(34,16),(34,32))
        self.add_arc('hook',(34,32),(26,40),radius_x=8)
        self.relate('connect','cursor','field-top-1','field-top-2','field-bottom-1','field-bottom-2','hook')
        self.contours = [c for c in self.contours if c.contour_id not in ['field-top', 'field-bottom']]
