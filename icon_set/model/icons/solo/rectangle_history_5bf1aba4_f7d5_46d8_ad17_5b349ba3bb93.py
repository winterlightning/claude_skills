from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93'
SOURCE_PATH='icon_set/work/todo-references/rectangle history_5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93.svg'
AUTHOR='gpt-6'
PLAN='A clipped-corner history document with a clock and bottom text rule.'
OMISSIONS='Clock face ticks omitted, retaining both hands.'
LUCIDE_REFERENCE='file-clock'
HUMAN_REFERENCE=None
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='rectangle-history'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('rectangle', 'history')

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
        # A clipped-corner history document with a clock and bottom text rule.

        self.add_polyline('document',(8,4),(32,4),(40,12),(40,44),(8,44),closed=True)
        self.circle('clock',24,22,9)
        self.add_polyline('hands',(24,18),(24,22),(27,22))
        self.add_line('rule',(16,36),(32,36))

