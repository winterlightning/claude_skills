"""A folded portrait document carries a centered medical cross and one separator rule. The plus bars share their center; the rule clears the cross and lower page edge.
Construction references: Lucide file-plus: page and fold. Lucide cross: orthogonal plus; source plus retained as dominant content."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d9d4b43-b321-4da2-aa48-7a307656b538'
SOURCE_PATH = 'icon_set/work/todo-references/file medical cross_2d9d4b43-b321-4da2-aa48-7a307656b538.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'file-medical-cross'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('combination', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('file', 'medical', 'cross', 'health')

    def page(self):
        self.add_line("page-top",(12,4),(28,4)); self.add_line("page-fold-edge",(28,4),(40,16)); self.add_line("page-right",(40,16),(40,40))
        self.add_arc("page-br",(40,40),(36,44),radius_x=4); self.add_line("page-bottom",(36,44),(12,44)); self.add_arc("page-bl",(12,44),(8,40),radius_x=4)
        self.add_line("page-left",(8,40),(8,8)); self.add_arc("page-tl",(8,8),(12,4),radius_x=4)
        self.add_contour("page","page-top","page-fold-edge","page-right","page-br","page-bottom","page-bl","page-left","page-tl",closed=True)
        # Source has a clipped page corner without an inner crease.

    def circle(self,name,x,y,r):
        self.add_arc(name+"-upper",(x-r,y),(x+r,y),radius_x=r,sweep=False); self.add_arc(name+"-lower",(x+r,y),(x-r,y),radius_x=r,sweep=False)
        self.add_contour(name,name+"-upper",name+"-lower",closed=True)

    def build(self):
        self.page()
        self.add_line("cross-horizontal",(18,21),(30,21))
        self.add_line("cross-vertical",(24,15),(24,27))
        self.relate("connect","cross-horizontal","cross-vertical")

