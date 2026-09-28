"""A symmetrical peaked shield with straight shoulders, tapering lower sides and a check. Shield reaches (8,4)-(40,44); the check remains clear of its outline.
Construction references: Lucide shield-check: coherent outline and angular check, retaining the source peaked crown."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b6ec7ff-fa5a-4489-9bab-e1e940ac236f'
SOURCE_PATH = 'icon_set/work/todo-references/file shield_4b6ec7ff-fa5a-4489-9bab-e1e940ac236f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'file-shield'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'security'
    aliases = ()
    keywords = ('file', 'shield', 'security')

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
        self.add_polyline("shield",(24,4),(30,10),(40,10),(40,20),(36,30),(24,44),(12,30),(8,20),(8,10),(18,10),(24,4),closed=True)
        self.add_polyline("check",(19,23),(23,28),(31,18))
