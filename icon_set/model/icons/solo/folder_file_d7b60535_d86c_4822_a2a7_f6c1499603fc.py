"""A folded document peeks from behind a front folder. The folder side outline meets the visible ends of the open rear-page outline; the front/back order is preserved.
Construction references: Lucide folder and file: enclosure and folded-page construction. The source layers folder in front of the document."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7b60535-d86c-4822-a2a7-f6c1499603fc'
SOURCE_PATH = 'icon_set/work/todo-references/folder file_d7b60535-d86c-4822-a2a7-f6c1499603fc.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'folder-file-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface/files'
    aliases = ()
    keywords = ('folder', 'file', 'document')

    def page(self):
        self.add_line("page-top",(12,4),(28,4)); self.add_line("page-fold-edge",(28,4),(40,16)); self.add_line("page-right",(40,16),(40,40))
        self.add_arc("page-br",(40,40),(36,44),radius_x=4); self.add_line("page-bottom",(36,44),(12,44)); self.add_arc("page-bl",(12,44),(8,40),radius_x=4)
        self.add_line("page-left",(8,40),(8,8)); self.add_arc("page-tl",(8,8),(12,4),radius_x=4)
        self.add_contour("page","page-top","page-fold-edge","page-right","page-br","page-bottom","page-bl","page-left","page-tl",closed=True)
        self.add_polyline("fold-crease",(28,4),(28,16),(40,16)); self.relate("connect","page","fold-crease")

    def circle(self,name,x,y,r):
        self.add_arc(name+"-upper",(x-r,y),(x+r,y),radius_x=r,sweep=False); self.add_arc(name+"-lower",(x+r,y),(x-r,y),radius_x=r,sweep=False)
        self.add_contour(name,name+"-upper",name+"-lower",closed=True)

    def build(self):
        self.add_line("file-top",(14,8),(28,8))
        self.add_line("file-fold-edge",(28,8),(38,18))
        self.add_line("file-right",(38,18),(38,32))
        self.add_contour("back-top","file-top","file-fold-edge","file-right")
        self.add_line("file-left",(14,28),(14,8))
        self.add_polyline("front-folder",(4,28),(17,28),(22,32),(44,32),(44,40),(4,40),(4,28),closed=True)
        self.relate("connect","file-left","front-folder")
        self.relate("connect","file-right","front-folder")
