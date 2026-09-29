"""Rejected tiny spaced rings read as an abstract triangular symbol. Enlarge the eggs and stack them into a compact mound with visible circular interiors."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='e625a592-a7be-4a88-9cc8-1a1640f52612'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pyramid-of-round-caviar-eggs/20260929T041010Z-thuan-mac/reference/caviar_e625a592-a7be-4a88-9cc8-1a1640f52612.svg'
AUTHOR='gpt-6'
PLAN='Rejected tiny spaced rings read as an abstract triangular symbol. Enlarge the eggs and stack them into a compact mound with visible circular interiors.'
CONSTRUCTION_REFERENCE='No useful subject-specific Lucide match; original reference determines the silhouette.'
OMISSIONS='All six eggs retained; deliberate close packing preserves a pile of caviar.'
class Drawing(Solo48):
    icon_id='pyramid-of-round-caviar-eggs'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        r=5
        for n,(x,y) in enumerate(((24,13),(16,25),(32,25),(9,37),(24,37),(39,37))): self.circle(f'egg-{n}',x,y,r)
