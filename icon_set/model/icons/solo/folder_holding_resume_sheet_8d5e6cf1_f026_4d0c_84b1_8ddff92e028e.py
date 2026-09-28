"""An open tabbed folder physically holding an upright resume page.
SQUARE; one foreground folder contour and one partially occluded paper run.
Shared endpoints at page entry points; corner radii share 4-unit definition.
Lucide folder-open supplies tab and sloping front construction. The source
supplies the projecting sheet. Photo box omitted; one text rule remains.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "8d5e6cf1-f026-4d0c-84b1-8ddff92e028e"
SOURCE_PATH = "pictographic-primitives/_uncategorized_32/recruiting employee folder resume document_8d5e6cf1-f026-4d0c-84b1-8ddff92e028e.svg"
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = "folder-holding-resume-sheet"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("Employee Resume Folder",)
    keywords = ("folder", "resume", "document", "paper", "office", "recruitment")
    def build(self):
        self.add_arc('front-corner',(6,26),(10,22),radius_x=4)
        nodes=[(10,22),(14,22),(20,28),(38,28),(42,28),(40,38)]
        for j,(a,b) in enumerate(zip(nodes,nodes[1:]),1):
            self.add_line(f'front-top-{j}',a,b)
        self.add_bezier('front-lower-right',(40,38),((40,40),(38,42),(36,42)))
        self.add_line('front-bottom',(36,42),(10,42))
        self.add_arc('front-lower-left',(10,42),(6,38),radius_x=4)
        self.add_line('front-left',(6,38),(6,26))
        self.add_contour('folder','front-corner',*[f'front-top-{j}' for j in range(1,6)],'front-lower-right','front-bottom','front-lower-left','front-left',closed=True)
        self.add_line('page-left',(10,22),(10,10))
        self.add_arc('page-top-left',(10,10),(14,6),radius_x=4)
        self.add_line('page-top',(14,6),(34,6))
        self.add_arc('page-top-right',(34,6),(38,10),radius_x=4)
        self.add_line('page-right',(38,10),(38,28))
        self.add_contour('page','page-left','page-top-left','page-top','page-top-right','page-right')
        self.relate('connect','page-left','front-corner','front-top-1')
        self.relate('connect','page-right','front-top-3','front-top-4')
        self.add_line('text-rule',(20,16),(28,16))
