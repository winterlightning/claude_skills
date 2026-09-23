"""User bust inside a frame with a top band.
Symbol plan: preserve the reference's complete composition; shared parameters own repeated elements.
Keyshape SQUARE; exact profile envelope supplied by Keyshape.bounds_for.
Omissions: Lower frame edge also serves as lower band; neck simplified to a detached head.
Lucide: scan-face; rounded contour and coherent stroke construction where applicable.
Human reference: icon_set/references/human_ref/user.svg for portrait modules.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='35f4f66d-633b-4b5d-a821-74e6678a80e0'
SOURCE_PATH='icon_set/work/todo-references/frame human_35f4f66d-633b-4b5d-a821-74e6678a80e0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='frame-human-banded'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
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

        self.box('frame',6,6,36,36)
        for y in (14,42):
            if y==14:
                self.add_line('top-band',(6,y),(42,y));self.relate('connect','top-band','frame')
        self.circle('head',24,25,3)
        self.add_bezier('shoulders',(14,42),((14,36),(19,36),(24,36)),((29,36),(34,36),(34,42)))
        self.relate('connect','shoulders','frame')


# Detached circular head bottom y=28; shoulder crest y=36.
# Exact centerline gap 8, visible ink gap 4; symmetry axis x=24.
