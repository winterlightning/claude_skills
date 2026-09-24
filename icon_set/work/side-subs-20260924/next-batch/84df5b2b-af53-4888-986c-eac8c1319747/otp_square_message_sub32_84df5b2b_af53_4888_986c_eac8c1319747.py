"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '84df5b2b-af53-4888-986c-eac8c1319747'
SOURCE_PATH = 'pictographic-primitives/state/message otp_84df5b2b-af53-4888-986c-eac8c1319747.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square speech bubble', 'lower-left tail', 'uppercase OTP in source order')

class Drawing(Sub32):
    icon_id = 'otp-square-message-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('otp', 'message', 'bubble')
    TYPEFACE_GLYPH_IDS = ('letter-o-uppercase', 'letter-t-uppercase', 'letter-p-uppercase')

    def build(self):
        self.message()
        self.primitives.append(Bezier('text-O-0-0-0-0',Point(*(6, 15)),Point(*(11, 15)),(((6, 13.674426), (6.263572, 12.401788), (6.732233, 11.464466)), ((7.200894, 10.527144), (7.837213, 10), (8.5, 10)), ((9.162787, 10), (9.799106, 10.527144), (10.267767, 11.464466)), ((10.736428, 12.401788), (11, 13.674426), (11, 15)))))
        self.primitives.append(Bezier('text-O-0-0-0-1',Point(*(11, 15)),Point(*(6, 15)),(((11, 16.325574), (10.736428, 17.598212), (10.267767, 18.535534)), ((9.799106, 19.472856), (9.162787, 20), (8.5, 20)), ((7.837213, 20), (7.200894, 19.472856), (6.732233, 18.535534)), ((6.263572, 17.598212), (6, 16.325574), (6, 15)))))
        self.add_contour('glyph-O-0-0-0',*['text-O-0-0-0-0', 'text-O-0-0-0-1'],closed=True)
        self.add_line('text-T-0-0-0-0',(15, 10),(19, 10))
        self.add_line('text-T-0-1-0-0',(17, 10),(17, 20))
        self.add_line('text-P-0-0-0-0',(24, 20),(24, 10))
        self.add_line('text-P-0-0-0-1',(24, 10),(26.08, 10))
        self.add_contour('glyph-P-0-0-0',*['text-P-0-0-0-0', 'text-P-0-0-0-1'],closed=False)
        self.primitives.append(Bezier('text-P-0-0-1-0',Point(*(26.08, 10)),Point(*(26.08, 15.277778)),(((28.64, 10), (28.64, 15.277778), (26.08, 15.277778)),)))
        self.add_line('text-P-0-0-2-0',(26.08, 15.277778),(24, 15.277778))

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

