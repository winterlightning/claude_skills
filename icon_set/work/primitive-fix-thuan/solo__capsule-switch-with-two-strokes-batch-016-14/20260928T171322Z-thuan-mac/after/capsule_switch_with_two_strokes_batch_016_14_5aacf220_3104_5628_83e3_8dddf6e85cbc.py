"""The rejected capsule is tall and nearly oval, and the two strokes are too long. Restore the wide pill shape and shorter equal bars toward the left.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: toggle-left.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5aacf220-3104-5628-83e3-8dddf6e85cbc'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__capsule-switch-with-two-strokes-batch-016-14/20260928T171322Z-thuan-mac/reference/settings off_5aacf220-3104-5628-83e3-8dddf6e85cbc.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the natural wide capsule proportions. The two short bars have exactly 4px geometric ink clearance to the horizontal walls; the curve-containing contour retains its uncertified equality finding. The natural height is smaller than HRECT_M. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '551e157eccbebaea56a97a828f4c6101a69391d9d81ca477a0de640510e0d9d4'}
    icon_id='capsule-switch-with-two-strokes-batch-016-14'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('settings', 'off')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('capsule',(14,14),[('L',(34,14)),('A',(44,24),10,True),('A',(34,34),10,True),('L',(14,34)),('A',(4,24),10,True),('A',(14,14),10,True)],True)
        for i in range(2):line('bar-'+str(i),(15+8*i,22),(15+8*i,26))


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

