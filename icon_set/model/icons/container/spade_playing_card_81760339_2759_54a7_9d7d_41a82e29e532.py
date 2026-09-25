"""An upright rounded playing card containing a pointed spade and broad stem. VRECT_L preserves portrait proportions. Suit geometry mirrors about x=32; curved lobes and a single contiguous stem contour preserve the source identity. Card corners have radius 6.

Source rendered and inspected before authoring. Preserve the saved user classification.
Lucide image and ticket-x originals and atomic geometry informed coherent contours
and rounded enclosures; human reference used only for the three human scenes.
Hosting via compose.py using existing sub IDs: plus-sign-batch-04 invalid, heart-state-63 valid, check-mark valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64
SOURCE_ICON_ID = '81760339-2759-54a7-9d7d-41a82e29e532'
SOURCE_PATH = 'pictographic-primitives/entertainment/spades card_81760339-2759-54a7-9d7d-41a82e29e532.svg'
AUTHOR = 'gpt-6'

class QueueIcon(Container64):
    icon_id = 'spade-playing-card'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ('Spade Playing Card',)
    keywords = ('spade', 'playing', 'card')
    def build(self):

        def circle(name,x,y,r):
            self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        def rounded(name,l,t,r,b,rad):
            points=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
            ids=[]
            for j,p in enumerate(points):
                q=points[(j+1)%8]; part=f'{name}-{j}'; ids.append(part)
                if j%2: self.add_arc(part,p,q,radius_x=rad)
                else: self.add_line(part,p,q)
            self.add_contour(name,*ids,closed=True)
        def note(name,x,y):
            circle(name+'-head',x,y,2)
            self.add_polyline(name+'-stem',(x+2,y),(x+2,y-10),(x+6,y-8))
            self.relate('connect',name+'-head',name+'-stem')
        rounded('card',10,2,54,62,6)
        self.add_bezier('spade',(32,17),((24,24),(12,31),(21,37)),((25,40),(29,36),(28,36)))
        self.add_line('base-1',(28,36),(26,47))
        self.add_line('base-2',(26,47),(38,47))
        self.add_line('base-3',(38,47),(36,36))
        self.add_bezier('right',(36,36),((35,36),(39,40),(43,37)),((52,31),(40,24),(32,17)))
        self.add_contour('suit','spade','base-1','base-2','base-3','right',closed=True)
