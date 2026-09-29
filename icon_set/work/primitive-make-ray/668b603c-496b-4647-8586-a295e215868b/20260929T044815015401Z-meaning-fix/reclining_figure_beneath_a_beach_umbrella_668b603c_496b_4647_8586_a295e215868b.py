from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '668b603c-496b-4647-8586-a295e215868b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__reclining-figure-beneath-a-beach-umbrella/20260929T043927Z-thuan-mac/reference/beach person water parasol_668b603c-496b-4647-8586-a295e215868b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'reclining-figure-beneath-a-beach-umbrella'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('beach person water parasol',)

    # Revision plan: The swimmer/recliner was reduced to a floating angular mark and the umbrella nearly touched the water. Restore an articulated reclining body beneath a wide canopy.
    def build(self):

        # Separate the canopy, circular head, bent reclining pose and low water ripples.
        self.add_arc('canopy',(4,15),(22,15),radius_x=9,radius_y=9)
        self.add_line('canopy-base',(22,15),(4,15))
        self.add_contour('umbrella','canopy','canopy-base',closed=True)
        self.add_line('pole',(13,15),(11,35))
        self.circle('head',32,22,4)
        self.curve('torso',(32,34),((32,36),(27,36),(24,36)))
        self.add_polyline('legs',(24,36),(36,34),(43,38))
        self.relate('connect','torso','legs')
        self.mark_human_figure('recliner',head='head',torso='torso',torso_junction='start')
        self.curve('water',(4,43),((7,46),(10,46),(14,43)),((17,46),(20,46),(24,43)),((27,46),(30,46),(34,43)),((37,46),(40,46),(44,43)))

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
