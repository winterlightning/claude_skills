"""Framed male portrait with rounded shoulders.
Symbol plan: preserve the reference's complete composition; shared parameters own repeated elements.
Keyshape SQUARE; exact profile envelope supplied by Keyshape.bounds_for.
Omissions: Tiny ears and connected neck reduced to the shared circular head; lower band merges with frame base.
Lucide: scan-face; rounded contour and coherent stroke construction where applicable.
Human reference: icon_set/references/human_ref/user.svg for portrait modules.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d468b110-3c09-45a7-a6de-e6ecf180916a'
SOURCE_PATH='icon_set/work/todo-references/frame man_d468b110-3c09-45a7-a6de-e6ecf180916a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='frame-man'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'images'
    categories = ('images', 'primitives')
    aliases=()
    keywords=('frame', 'man')

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

        self.box('frame',6,6,36,36)
        self.add_line('top-band',(6,14),(42,14));self.relate('connect','top-band','frame')
        self.circle('head',24,25,3)
        self.add_bezier('shoulders',(14,42),((14,38),(19,36),(24,36)),((29,36),(34,38),(34,42)))
        self.relate('connect','shoulders','frame')

