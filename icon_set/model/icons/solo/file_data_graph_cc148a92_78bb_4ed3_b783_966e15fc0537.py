"""A portrait sheet carries a rising data polyline. One rising graph stroke preserves the data-graph identity; spacing rules require omitting the two source rules.
Construction references: Lucide file and file-chart-column-increasing: folded page and compact chart strokes. The source has a plot and two lower rules."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc148a92-78bb-4ed3-b783-966e15fc0537'
SOURCE_PATH = 'icon_set/work/todo-references/file data graph_cc148a92-78bb-4ed3-b783-966e15fc0537.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'file-data-graph'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('file', 'document', 'data', 'graph', 'chart')

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
        self.page()
        self.add_polyline("plot",(18,34),(22,29),(25,32),(30,24))

