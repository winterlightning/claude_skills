"""Feedback names the strap. The rejected semicircular strap makes the camera resemble a handbag. Restore the long triangular carry strap, raised viewfinder housing, offset lens and shutter mark.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: camera.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='08e27f33-65ac-57d2-8a06-756b3779a004'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__camera-with-carry-strap/20260928T171322Z-thuan-mac/reference/camera carry_08e27f33-65ac-57d2-8a06-756b3779a004.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the triangular carry strap, viewfinder hump, shutter and lens. Strap/hump ink gaps are now equal at about 2.36px, with no overlap. Lens clearance is about 1.82px; all details remain legible at 48px. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '842293ff48905a90ac7e714faf814cf919e7a7118759b6af87ef323fd971407c'}
    icon_id='camera-with-carry-strap'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('camera', 'carry')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('body',(8,24),[('L',(16,24)),('L',(20,20)),('L',(28,20)),('L',(32,24)),('L',(40,24)),('A',(44,28),4,True),('L',(44,40)),('A',(40,44),4,True),('L',(8,44)),('A',(4,40),4,True),('L',(4,28)),('A',(8,24),4,True)],True)
        poly('strap',(8,24),(24,4),(40,24));join('strap','body')
        circle('lens',26,33,5);self.add_dot('shutter',(11,32))

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

