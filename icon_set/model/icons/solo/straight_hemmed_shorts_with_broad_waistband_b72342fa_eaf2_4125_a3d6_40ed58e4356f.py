'Straight-Hemmed Shorts with Broad Waistband.\nSymbol plan: A pair of shorts has a broad straight waistband and gently widening outer sides. A deep rounded gap separates the two legs, which end in flat hems without visible pockets or decoration.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: \nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b72342fa-eaf2-4125-a3d6-40ed58e4356f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/spandex_b72342fa-eaf2-4125-a3d6-40ed58e4356f.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'straight-hemmed-shorts-with-broad-waistband'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('shorts', 'clothing', 'waistband', 'legs', 'spandex', 'garment')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry,sweep=s)
        def bez(n,a,*s): self.add_bezier(n,a,*s)
        def con(n,*p,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members)&set(p)]
            self.add_contour(n,*p,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            ps=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                if j%2: arc(n+str(j),ps[j],ps[(j+1)%8],r)
                else: line(n+str(j),ps[j],ps[(j+1)%8])
            con(n,*(n+str(j) for j in range(8)),closed=True)
        poly('shorts',(10,6),(38,6),(42,42),(28,42),(28,34))
        arc('crotch',(28,34),(20,34),4,s=False)
        poly('left',(20,34),(20,42),(6,42),(10,6))
        con('shorts-outline',*['shorts-'+str(i) for i in range(1,5)],'crotch','left-1','left-2','left-3',closed=True)
        line('waist',(9,14),(39,14));self.relate('connect','waist','shorts-outline')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
