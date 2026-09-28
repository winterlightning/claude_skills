"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '05032593-c317-46fb-9187-d42561ffa0d2'
SOURCE_PATH = 'pictographic-primitives/state/circle thumbs up_05032593-c317-46fb-9187-d42561ffa0d2.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('circular frame', 'continuous raised-thumb silhouette', 'left wrist edge without an added cuff divider')

class Drawing(Sub32):
    icon_id = 'circle-thumbs-up-sub32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    keywords = ('thumbs', 'up', 'approval', 'symbol')


    STROKE_WIDTH = 4
    PATH_STROKE_WIDTHS = {'frame': 4}
    COMPACT_EXCEPTION = 'Complete source composition with uniform 4px strokes. Spacing and grid findings are retained for review.'
    def to_record(self):
        record=super().to_record()
        record['style']['path_stroke_widths']=dict(self.PATH_STROKE_WIDTHS)
        record['compact_exception']=self.COMPACT_EXCEPTION
        return record

    def build(self):
        self.circle('frame',16,16,14)
        self.add_line('wrist',(8,16),(8,23))
        self.add_bezier('palm',(8,23),((11,23),(11,25),(15,25)),((17,25),(19,25),(20,25)),((22,25),(22,23),(23,20)),((24,17),(25,15),(22,15)))
        self.add_line('fingers',(22,15),(18,15))
        self.add_bezier('thumb',(18,15),((19,13),(20,10),(19,8)),((18,6),(17,8),(16,10)),((14,14),(12,16),(8,16)))
        self.add_contour('hand','wrist','palm','fingers','thumb',closed=True)

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

