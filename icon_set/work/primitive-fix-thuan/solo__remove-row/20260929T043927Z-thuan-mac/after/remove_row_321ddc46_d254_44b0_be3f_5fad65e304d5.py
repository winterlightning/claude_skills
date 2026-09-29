from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '321ddc46-d254-44b0-be3f-5fad65e304d5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__remove-row/20260929T043927Z-thuan-mac/reference/remove row_321ddc46-d254-44b0-be3f-5fad65e304d5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'remove-row'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('remove row',)

    # Revision plan: The isolated X and two rules no longer clearly described a table row. Restore a table grid with a delete X aligned to its middle row.
    def build(self):

        self.rect('table',20,8,24,32,2)
        for y in (18,30):self.add_line('row-'+str(y),(20,y),(44,y));self.relate('connect','table','row-'+str(y))
        self.add_polyline('delete-a',(4,20),(12,28))
        self.add_polyline('delete-b',(4,28),(12,20))

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
