"""A house inside a broken circular market chart.
Plan: CIRCLE uses center (24,24), radius20 centerline / radius22 ink to open the central space.
Reduction: Omitted the undersized doorway; preserved the broken ring and thick upper-right quadrant.
Construction: Lucide house: closed roof-and-wall outline; supplied source owns the surrounding chart.
Layout: House deliberately sits slightly left and low to clear the emphasized upper-right segment."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='1228a3cf-b0ac-41b8-a4db-2d272fbe1241'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/real estate market house_1228a3cf-b0ac-41b8-a4db-2d272fbe1241.svg'
AUTHOR = "gpt-6"
PLAN='A house sits inside an open circular market ring with a thick upper-right segment.'
OMISSIONS='Omitted the undersized doorway; preserved the broken ring and thick upper-right quadrant.'
LUCIDE_REFERENCE='house'
HUMAN_REFERENCE=None
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='real-estate-market-house'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('real', 'estate', 'market', 'house')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for j,a in enumerate(pts):
            b=pts[(j+1)%8];name=f'{n}-{j}';names.append(name)
            if j%2:self.add_arc(name,a,b,radius_x=r)
            else:self.add_line(name,a,b)
        self.add_contour(n,*names,closed=True)

    def house(self,n,x,y,w,h):
        mid=x+w//2
        self.add_polyline(n,(x,y+8),(mid,y),(x+w,y+8),(x+w,y+h),(x,y+h),closed=True)

    def bust(self,n,x,y,r,shoulder_w,shoulder_h):
        self.circle(n+'-head',x,y,r)
        body_top=y+r+8
        self.add_arc(n+'-shoulders',(x-shoulder_w,body_top+shoulder_h),(x+shoulder_w,body_top+shoulder_h),radius_x=shoulder_w,radius_y=shoulder_h)
        # Exact detached gap: (y+r+8) - (y+r) = 8 centerline / 4 ink.

    def build(self):
        # CIRCLE radius20 centerline: broken market ring, thick quadrant, house.
        # The doorway is omitted to leave a clear central house opening.
        self.add_arc('ring',(12,8),(40,36),radius_x=20,large_arc=True,sweep=False)
        self.add_arc('segment-outer',(24,4),(44,24),radius_x=20)
        self.add_arc('segment-inner',(36,24),(24,12),radius_x=12,sweep=False)
        self.add_line('segment-end',(44,24),(36,24));self.add_line('segment-start',(24,12),(24,4))
        self.add_contour('segment','segment-outer','segment-end','segment-inner','segment-start',closed=True)
        self.add_polyline('house',(16,26),(22,22),(28,26),(28,32),(16,32),closed=True)
