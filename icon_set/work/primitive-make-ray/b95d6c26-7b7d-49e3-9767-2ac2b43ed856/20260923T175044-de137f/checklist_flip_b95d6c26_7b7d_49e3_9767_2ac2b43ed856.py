"""A top-bound checklist with two checked rows and a folded corner.
Construction: Reduced four binding strokes to three and omitted the second text stroke to leave room beside the folded corner; both checks retained.
Lucide construction reference: clipboard-list; coherent arcs and independent enclosed content.
Keyshape VRECT_L: (6,2)-(42,46) ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b95d6c26-7b7d-49e3-9767-2ac2b43ed856'
SOURCE_PATH = 'icon_set/work/todo-references/checklist flip_b95d6c26-7b7d-49e3-9767-2ac2b43ed856.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'checklist-flip'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('checklist', 'flip')

    def build(self):
        # Bound page and folded lower-right corner; repeated binding and checklist rows.
        self.add_polyline('page', (8,12),(40,12),(40,36),(32,44),(8,44), closed=True)
        self.add_polyline('fold', (32,44),(32,36),(40,36))
        self.relate('connect','page','fold')
        for i,x in enumerate((16,24,32)):
            self.add_line(f'binding-{i}', (x,4), (x,12))
            self.relate('connect', 'page', f'binding-{i}')
        for i,y in enumerate((22,34)):
            self.add_polyline(f'check-{i}', (16,y),(18,y+2),(22,y-2))
            if i == 0: self.add_line(f'entry-{i}', (30,y),(32,y))

