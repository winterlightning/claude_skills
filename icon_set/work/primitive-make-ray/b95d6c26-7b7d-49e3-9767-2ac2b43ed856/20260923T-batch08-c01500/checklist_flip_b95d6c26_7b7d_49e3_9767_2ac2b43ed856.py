"""checklist flip. Standalone reconstruction of supplied reference.
Plan: preserve the whole composition; VRECT_L bounds (6, 2, 42, 46).
Construction reference: Lucide clipboard-list, round joins and coherent symbol contours.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b95d6c26-7b7d-49e3-9767-2ac2b43ed856'
SOURCE_PATH = 'icon_set/work/todo-references/checklist flip_b95d6c26-7b7d-49e3-9767-2ac2b43ed856.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'checklist-flip'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('checklist', 'flip')

    def build(self):

        # Upright page, folded lower-right corner, two checklist rows and top binding.
        self.add_polyline('page',(8,4),(40,4),(40,32),(28,44),(8,44),closed=True)
        self.add_polyline('fold',(28,44),(28,32),(40,32))
        self.relate('connect','page','fold')
        for row,y in enumerate((14,26)):
            self.add_polyline(f'check-{row}',(16,y),(18,y+3),(21,y-1))
            text_y = y if row == 0 else y-2
            self.add_line(f'text-{row}',(29,text_y),(32,text_y))
        for col,x in enumerate((16,24,32)):
            self.add_line(f'binding-{col}',(x,4),(x,5))
            self.relate('connect','page',f'binding-{col}')

