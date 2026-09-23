"""A folded portrait page contains an outlined shield and a compact plus mark. The plus uses a short vertical bar and central dot; the source composition remains whole, with the spacing blocker retained.
Construction references: Lucide file and shield-check: folded page and shield construction. The source uses a medical plus."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd1c4154e-8c68-4782-9c5a-e5c81055a594'
SOURCE_PATH = 'icon_set/work/todo-references/file with shield plus_d1c4154e-8c68-4782-9c5a-e5c81055a594.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'file-with-shield-plus'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface/files'
    aliases = ()
    keywords = ('file', 'shield', 'medical', 'plus', 'security')

    def page(self):
        self.add_line("page-top",(12,4),(28,4)); self.add_line("page-fold-edge",(28,4),(40,16)); self.add_line("page-right",(40,16),(40,40))
        self.add_arc("page-br",(40,40),(36,44),radius_x=4); self.add_line("page-bottom",(36,44),(12,44)); self.add_arc("page-bl",(12,44),(8,40),radius_x=4)
        self.add_line("page-left",(8,40),(8,8)); self.add_arc("page-tl",(8,8),(12,4),radius_x=4)
        self.add_contour("page","page-top","page-fold-edge","page-right","page-br","page-bottom","page-bl","page-left","page-tl",closed=True)
        # This source uses a diagonal page corner with no inner crease.

    def circle(self,name,x,y,r):
        self.add_arc(name+"-upper",(x-r,y),(x+r,y),radius_x=r,sweep=False); self.add_arc(name+"-lower",(x+r,y),(x-r,y),radius_x=r,sweep=False)
        self.add_contour(name,name+"-upper",name+"-lower",closed=True)

    def build(self):
        self.page()
        self.add_polyline("shield",(24,13),(32,17),(32,25),(29,30),(24,34),(19,30),(16,25),(16,17),(24,13),closed=True)
        self.add_dot("plus-horizontal",(24,22))
        self.add_line("plus-vertical",(24,20),(24,24))
        self.relate("connect","plus-horizontal","plus-vertical")
