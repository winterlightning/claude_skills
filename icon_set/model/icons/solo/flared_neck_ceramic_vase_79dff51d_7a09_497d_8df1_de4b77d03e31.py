'A symmetrical ceramic vase with flared rim, narrow neck and rounded belly. VRECT_L fits the upright vessel. One contour, with the left side derived by reversing and mirroring the right side about x24. Exact extremes x8/x40 and y4/y44. Source supplies the blank ceramic silhouette; no decorative details added. Lucide amphora informs continuous vessel side contours; handles are absent from this reference.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79dff51d-7a09-497d-8df1-de4b77d03e31'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/pottery_79dff51d-7a09-497d-8df1-de4b77d03e31.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'flared-neck-ceramic-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ['Decorative Ceramic Vase']
    keywords = []
    def build(self):
        right=[((34,8),(30,10),(30,14)),((30,18),(40,19),(40,28)),((40,34),(35,41),(32,44))]
        self.add_line('rim',(12,4),(36,4))
        self.add_bezier('right',(36,4),*right)
        self.add_line('base',(32,44),(16,44))
        mirror=lambda p:(48-p[0],p[1])
        starts=[(36,4)]+[segment[2] for segment in right[:-1]]
        left=[(mirror(c2),mirror(c1),mirror(start)) for start,(c1,c2,end) in reversed(list(zip(starts,right)))]
        self.add_bezier('left',(16,44),*left)
        self.add_contour('vase','rim','right','base','left',closed=True)
