"""Feedback names the phone. The rejected phone is much too narrow compared with the reference. Widen the portrait device, retain equal corner radii, and balance the two vibration strokes.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: smartphone.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e5eda811-8fbc-4a56-bb99-a31e94e69ea2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__vibrating-mobile-device-solo-b004-14/20260928T171322Z-thuan-mac/reference/rectangle stacked_e5eda811-8fbc-4a56-bb99-a31e94e69ea2.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the wider portrait phone and two detached vibration strokes. Each side has a readable 2px visible gap; the overall 44px square ink envelope remains inset within the 48px canvas. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'f70c0cb9033dbeb88325c30d73bd76e6e4b25aded46fae84df7c7980f3f4d7e9'}
    icon_id='vibrating-mobile-device-solo-b004-14'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('rectangle', 'stacked')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        box('phone',10,4,38,44,3)
        for n,x in [('left',4),('right',44)]:line(n+'-vibration',(x,12),(x,36))


    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='E':self.add_arc(ident,start,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,True),('A',(x,y+r),r,True),('A',(x-r,y),r,True),('A',(x,y-r),r,True)],True)
    def box(self,n,l,t,r,b,q):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,True),('L',(r,b-q)),('A',(r-q,b),q,True),('L',(l+q,b)),('A',(l,b-q),q,True),('L',(l,t+q)),('A',(l+q,t),q,True)],True)

