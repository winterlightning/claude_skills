"""A right-directed cursor arrow inside a large round target with a smaller circle overlapping its right rim. Main left semicircle has center (20,24), radius 16; smaller target center (36,24), radius 8. Preserve directional asymmetry.
Lucide mouse-pointer: clear directional silhouette; circular composition comes from the supplied reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f5615c5-bf24-47d6-91f8-143df2544bf8'
SOURCE_PATH = 'icon_set/work/todo-references/cursor move target right_5f5615c5-bf24-47d6-91f8-143df2544bf8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cursor-move-target-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('cursor', 'move', 'target', 'right')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded(self, name, l, t, r, b, radius):
        q=radius
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
        for j in range(8):
            if j%2: self.add_arc(name+str(j),pts[j],pts[j+1],radius_x=q)
            else: self.add_line(name+str(j),pts[j],pts[j+1])
        self.add_contour(name, *(name+str(j) for j in range(8)), closed=True)

    def build(self):

        self.add_arc('main-left',(20,40),(20,8),radius_x=16)
        self.add_bezier('main-top',(20,8),((27,8),(32,11),(36,16)))
        self.add_bezier('main-bottom',(36,32),((32,37),(27,40),(20,40)))
        self.add_contour('main','main-bottom','main-left','main-top')
        self.add_arc('target-right',(36,16),(36,32),radius_x=8)
        self.add_arc('target-left',(36,32),(36,16),radius_x=8)
        self.add_contour('target','target-right','target-left',closed=True)
        self.relate('connect','main','target')
        self.add_polyline('shaft',(13,24),(20,24))
        self.add_polyline('arrow',(16,20),(20,24),(16,28))
        self.relate('connect','shaft','arrow')
