from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ce1ed58e-e672-4d3c-afbe-79946ffec09f'
SOURCE_PATH = 'pictographic-primitives/holidays/hand_ce1ed58e-e672-4d3c-afbe-79946ffec09f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'open-palm-hand-ce1ed58e-e672-4d3c-afbe-79946ffec09f'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('hand',)
    def build(self):
        # Source-led upright hand: circular finger caps and a smooth, distinct thumb.
        # Shared curve vocabulary; maintain stroke4 instead of flattening the silhouette.
        members=[];here=(14,28)
        for i,(x,end,y,r) in enumerate(((14,21,14,3.5),(21,29,10,4),(29,36,14,3.5),(36,42,20,3))):
            self.add_line(f"side-{i}",here,(x,y));members.append(f"side-{i}")
            if r==3.5: self.add_bezier(f"tip-{i}",(x,y),((x,y-4*r/3),(end,y-4*r/3),(end,y)))
            else: self.add_arc(f"tip-{i}",(x,y),(end,y),radius_x=r)
            members.append(f"tip-{i}");here=(end,y)
        self.path("palm",here,[(42,29),((42,37),(37,42),(29,42)),(25,42),((20,42),(17,40),(14,36)),(7,28),((6,27),(6,27),(6,26)),((6,23),(9,23),(11,25)),(14,28)])
        self.contours[:]=[c for c in self.contours if c.contour_id!="palm"]
        self.add_contour("outline",*members,*[f"palm-{i}" for i in range(8)],closed=True)
        for x,y,end in ((21,14,25),(29,14,25),(36,20,26)):
            self.add_line(f"crease-{x}",(x,y),(x,end));self.relate("connect",f"crease-{x}","outline")

    def path(self,name,start,commands,closed=False):
        members=[]
        for i,c in enumerate(commands):
            tag=f"{name}-{i}"
            if len(c)==2: self.add_line(tag,start,c); start=c
            else: self.add_bezier(tag,start,c); start=c[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for i in range(4): self.add_arc(f"{name}-{i}",pts[i],pts[i+1],radius_x=r)
        self.add_contour(name,*[f"{name}-{i}" for i in range(4)],closed=True)

    def box(self,name,x,y,w,h,r=0):
        if not r:
            self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r),(x+r,y)]
        for i in range(8):
            if i%2: self.add_arc(f"{name}-{i}",pts[i],pts[i+1],radius_x=r)
            else: self.add_line(f"{name}-{i}",pts[i],pts[i+1])
        self.add_contour(name,*[f"{name}-{i}" for i in range(8)],closed=True)

    icon_id = 'open-palm-hand-ce1ed58e-e672-4d3c-afbe-79946ffec09f'
    category = 'holidays'
    aliases = ()
    keywords = ('open', 'palm', 'hand')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'reason': 'User approved the latest redraw shown in the seven remaining icons preview: "exception approval them". Accept the existing spacing, hole and internal-spacing findings for this exact drawing.', 'approved_on': '2026-09-25', 'svg_sha256': 'f12b522ac843ab742e3863cb5370d6f01c78bb9bfd5505632d06873b6bd5b650', 'source_svg_sha256': 'f12b522ac843ab742e3863cb5370d6f01c78bb9bfd5505632d06873b6bd5b650'}
