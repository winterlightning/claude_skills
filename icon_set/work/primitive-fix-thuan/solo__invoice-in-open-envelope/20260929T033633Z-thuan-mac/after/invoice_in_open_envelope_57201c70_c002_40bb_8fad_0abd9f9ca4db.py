"""invoice mail.
Plan: Rebuilt the open envelope around a projecting invoice, with side flaps, lower flap, two item lines and a dollar mark.
Construction: mail-open: diagonal side folds and open envelope silhouette.
Keyshape: SQUARE; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '57201c70-c002-40bb-8fad-0abd9f9ca4db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__invoice-in-open-envelope/20260929T033633Z-thuan-mac/reference/invoice mail_57201c70-c002-40bb-8fad-0abd9f9ca4db.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'invoice-in-open-envelope'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('invoice', 'mail')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

    def build(self):

        self.add_polyline('paper',(10,26),(10,4),(38,4),(38,26))
        self.add_polyline('envelope',(10,17),(4,22),(4,41),(44,41),(44,22),(38,17))
        self.add_polyline('flap',(4,41),(20,29),(28,29),(44,41))
        self.add_line('fold-left',(4,22),(15,30));self.add_line('fold-right',(44,22),(33,30))
        self.relate('connect','envelope','flap');self.relate('connect','fold-left','envelope');self.relate('connect','fold-right','envelope')
        for y in [12,20]:self.add_line('item'+str(y),(16,y),(20,y))
        self.add_bezier('dollar',(32,11),((26,9),(24,14),(29,15)),((35,16),(32,22),(26,20)))
        self.add_line('currency-top',(29,7),(29,10));self.add_line('currency-bottom',(29,21),(29,24))

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Preserve an invoice with a dollar mark and item lines projecting above a folded open envelope. Small fold corners and nested text clearance are essential to distinguish invoice mail.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': 'cddf58c2f3dddd2d250209f81c1023e66e832437de028eb1f950840b5ca58d45'}
