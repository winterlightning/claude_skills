"""A happy emoji reads an open book. SQUARE 6,6–42,42. Repair existing draft: parallel sloping page boundaries replace the bowtie-shaped page bases. Source supplies closed eyes and open book. Symmetry about x24 and shared page depth13; omit mouth, explicit fingers and page text. No exact local Lucide smile reference available."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '35d8adfa-635c-4306-8acd-147f2e6dbc87'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/emoji reading lover hug_35d8adfa-635c-4306-8acd-147f2e6dbc87.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'smiling-face-holding-open-book'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('Happy Smiling Face Reading a Book',)
    keywords = ('happy', 'smiling', 'face', 'reading', 'a', 'book')
    def build(self):
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[("A",(x,y+r),r,r,True),("A",(x,y-r),r,r,True)],True)
        path("face",(6,29),[("C",(24,6),(6,10),(11,6)),("C",(42,29),(37,6),(42,10))])
        for i,x in enumerate((18,30)):self.add_arc(f"eye-{i}",(x-2,19),(x+2,19),radius_x=2,sweep=True)
        self.add_polyline("book",(6,29),(24,33),(42,29),(42,38),(24,42),(6,38),closed=True)
        self.add_line("fold",(24,33),(24,42))
        self.relate("connect","fold","book")
        self.relate("connect","face","book")

