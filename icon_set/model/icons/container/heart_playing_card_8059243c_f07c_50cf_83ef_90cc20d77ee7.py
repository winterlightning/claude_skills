"""An upright rounded playing card containing a heart. VRECT_L preserves its portrait proportions. The heart uses two mirrored cubic sections meeting at its cleft and pointed base; smooth lobe tangents. The card has radius-6 corners.

Source rendered and inspected before authoring. Preserve the saved user classification.
Lucide image and ticket-x originals and atomic geometry informed coherent contours
and rounded enclosures; human reference used only for the three human scenes.
Hosting via compose.py using existing sub IDs: plus-sign-batch-04 valid, heart-state-63 review, check-mark review.
"""
from ...keyshapes import Keyshape
from ._base import Container64
SOURCE_ICON_ID = '8059243c-f07c-50cf-83ef-90cc20d77ee7'
SOURCE_PATH = 'pictographic-primitives/entertainment/fortune telling tarot_8059243c-f07c-50cf-83ef-90cc20d77ee7.svg'
AUTHOR = 'gpt-6'

class QueueIcon(Container64):
    icon_id = 'heart-playing-card'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ('Heart Playing Card',)
    keywords = ('heart', 'playing', 'card')
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
        self.add_bezier('heart',(32,25),((18,10),(9,31),(32,43)),((55,31),(46,10),(32,25)))
        self.add_contour('suit','heart',closed=True)
