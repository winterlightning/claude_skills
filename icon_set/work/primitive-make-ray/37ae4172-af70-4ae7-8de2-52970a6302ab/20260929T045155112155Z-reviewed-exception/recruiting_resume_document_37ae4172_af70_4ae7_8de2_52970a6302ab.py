from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '37ae4172-af70-4ae7-8de2-52970a6302ab'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__recruiting-resume-document/20260929T043927Z-thuan-mac/reference/recruiting resume document_37ae4172-af70-4ae7-8de2-52970a6302ab.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': "Preserve the resume portrait, two text lines and candidate bust. Compact text spacing and page-to-candidate separation retain the complete recruiting meaning at native size. Visually reviewed at 48px in light and dark themes under the user's explicit delegated exception authorization.", 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '6259c3ce67aefdda2f38f98f1f98fbd3e348b3aa2c6b4bfa6948005a8d6b1c38'}
    icon_id = 'recruiting-resume-document'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('recruiting resume document',)

    # Revision plan: The page became an E-shaped bracket and the candidate looked like a small bucket. Restore a document outline, portrait panel, text lines and a clear candidate bust.
    def build(self):

        # Resume page at left; person overlaps the open right edge as in the original.
        self.add_polyline('page',(29,6),(6,6),(6,42),(21,42))
        self.add_polyline('portrait',(14,14),(22,14),(22,22),(14,22),closed=True)
        self.add_line('text-1',(14,30),(23,30))
        self.add_line('text-2',(14,36),(21,36))
        self.circle('candidate-head',35,17,4)
        self.curve('candidate-shoulders',(28,42),((28,34),(30,29),(35,29)),((40,29),(42,34),(42,42)))
        self.add_line('candidate-base',(28,42),(42,42))
        self.relate('connect','candidate-shoulders','candidate-base')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def rect(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for k in range(8):
            a,b=pts[k],pts[(k+1)%8]
            if k%2:self.add_arc(n+str(k),a,b,radius_x=r)
            else:self.add_line(n+str(k),a,b)
        self.add_contour(n,*[n+str(k) for k in range(8)],closed=True)

    def curve(self,n,start,*segs):
        self.add_bezier(n,start,*segs)

    def star(self,n,x,y,s):
        # Five-point silhouette, shared integer vertices for each star instance.
        p=[(0,-6),(2,-2),(6,-2),(3,1),(4,6),(0,3),(-4,6),(-3,1),(-6,-2),(-2,-2)]
        self.add_polyline(n,*[(x+round(a*s/6),y+round(b*s/6)) for a,b in p],closed=True)
