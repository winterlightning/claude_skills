"""Framed user bust with detached horizontal rules.
Symbol plan: preserve the reference's complete composition; shared parameters own repeated elements.
Keyshape SQUARE; exact profile envelope supplied by Keyshape.bounds_for.
Omissions: Continuous neck replaced with the shared circular-head bust vocabulary.
Lucide: scan-face; rounded contour and coherent stroke construction where applicable.
Human reference: icon_set/references/human_ref/user.svg for portrait modules.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1dccf6db-d157-5a7b-98f3-d179b8bf43ee'
SOURCE_PATH='icon_set/work/todo-references/frame human_1dccf6db-d157-5a7b-98f3-d179b8bf43ee.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='frame-human-floating'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'images'
    categories = ('images', 'primitives')
    aliases=()
    keywords=('frame', 'human')

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

        self.add_line('top-rule',(6,6),(42,6))
        self.add_line('bottom-rule',(6,42),(42,42))
        self.box('frame',6,14,36,20)
        self.circle('head',24,22,3)
        self.add_bezier('shoulders',(15,34),((15,33),(19,33),(24,33)),((29,33),(33,33),(33,34)))
        self.relate('connect','shoulders','frame')

