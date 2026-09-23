"""Sloped open folder with stepped rear tab.
Symbol plan: preserve the reference's complete composition; shared parameters own repeated elements.
Keyshape HRECT_L; exact profile envelope supplied by Keyshape.bounds_for.
Omissions: Only small corner fillets omitted.
Lucide: folder-open; rounded contour and coherent stroke construction where applicable.
Human reference: icon_set/references/human_ref/user.svg for portrait modules.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='11f861f7-9062-4cbd-a3fd-0cba990dfc4b'
SOURCE_PATH='icon_set/work/todo-references/folder open_11f861f7-9062-4cbd-a3fd-0cba990dfc4b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='folder-open-sloped'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('folder', 'open')

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

        self.add_polyline('back',(4,40),(4,8),(16,8),(24,16),(36,16),(36,24))
        self.add_polyline('front',(4,40),(12,24),(44,24),(38,40),(4,40))
        self.relate('connect','back','front')

