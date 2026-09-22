"""A wide framed landscape with two mountain peaks and a sun. HRECT_L spans x=2..62 and y=10..54. Lucide image informs the rounded enclosure and compact landscape. The outer frame owns a separate inset opening and mountains/sun. Angular peaks replace fine source curvature for clarity.

Source rendered and inspected before authoring. Preserve the saved user classification.
Lucide image and ticket-x originals and atomic geometry informed coherent contours
and rounded enclosures; human reference used only for the three human scenes.
Hosting via compose.py using existing sub IDs: plus-sign-batch-04 invalid, heart-state-63 invalid, check-mark invalid.
"""
from ...keyshapes import Keyshape
from ._base import Container64
SOURCE_ICON_ID = '2225e58f-a12a-431b-a3b2-b7ca04198743'
SOURCE_PATH = 'pictographic-primitives/entertainment/museum painting_2225e58f-a12a-431b-a3b2-b7ca04198743.svg'
AUTHOR = 'gpt-6'

class QueueIcon(Container64):
    icon_id = 'framed-landscape-painting'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ('Framed Landscape Painting',)
    keywords = ('framed', 'landscape', 'painting')
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
        rounded('frame',2,10,62,54,5)
        self.add_polyline('opening',(10,18),(54,18),(54,46),(10,46),(10,18))
        self.add_polyline('hills',(18,38),(28,33),(35,40),(43,27),(48,38))
        circle('sun',18,26,2)
