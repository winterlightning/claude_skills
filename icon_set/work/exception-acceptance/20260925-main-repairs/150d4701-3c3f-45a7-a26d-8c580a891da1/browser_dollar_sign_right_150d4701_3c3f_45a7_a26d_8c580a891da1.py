from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '150d4701-3c3f-45a7-a26d-8c580a891da1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__browser-dollar-sign-right/20260925T035753Z-thuan-mac/reference/browser dollar sign right_150d4701-3c3f-45a7-a26d-8c580a891da1.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'browser-dollar-sign-right'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # Square browser window at left and a curved dollar on the right; its two S bowls share radius 5. Move the dollar beside the browser to preserve its conventional shape.
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*p,closed=False): self.add_contour(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,k=4):
            line(n+'t',(l+k,t),(r-k,t));arc(n+'tr',(r-k,t),(r,t+k),k)
            line(n+'r',(r,t+k),(r,b-k));arc(n+'br',(r,b-k),(r-k,b),k)
            line(n+'b',(r-k,b),(l+k,b));arc(n+'bl',(l+k,b),(l,b-k),k)
            line(n+'l',(l,b-k),(l,t+k));arc(n+'tl',(l,t+k),(l+k,t),k)
            contour(n,*[n+x for x in ['t','tr','r','br','b','bl','l','tl']],closed=True)

        box('browser',4,13,26,35)
        line('toolbar',(4,21),(26,21));join('browser','toolbar')
        line('s-top',(44,14),(39,14))
        arc('s-upper',(39,14),(39,24),5,s=False)
        arc('s-lower',(39,24),(39,34),5)
        line('s-bottom',(39,34),(34,34))
        contour('dollar-s','s-top','s-upper','s-lower','s-bottom')
        line('stem-top',(39,10),(39,14));line('stem-bottom',(39,34),(39,38))
        join('dollar-s','stem-top');join('dollar-s','stem-bottom')

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '07c5599a5f922b85ccdf66468e7c22899510fbbac0f553726508e21396df6090', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '150d4701-3c3f-45a7-a26d-8c580a891da1'}
