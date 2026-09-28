"""Restore the jagged torn seam and diagonal top tape seam on the perspective parcel.
Plan: named coherent contours; repeated elements share parameters.
Keyshape: SQUARE for the subject's natural orientation.
Construction: Lucide box: shared perspective corners and clean joined faces.
Reduction: Short tape end simplified; retain the defining jagged tear.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '958637b4-0216-5d2f-a6a7-e9708b032af8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__damaged-shipping-box/20260925T083122Z-thuan-mac/reference/logistic damaged package_958637b4-0216-5d2f-a6a7-e9708b032af8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Retain the diagonal tape and visible jagged torn seam that identify a damaged package. The tape has 3.16px ink clearance and a short local tear/lid gap is below the 4px target; these remain distinct at 48px. The tear end stays visibly separate from the bottom edge.', 'approved_by': 'user-delegated-to-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'dd435467b89b80deac960b11f0bdde51caaf71b6e89acab20839f3cd65be0842'}
    icon_id = 'damaged-shipping-box'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('logistic', 'damaged', 'package')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        poly('outline',(24,6),(42,15),(42,33),(24,42),(6,33),(6,15),(14,11),closed=True)
        poly('lid',(6,15),(24,24),(32,20),(42,15));join('lid','outline')
        line('tape',(14,11),(32,20));join('tape','outline');join('tape','lid')
        poly('tear',(24,24),(24,30),(29,28),(31,33));join('tear','lid')
        line('bottom-seam',(24,39),(24,42));join('bottom-seam','outline')
