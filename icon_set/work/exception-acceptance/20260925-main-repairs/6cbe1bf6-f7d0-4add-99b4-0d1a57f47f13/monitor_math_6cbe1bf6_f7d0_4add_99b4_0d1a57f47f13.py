'Computer monitor with math symbols.\nPlan: VRECT_L supplies height for division dots at pitch 8, the lower-left plus and an 8-unit stand.\nReference: monitor; Display frame and centered stand; intentional diagonal symbol arrangement retained.\nChanges: No marks omitted; frame made taller with square corners and shorter operator bars.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6cbe1bf6-f7d0-4add-99b4-0d1a57f47f13'
SOURCE_PATH = 'pictographic-primitives/other/monitor math_6cbe1bf6-f7d0-4add-99b4-0d1a57f47f13.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'monitor-math'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('monitor math',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)

    def rounded(self,n,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)

    def monitor(self):
        self.add_polyline('screen',(8,4),(40,4),(40,36),(24,36),(8,36),closed=True)
        self.add_line('stand',(24,36),(24,44))
        self.add_polyline('foot',(16,44),(24,44),(32,44))
        self.relate('connect','screen','stand');self.relate('connect','stand','foot')

    def banknote(self):
        self.add_polyline('note',(4,8),(44,8),(44,40),(4,40),closed=True)
        # Paired eight-unit corner quadrants meet the note edges.
        arcs=[((12,8),(4,16)),((44,16),(36,8)),((4,32),(12,40)),((36,40),(44,32))]
        for i,(a,b) in enumerate(arcs):
            self.add_arc('corner-'+str(i),a,b,radius_x=8)
            self.relate('connect','note','corner-'+str(i))

    def build(self):
        self.monitor()
        self.add_polyline('plus-h',(16,26),(19,26),(22,26))
        self.add_polyline('plus-v',(19,24),(19,26),(19,28))
        self.relate('connect','plus-h','plus-v')
        self.add_line('divide-bar',(28,20),(32,20))
        for i,y in enumerate((12,28)):self.add_dot('divide-dot-'+str(i),(30,y))

PARENT_MODULE = 'icon_set/model/icons/solo/monitor_math_6cbe1bf6_f7d0_4add_99b4_0d1a57f47f13.py'

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '914c36f07721e5ea2fb76e22b7dc204b597743dd59a9ff8a6c4a9634851ee119', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '6cbe1bf6-f7d0-4add-99b4-0d1a57f47f13'}
