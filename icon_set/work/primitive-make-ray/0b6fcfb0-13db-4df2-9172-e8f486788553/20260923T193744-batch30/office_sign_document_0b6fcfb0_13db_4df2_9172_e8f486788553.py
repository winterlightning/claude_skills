"""A pen signing a document.

Symbol plan: Open page contour behind a diagonal outlined pen. SQUARE ink extremes (4,4)-(44,44).
Construction: pencil: diagonal body, pointed tip and rounded cap; file-text: page perimeter.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0b6fcfb0-13db-4df2-9172-e8f486788553'
SOURCE_PATH = 'icon_set/work/todo-references/office sign document_0b6fcfb0-13db-4df2-9172-e8f486788553.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'office-sign-document'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('office', 'sign', 'document')

    def build(self):
        self.add_line('top',(10,6),(34,6))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_line('left',(6,38),(6,10))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('right',(42,28),(42,38))
        self.add_contour('page','right','br','bottom','bl','left','tl','top')
        self.add_line('pen-edge-1',(30,14),(18,26))
        self.add_line('pen-edge-2',(18,26),(14,38))
        self.add_line('pen-edge-3',(14,38),(26,34))
        self.add_line('pen-edge-4',(26,34),(38,22))
        self.add_bezier('pen-cap',(38,22),((46,14),(38,6),(30,14)))
        self.add_contour('pen','pen-edge-1','pen-edge-2','pen-edge-3','pen-edge-4','pen-cap',closed=True)
        self.add_line('cap-seam',(27,17),(35,25))
        self.relate('connect','cap-seam','pen')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-upper', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-lower', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-upper', name+'-lower', closed=True)

    def box(self, name, x, y, right, bottom, r=4):
        # A single radius owns all four tangent corners.
        pts=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),
             (right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i in range(8):
            n=f'{name}-{i}'; a=pts[i]; b=pts[(i+1)%8]
            if a == b:
                continue
            if i%2:
                self.add_arc(n,a,b,radius_x=r)
            else:
                self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def clipboard(self):
        # Clip capsule and open board share the two lateral attachment nodes.
        self.box('clip',16,4,32,12,4)
        self.add_line('board-top-right',(32,8),(36,8))
        self.add_arc('board-tr',(36,8),(40,12),radius_x=4)
        self.add_line('board-right',(40,12),(40,40))
        self.add_arc('board-br',(40,40),(36,44),radius_x=4)
        self.add_line('board-bottom',(36,44),(12,44))
        self.add_arc('board-bl',(12,44),(8,40),radius_x=4)
        self.add_line('board-left',(8,40),(8,12))
        self.add_arc('board-tl',(8,12),(12,8),radius_x=4)
        self.add_line('board-top-left',(12,8),(16,8))
        self.add_contour('board','board-top-right','board-tr','board-right','board-br','board-bottom','board-bl','board-left','board-tl','board-top-left')
        self.relate('connect','board','clip')

