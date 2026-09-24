"""Framed female bust with a symmetrical hair silhouette and detached rules.
Symbol plan: preserve the reference's complete composition; shared parameters own repeated elements.
Keyshape SQUARE; exact profile envelope supplied by Keyshape.bounds_for.
Omissions: Face and neck simplified to circular head; tiny hair interior lines omitted.
Lucide: scan-face; rounded contour and coherent stroke construction where applicable.
Human reference: icon_set/references/human_ref/user.svg for portrait modules.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0289cf64-76d2-5178-94b9-4767e8076f59'
SOURCE_PATH='icon_set/work/todo-references/frame woman_0289cf64-76d2-5178-94b9-4767e8076f59.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='frame-woman'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('frame', 'woman')

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

    # Human construction reference: icon_set/references/human_ref/user.svg
    def build(self):

        self.add_line('top-rule',(6,6),(42,6))
        self.add_line('bottom-rule',(6,42),(42,42))
        self.box('frame',6,14,36,20)
        self.circle('head',24,23,3)
        self.add_bezier('hair',(15,29),((18,29),(14,17),(24,17)),((34,17),(30,29),(33,29)))
        self.add_bezier('shoulders',(14,34),((16,34),(20,34),(24,34)),((28,34),(32,34),(34,34)))
        self.relate('connect','shoulders','frame')

