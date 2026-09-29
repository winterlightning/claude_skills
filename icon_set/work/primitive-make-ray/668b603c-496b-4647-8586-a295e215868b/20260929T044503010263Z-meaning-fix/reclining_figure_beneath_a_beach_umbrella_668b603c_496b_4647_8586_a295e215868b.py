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

        # Broad umbrella left; detached head and reclining bent legs right; low water line.
        self.add_arc('canopy',(4,17),(24,17),radius_x=10,radius_y=9)
        self.add_line('canopy-base',(24,17),(4,17))
        self.add_contour('umbrella','canopy','canopy-base',closed=True)
        self.add_line('pole',(14,17),(12,34))
        self.circle('head',30,21,4)
        self.curve('torso',(30,33),((30,36),(25,37),(22,37)))
        self.add_polyline('legs',(22,37),(34,31),(42,37))
        self.relate('connect','torso','legs')
        self.mark_human_figure('recliner',head='head',torso='torso',torso_junction='start')
        self.curve('water',(4,40),((8,44),(11,44),(15,40)),((19,44),(22,44),(26,40)),((30,44),(33,44),(37,40)),((40,43),(42,43),(44,40)))

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
