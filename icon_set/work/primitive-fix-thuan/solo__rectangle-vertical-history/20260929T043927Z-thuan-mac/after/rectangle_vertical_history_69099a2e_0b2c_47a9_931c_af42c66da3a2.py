from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '69099a2e-0b2c-47a9-931c-af42c66da3a2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rectangle-vertical-history/20260929T043927Z-thuan-mac/reference/rectangle vertical history_69099a2e-0b2c-47a9-931c-af42c66da3a2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': "Preserve the clock hands and return arrow inside the portrait card. Compact interior spacing is essential to distinguish history from a plain card or return arrow. Visually reviewed at 48px in light and dark themes under the user's explicit delegated exception authorization.", 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'cc7944308fe7b30eaa489f60a5029a997e42f5a420e96c75e315d8f0b1d2f4ba'}
    icon_id = 'rectangle-vertical-history'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('rectangle vertical history',)

    # Revision plan: The history symbol lost the clock face and recognizable return arrow. Restore a circular clock with hands and a small clockwise return arrow on the portrait card.
    def build(self):

        self.rect('card',8,4,32,40,5)
        self.curve('clock',(33,21),((31,11),(15,11),(14,23)),((13,34),(25,37),(31,31)))
        self.add_polyline('arrow',(28,20),(33,21),(34,15))
        self.add_polyline('hands',(23,19),(23,25),(27,28))

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
