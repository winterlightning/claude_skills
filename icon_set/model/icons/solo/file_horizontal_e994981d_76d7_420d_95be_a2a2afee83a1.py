"""A horizontal sheet with rounded left corners and clipped upper-right corner. Centerline extremes (4,8)-(44,40).
Construction references: Lucide file: coherent folded-page silhouette, recomposed for the source horizontal proportion."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e994981d-76d7-420d-95be-a2a2afee83a1'
SOURCE_PATH = 'icon_set/work/todo-references/file horizontal_e994981d-76d7-420d-95be-a2a2afee83a1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'file-horizontal'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface/files'
    aliases = ()
    keywords = ('file', 'document', 'horizontal', 'page')

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
        self.add_line("top",(8,8),(38,8))
        self.add_line("fold",(38,8),(44,14))
        self.add_line("right",(44,14),(44,36))
        self.add_arc("br",(44,36),(40,40),radius_x=4)
        self.add_line("bottom",(40,40),(8,40))
        self.add_arc("bl",(8,40),(4,36),radius_x=4)
        self.add_line("left",(4,36),(4,12))
        self.add_arc("tl",(4,12),(8,8),radius_x=4)
        self.add_contour("sheet","top","fold","right","br","bottom","bl","left","tl",closed=True)
