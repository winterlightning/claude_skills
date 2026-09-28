"""Fresh reconstruction of hotel single bed from the supplied reference.
Construction references: Lucide bed-single. Symbol plan recorded in build().
Profile SOLO48, keyshape HRECT_L; final findings are recorded alongside this module.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ec421b89-c7d9-573b-bec3-256a6da2bdb4'
SOURCE_PATH = 'pictographic-primitives/hotels/hotel single bed_ec421b89-c7d9-573b-bec3-256a6da2bdb4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-bed-with-pillow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hotel', 'single', 'bed')

    def circle(self, n, x, y, r):
        self.add_arc(n+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(n+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def box(self,n,l,t,r,b,k=4,top=(),bottom=()):
        p=[(l+k,t),*[(x,t) for x in sorted(top)],(r-k,t),(r,t+k),(r,b-k),(r-k,b),*[(x,b) for x in sorted(bottom,reverse=True)],(l+k,b),(l,b-k),(l,t+k)]
        ids=[]
        for i,(a,z) in enumerate(zip(p,p[1:]+p[:1])):
            if a==z:continue
            name=f'{n}-{i}';ids.append(name)
            if a[0]!=z[0] and a[1]!=z[1]:self.add_arc(name,a,z,radius_x=k)
            else:self.add_line(name,a,z)
        self.add_contour(n,*ids,closed=True)

    def build(self):
        # Broad headboard, centered pillow and lower mattress; shared attachment nodes.
        self.add_line('head-left',(8,25),(8,12))
        self.add_arc('head-tl',(8,12),(12,8),radius_x=4)
        self.add_line('head-top',(12,8),(36,8))
        self.add_arc('head-tr',(36,8),(40,12),radius_x=4)
        self.add_line('head-right',(40,12),(40,25))
        self.add_contour('headboard','head-left','head-tl','head-top','head-tr','head-right')
        self.add_line('pillow-left',(17,25),(17,19))
        self.add_arc('pillow-tl',(17,19),(19,17),radius_x=2)
        self.add_line('pillow-top',(19,17),(29,17))
        self.add_arc('pillow-tr',(29,17),(31,19),radius_x=2)
        self.add_line('pillow-right',(31,19),(31,25))
        self.add_contour('pillow','pillow-left','pillow-tl','pillow-top','pillow-tr','pillow-right')
        self.add_line('front-left',(4,40),(4,33))
        self.add_line('front-left-upper',(4,33),(4,29))
        self.add_arc('front-tl',(4,29),(8,25),radius_x=4)
        self.add_polyline('blanket',(8,25),(17,25),(31,25),(40,25))
        self.add_arc('front-tr',(40,25),(44,29),radius_x=4)
        self.add_line('front-right-upper',(44,29),(44,33))
        self.add_line('front-right',(44,33),(44,40))
        self.contours[:] = [c for c in self.contours if c.contour_id != 'blanket']
        self.add_contour('front','front-left','front-left-upper','front-tl','blanket-1','blanket-2','blanket-3','front-tr','front-right-upper','front-right')
        self.add_line('base',(4,33),(44,33))
        self.relate('connect','front','headboard')
        self.relate('connect','front','pillow')
        self.relate('connect','front','base')
