"""A folded page contains a circular head and open shoulder bust. Human-reference user.svg proportions reviewed. This attempt has radius-5 head centered (22,16) and shoulder apex (22,28), so the centerline gap is 7 and visible ink gap is 3, one unit short of the required 4.
Construction references: Lucide file for page construction. Human proportions follow icon_set/references/human_ref/user.svg: circular head, broad shoulders and open bottom."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96e78ff1-3119-4911-8baf-721686e578a7'
SOURCE_PATH = 'icon_set/work/todo-references/file person_96e78ff1-3119-4911-8baf-721686e578a7.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'file-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface/files'
    aliases = ()
    keywords = ('file', 'person', 'user', 'portrait')

    def page(self):
        self.add_line("page-top",(12,4),(28,4)); self.add_line("page-fold-edge",(28,4),(40,16)); self.add_line("page-right",(40,16),(40,40))
        self.add_arc("page-br",(40,40),(36,44),radius_x=4); self.add_line("page-bottom",(36,44),(12,44)); self.add_arc("page-bl",(12,44),(8,40),radius_x=4)
        self.add_line("page-left",(8,40),(8,8)); self.add_arc("page-tl",(8,8),(12,4),radius_x=4)
        self.add_contour("page","page-top","page-fold-edge","page-right","page-br","page-bottom","page-bl","page-left","page-tl",closed=True)
        # The reference page shows a clipped corner, not an inner fold crease.

    def circle(self,name,x,y,r):
        self.add_arc(name+"-upper",(x-r,y),(x+r,y),radius_x=r,sweep=False); self.add_arc(name+"-lower",(x+r,y),(x-r,y),radius_x=r,sweep=False)
        self.add_contour(name,name+"-upper",name+"-lower",closed=True)

    def build(self):
        self.page()
        self.circle("head",23,17,5)
        self.add_bezier("shoulder-left",(16,36),((16,32),(19,30),(23,30)))
        self.add_bezier("shoulder-right",(23,30),((27,30),(30,32),(30,36)))
        self.add_contour("shoulders","shoulder-left","shoulder-right")
