"""A speech bubble with a lightning-shaped break in its upper edge.
Review before drawing: The current broad, short notch resembles a heart indentation; the original has a long angular lightning crack and an inset tail.
Reviewer feedback: Manual fix request (no more specific instruction).
Plan: SQUARE ink extremes (4,4)-(44,44). Restore long tapered lightning fracture and inset lower-left tail while retaining rounded exterior corners.
Construction reference: Lucide message-square original and atoms: continuous rounded enclosure and integrated tail. Source determines the lightning fracture.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9390f65a-a76b-451f-b66d-2d0bd6fbda66'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__broken-speech-bubble-batch-003/20260928T164600Z-thuan-mac/reference/language barrier broken bubble_9390f65a-a76b-451f-b66d-2d0bd6fbda66.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broken-speech-bubble-batch-003'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('broken', 'speech', 'bubble', 'batch', '003')

    def build(self):

        def path(n, start, steps, closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                p=f'{n}-{i}'
                if kind=='L': self.add_line(p,here,end)
                elif kind=='A': self.add_arc(p,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(p,here,(args[0],args[1],end))
                here=end;members.append(p)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def poly(n,*pts): self.add_polyline(n,*pts,closed=pts[0]==pts[-1])
        def line(n,a,b): self.add_line(n,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('bubble',(10,6),[('L',(19,6)),('L',(25,14)),('L',(21,17)),('L',(30,28)),('L',(28,19)),('L',(32,16)),('L',(29,6)),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,30)),('A',(38,34),4,4,True),('L',(23,34)),('L',(12,42)),('L',(12,34)),('L',(10,34)),('A',(6,30),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)

# User explicitly delegated drawing-specific exceptions after UI/UX review.
Drawing.exception = {'reason': 'Preserve the long lightning fracture from the source rather than a broad heart-like notch. Its intentional taper and 1.8px narrowest measured parallel gap read clearly in both native-size themes.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-28', 'svg_sha256': 'e77eea2056e703931c0cb3370de5b11408a3df570b34b484814fb18eb5b4c8db'}
