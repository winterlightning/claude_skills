"""Restore a left-facing long-snouted serpent with curved belly, a large pointed bat wing and a tapering tail."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '73f4cc87-427b-5322-aec8-d42d4ff0929d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__winged-serpent-dragon/20260929T085457Z-thuan-mac/reference/fantasy amphiptere dragon_73f4cc87-427b-5322-aec8-d42d4ff0929d.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'winged-serpent-dragon'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve the long snout, narrow serpentine body and large bat wing. The neck strip is intentionally narrow and the asymmetric outline keeps its natural proportions instead of being stretched into the square keyshape.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'eef5995c623c622d57ed2009f740cd77d108a43649fbfba5653497c71b1b4b34'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('fantasy amphiptere dragon',)
    # Symbol plan: Restore a left-facing long-snouted serpent with curved belly, a large pointed bat wing and a tapering tail.
    # Construction: No useful Lucide fantasy match; original reference controls the asymmetrical wing and serpentine silhouette.

    def path(self, name, start, *segments, closed=False):
        ids = []
        point = start
        for j, segment in enumerate(segments):
            eid = f"{name}-{j}"
            if len(segment) == 2:
                self.add_line(eid, point, segment)
                end = segment
            else:
                end, rx, ry, sweep, large = segment
                self.add_arc(eid, point, end, radius_x=rx, radius_y=ry,
                             sweep=sweep, large_arc=large)
            ids.append(eid)
            point = end
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), ((x+r,y),r,r,True,False),
                  ((x-r,y),r,r,True,False), closed=True)

    def oval(self, name, x, y, rx, ry):
        self.path(name, (x-rx,y), ((x+rx,y),rx,ry,True,False),
                  ((x-rx,y),rx,ry,True,False), closed=True)

    def box(self, name, x1,y1,x2,y2,r=3):
        self.path(name, (x1+r,y1), (x2-r,y1),
                  ((x2,y1+r),r,r,True,False), (x2,y2-r),
                  ((x2-r,y2),r,r,True,False), (x1+r,y2),
                  ((x1,y2-r),r,r,True,False), (x1,y1+r),
                  ((x1+r,y1),r,r,True,False), closed=True)

    def build(self):

        self.path('head-back',(5,29),(5,24),(14,16),(13,22),
                  ((24,25),12,7,True,False))
        self.path('belly-tail',(5,29),(12,29),((23,30),11,8,True,False),
                  (38,40),((14,38),16,11,True,False))
        self.path('wing',(24,25),((19,4),27,25,False,False),
                  ((43,15),34,27,True,False),((38,22),7,8,False,False),
                  ((38,40),29,20,True,False),((29,23),25,22,False,False))
        self.relate('connect','head-back','belly-tail')
        self.relate('connect','head-back','wing')
        self.relate('connect','belly-tail','wing')
     
