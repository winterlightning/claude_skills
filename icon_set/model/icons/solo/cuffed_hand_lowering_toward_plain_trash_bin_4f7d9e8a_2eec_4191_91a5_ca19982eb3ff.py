"""Hand Putting Waste In Trash Can.
Symbol plan: Cuffed hand reaches above a tapered bin; a rounded fingertip and short thumb preserve the gesture.
Reference construction: hand and trash; human_ref/user.svg.
VRECT_L visible extremes: (6, 2, 42, 46); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4f7d9e8a-2eec-4191-91a5-ca19982eb3ff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/recycling hand trash_4f7d9e8a-2eec-4191-91a5-ca19982eb3ff.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'cuffed-hand-lowering-toward-plain-trash-bin'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    aliases = ()
    keywords = ('hand', 'bin', 'trash', 'waste', 'disposal', 'cuff', 'recycling', 'ecology')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def contour(n,*parts,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members) & set(parts)]
            self.add_contour(n,*parts,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r:
                poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2: arc(n+str(i),a,b,r)
                else: line(n+str(i),a,b)
            contour(n,*(n+str(i) for i in range(8)),closed=True)
        poly('hand-upper',(40,4),(32,4),(26,4),(14,7))
        arc('fingertips',(14,7),(14,17),5,sweep=False)
        poly('hand-lower',(14,17),(26,13),(32,13),(40,13))
        contour('hand','hand-upper-1','hand-upper-2','hand-upper-3','fingertips','hand-lower-1','hand-lower-2','hand-lower-3')
        line('thumb',(26,13),(22,17))
        line('cuff',(32,4),(32,13))
        poly('rim',(8,26),(12,26),(36,26),(40,26))
        line('wall-left',(12,26),(12,40))
        arc('corner-left',(12,40),(16,44),4,sweep=False)
        line('base',(16,44),(32,44))
        arc('corner-right',(32,44),(36,40),4,sweep=False)
        line('wall-right',(36,40),(36,26))
        contour('bin','wall-left','corner-left','base','corner-right','wall-right')
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
