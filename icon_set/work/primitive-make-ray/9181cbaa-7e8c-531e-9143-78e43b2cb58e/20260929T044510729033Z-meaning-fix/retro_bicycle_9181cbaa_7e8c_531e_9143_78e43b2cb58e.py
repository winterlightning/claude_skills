from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9181cbaa-7e8c-531e-9143-78e43b2cb58e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__retro-bicycle/20260929T043927Z-thuan-mac/reference/bicycle retro_9181cbaa-7e8c-531e-9143-78e43b2cb58e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'retro-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('bicycle retro',)

    # Revision plan: The wheels were undersized and the retro handlebar was a heavy hook. Restore larger wheels, the diamond frame, a slim saddle and curled handlebar.
    def build(self):

        # Equal larger wheels and shared frame nodes; intentional classic bicycle asymmetry.
        for x in (13,35):self.circle('wheel-'+str(x),x,31,9)
        self.add_polyline('frame',(13,31),(24,31),(31,17),(18,17),(13,31))
        self.add_line('seat-tube',(18,12),(24,31))
        self.add_line('saddle',(13,12),(23,12));self.relate('connect','seat-tube','saddle')
        self.add_polyline('fork',(35,31),(30,8),(35,8))
        self.add_arc('handlebar',(35,8),(35,16),radius_x=4)
        self.relate('connect','fork','handlebar');self.relate('connect','frame','seat-tube')

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
