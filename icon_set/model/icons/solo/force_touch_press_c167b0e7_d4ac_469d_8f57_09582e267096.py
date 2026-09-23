"""Bent finger pressing down on a surface with downward feedback arrow.
Symbol plan: preserve the reference's complete composition; shared parameters own repeated elements.
Keyshape SQUARE; exact profile envelope supplied by Keyshape.bounds_for.
Omissions: Surface thickness and tiny impact rays omitted.
Lucide: none; rounded contour and coherent stroke construction where applicable.
Human reference: icon_set/references/human_ref/user.svg for portrait modules.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c167b0e7-d4ac-469d-8f57-09582e267096'
SOURCE_PATH='icon_set/work/todo-references/force touch press_c167b0e7-d4ac-469d-8f57-09582e267096.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='force-touch-press'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('force', 'touch', 'press')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def box(self, name, x, y, w, h, r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            eid=f'{name}-{i}';ids.append(eid)
            if i%2:self.add_arc(eid,pts[i],pts[(i+1)%8],radius_x=r)
            else:self.add_line(eid,pts[i],pts[(i+1)%8])
        self.add_contour(name,*ids,closed=True)

    def build(self):

        self.add_bezier('finger',(22,6),((18,8),(15,15),(12,21)),((10,25),(14,28),(17,24)),((19,21),(20,15),(23,16)),((26,17),(22,21),(26,22)),((30,23),(29,14),(36,12)))
        self.add_line('surface-left',(6,34),(12,34))
        self.add_line('surface-right',(36,34),(42,34))
        self.add_polyline('press',(24,30),(24,42))
        self.add_polyline('arrow',(20,38),(24,42),(28,38))
        self.relate('connect','press','arrow')

