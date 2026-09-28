"""An upright rounded playing card containing a three-lobed club. VRECT_L preserves its portrait proportions; the centered suit mirrors about x=32. Rounded corner radius 6; lobes share one coherent curve. No corner rank or decorative detail added.

Source rendered and inspected before authoring. Preserve the saved user classification.
Lucide image and ticket-x originals and atomic geometry informed coherent contours
and rounded enclosures; human reference used only for the three human scenes.
Hosting via compose.py using existing sub IDs: plus-sign-batch-04 valid, heart-state-63 valid, check-mark valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64
SOURCE_ICON_ID = '72cddd13-b109-55d8-ad04-0b1b8a22fe0b'
SOURCE_PATH = 'pictographic-primitives/entertainment/clubs card_72cddd13-b109-55d8-ad04-0b1b8a22fe0b.svg'
AUTHOR = 'gpt-6'

class QueueIcon(Container64):
    icon_id = 'clubs-suit-playing-card'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ('Clubs Suit Playing Card',)
    keywords = ('clubs', 'suit', 'playing', 'card')
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
        self.add_bezier('club',(28,34),((12,38),(16,19),(26,25)),((20,10),(44,10),(38,25)),((48,19),(52,38),(36,34)))
        self.add_line('base-1',(36,34),(38,44))
        self.add_line('base-2',(38,44),(26,44))
        self.add_line('base-3',(26,44),(28,34))
        self.add_contour('suit','club','base-1','base-2','base-3',closed=True)
