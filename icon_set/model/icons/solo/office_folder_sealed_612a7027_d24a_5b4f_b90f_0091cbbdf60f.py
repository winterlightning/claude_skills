'Sealed folder: clean folder tab and an 8-unit band without wavy fitted edges.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '612a7027-d24a-5b4f-b90f-0091cbbdf60f'
SOURCE_PATH = 'pictographic-primitives/office/office folder sealed_612a7027-d24a-5b4f-b90f-0091cbbdf60f.svg'
AUTHOR = 'gpt-6'

class OfficeFolderSealed(Solo48):
    icon_id = 'office-folder-sealed'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    categories = ('office', 'primitives')
    aliases = ()
    keywords = ('office', 'folder', 'sealed')

    def build(self):
        # Sealed folder: clean folder tab and an 8-unit band without wavy fitted edges.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('folder',(4,40),(4,8),(16,8),(24,16),(44,16),(44,40),(4,40))
        l('seam',(4,24),(44,24))
        link('connect','seam','folder')
