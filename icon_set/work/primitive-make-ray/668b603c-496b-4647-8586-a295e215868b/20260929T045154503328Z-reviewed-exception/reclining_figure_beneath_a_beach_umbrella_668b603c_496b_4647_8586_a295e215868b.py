from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '668b603c-496b-4647-8586-a295e215868b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__reclining-figure-beneath-a-beach-umbrella/20260929T043927Z-thuan-mac/reference/beach person water parasol_668b603c-496b-4647-8586-a295e215868b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': "Preserve the umbrella, articulated reclining person and water as a complete scene. Wider/taller composition and the compact canopy/head and legs/water gaps remain readable at 48 pixels; detached head-to-torso clearance is exactly 4 units. Visually reviewed at 48px in light and dark themes under the user's explicit delegated exception authorization.", 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'f17965d0d76e1531f2242fe7753e81c1186605bf46243fb9aa4f9d59131fc4e6'}
    icon_id = 'reclining-figure-beneath-a-beach-umbrella'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('beach person water parasol',)

    # Revision plan: The swimmer/recliner was reduced to a floating angular mark and the umbrella nearly touched the water. Restore an articulated reclining body beneath a wide canopy.
    def build(self):

        # Canopy left, reclining person with distinct raised knees right, low water ripples.
        self.add_arc('canopy',(4,14),(20,14),radius_x=8,radius_y=8)
        self.add_line('canopy-base',(20,14),(4,14))
        self.add_contour('umbrella','canopy','canopy-base',closed=True)
        self.add_line('pole',(12,14),(10,35))
        self.circle('head',28,20,4)
        self.curve('torso',(28,32),((28,34),(28,36),(31,36)))
        self.add_polyline('legs',(31,36),(38,28),(44,35))
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
