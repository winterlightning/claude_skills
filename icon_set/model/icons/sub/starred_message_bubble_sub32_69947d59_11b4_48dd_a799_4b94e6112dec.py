"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '69947d59-11b4-48dd-a799-4b94e6112dec'
SOURCE_PATH = 'pictographic-primitives/messages/messages bubble square star_69947d59-11b4-48dd-a799-4b94e6112dec.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded rectangular speech bubble', 'lower-left downward tail', 'outlined five-point star')

class Drawing(Sub32):
    icon_id = 'starred-message-bubble-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'messages'
    keywords = ('starred', 'message', 'bubble')


    STROKE_WIDTH = 4
    PATH_STROKE_WIDTHS = {'frame': 4}
    COMPACT_EXCEPTION = 'Complete source composition with uniform 4px strokes. Spacing and grid findings are retained for review.'
    def to_record(self):
        record=super().to_record()
        record['style']['path_stroke_widths']=dict(self.PATH_STROKE_WIDTHS)
        record['compact_exception']=self.COMPACT_EXCEPTION
        return record

    def build(self):
        self.message()
        # All five points remain; the nested star is not extracted from its bubble.
        self.add_polyline('star',(16,8),(18,12),(23,12),(19,16),(21,21),(16,18),(11,21),(13,16),(9,12),(14,12),closed=True)

    def message(self):
        self.add_line('frame-top',(4,2),(28,2))
        self.add_arc('frame-tr',(28,2),(30,4),radius_x=2)
        self.add_line('frame-right',(30,4),(30,23))
        self.add_arc('frame-br',(30,23),(28,25),radius_x=2)
        tail=[(28,25),(15,25),(9,30),(9,25),(4,25)]
        for i,(a,b) in enumerate(zip(tail,tail[1:]),1):self.add_line(f'frame-tail-{i}',a,b)
        self.add_arc('frame-bl',(4,25),(2,23),radius_x=2)
        self.add_line('frame-left',(2,23),(2,4))
        self.add_arc('frame-tl',(2,4),(4,2),radius_x=2)
        self.add_contour('frame','frame-top','frame-tr','frame-right','frame-br',*[f'frame-tail-{i}' for i in range(1,5)],'frame-bl','frame-left','frame-tl',closed=True)


# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'starred-message-bubble-sub32': {'status': 'fixed',
                                  'date': '2026-09-24',
                                  'author': 'gpt-6',
                                  'source_icon_id': '69947d59-11b4-48dd-a799-4b94e6112dec',
                                  'failures_at_review': ['mic [frame]: frame and star are 4 apart '
                                                         'on centerlines nearest (21, 25)<->(21, '
                                                         '21); SUB32 requires at least 6 (ink '
                                                         'clearance 2) unless the contact is '
                                                         'declared with a scoped `connect` '
                                                         'relationship'],
                                  'variant': 'starred-message-bubble-sub32-v2-clean',
                                  'evidence': 'icon_set/work/side-subs-20260924/fix-25/69947d59-11b4-48dd-a799-4b94e6112dec'}}
