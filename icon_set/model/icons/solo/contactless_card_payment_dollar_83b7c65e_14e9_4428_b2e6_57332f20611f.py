from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '83b7c65e-14e9-4428-b2e6-57332f20611f'
SOURCE_PATH = 'pictographic-primitives/payments/contactless payment_83b7c65e-14e9-4428-b2e6-57332f20611f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'contactless-card-payment-dollar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'payments'
    categories = ('primitives', 'payments')
    aliases = ()
    keywords = ('contactless payment',)
    # Plan: A payment card with contactless radio waves instead of an ambiguous touching hand.
    # Construction references: Lucide nfc: concentric wireless arcs; original contactless payment: card and wireless cue.
    # Omissions: Dollar and holding hand omitted so the contactless payment concept remains clear.
    def build(self):
        # Payment card in the lower right; radiating arcs at upper left show NFC.
        self.box('card',18,30,24,12,2)
        self.path('signal-outer',(6,24),[((24,6),18,18,False)])
        self.path('signal-inner',(6,15),[((15,6),9,9,False)])

    def path(self, name, start, steps, closed=False):
        current = start
        ids = []
        for index, step in enumerate(steps):
            ident = f"{name}-{index}"
            if len(step) == 2:
                self.add_line(ident, current, step)
                current = step
            else:
                end, rx, ry, sweep = step
                self.add_arc(ident, current, end, radius_x=rx, radius_y=ry, sweep=sweep)
                current = end
            ids.append(ident)
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name, (cx-r,cy), [((cx+r,cy),r,r,True),((cx-r,cy),r,r,True)], True)

    def box(self, name, x, y, w, h, r=3):
        self.path(name,(x+r,y),[(x+w-r,y),((x+w,y+r),r,r,True),(x+w,y+h-r),
            ((x+w-r,y+h),r,r,True),(x+r,y+h),((x,y+h-r),r,r,True),(x,y+r),((x+r,y),r,r,True)],True)
