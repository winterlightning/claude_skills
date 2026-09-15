"""Leaning palm with curved fronds, shoreline, sea wave and sun disk."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '276cf575-05e5-5bc9-906a-770f69748a36'
SOURCE_PATH = 'pictographic-primitives/outdoors/vacation beach_276cf575-05e5-5bc9-906a-770f69748a36.svg'
AUTHOR = 'gpt-6'

class BeachPalmTreeSun(Solo48):
    icon_id = 'beach-palm-tree-sun'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('beach', 'palm', 'tree', 'sun', 'outdoors', 'outdoors-batch-04')

    def build(self):
        # Plan: Leaning palm with curved fronds, shoreline, sea wave and sun disk.
        # Envelope (6,6)-(42,42). Shared endpoints own all attachments.
        # Lucide original/atomic-debug reference: tree-palm and sun.
        # Human reference: full_body_ref.png; head bottom12, shoulder20, ink gap4.
        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                part = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(part, here, end)
                else:
                    rx, ry, sweep = args
                    self.add_arc(part, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(part)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)

        circle('sun',37,11,5)
        path('trunk',(16,16),[('A',(6,34),10,18,False)])
        path('frond-up',(6,6),[('A',(16,16),10,10,True)]);join('frond-up','trunk')
        path('frond-right',(16,16),[('A',(24,24),8,8,True)]);join('frond-right','trunk');join('frond-right','frond-up')
        path('frond-left',(6,16),[('A',(16,16),10,6,True)]);join('frond-left','trunk');join('frond-left','frond-up');join('frond-left','frond-right')
        path('shore',(6,34),[('A',(24,42),18,8,False),('L',(42,42))]);join('shore','trunk')
        path('sea',(22,32),[('A',(32,32),5,1,False),('A',(42,32),5,1,True)])
