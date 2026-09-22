"""A notched ticket crossed by a cancellation slash. HRECT_L spans centerlines x=4..44 and y=8..40. Lucide ticket-x supplies the rounded corner and inward notch principle; the source supplies cancellation semantics. The slash intentionally occludes the ticket; no false join is declared. Tiny ticket markings omitted.

Source rendered and inspected before authoring. Preserve the saved user classification.
Lucide image and ticket-x originals and atomic geometry informed coherent contours
and rounded enclosures; human reference used only for the three human scenes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '72224c18-af36-58a9-9579-12f4f96d0a1a'
SOURCE_PATH = 'pictographic-primitives/entertainment/cut_72224c18-af36-58a9-9579-12f4f96d0a1a.svg'
AUTHOR = 'gpt-6'

class QueueIcon(Solo48):
    icon_id = 'canceled-ticket-voucher'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ('Canceled Ticket Voucher',)
    keywords = ('canceled', 'ticket', 'voucher')
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
        self.add_line('top',(8,12),(40,12))
        self.add_arc('ne',(40,12),(44,16),radius_x=4)
        self.add_line('right-upper',(44,16),(44,20))
        self.add_arc('right-notch',(44,20),(44,28),radius_x=4,sweep=False)
        self.add_line('right-lower',(44,28),(44,32))
        self.add_arc('se',(44,32),(40,36),radius_x=4)
        self.add_line('bottom',(40,36),(8,36))
        self.add_arc('sw',(8,36),(4,32),radius_x=4)
        self.add_line('left-lower',(4,32),(4,28))
        self.add_arc('left-notch',(4,28),(4,20),radius_x=4,sweep=False)
        self.add_line('left-upper',(4,20),(4,16))
        self.add_arc('nw',(4,16),(8,12),radius_x=4)
        self.add_contour('ticket','top','ne','right-upper','right-notch','right-lower','se','bottom','sw','left-lower','left-notch','left-upper','nw',closed=True)
        self.add_line('cancel',(6,8),(42,40))
        self.relate('occlude','cancel','ticket')
