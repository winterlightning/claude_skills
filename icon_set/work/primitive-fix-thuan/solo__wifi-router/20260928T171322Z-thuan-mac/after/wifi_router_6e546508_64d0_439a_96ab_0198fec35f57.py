"""Feedback names Wi-Fi. The rejected router has only two tall semicircles and a filled-looking chassis. Restore three broad, shallow signal waves, antenna and a rounded open chassis.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: wifi; router.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6e546508-64d0-439a-96ab-0198fec35f57'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__wifi-router/20260928T171322Z-thuan-mac/reference/router signal_6e546508-64d0-439a-96ab-0198fec35f57.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the three shallow Wi-Fi waves and open router chassis. Natural envelope stays inside the canvas; smallest antenna-to-wave ink clearance is 2.4px, and the near-exact 4px curved wave gap remains an automatic advisory. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '32a1b50b62ae38532d8fe288e673d5fd40e4af169f2dccd722f9615cbf1b98c8'}
    icon_id='wifi-router'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('router', 'signal')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        for n,a,z,c1,c2 in [('outer-left',(8,9),(24,3),(13,5),(18,3)),('outer-right',(24,3),(40,9),(30,3),(35,5)),('middle-left',(14,16),(24,11),(17,13),(20,11)),('middle-right',(24,11),(34,16),(28,11),(31,13)),('inner',(20,23),(28,23),(22,20),(26,20))]:
            self.add_bezier(n,a,(c1,c2,z))
        self.add_contour('outer','outer-left','outer-right')
        self.add_contour('middle','middle-left','middle-right')
        path('case',(8,32),[('L',(24,32)),('L',(40,32)),('A',(44,36),4,True),('L',(44,38)),('A',(40,42),4,True),('L',(36,42)),('L',(12,42)),('L',(8,42)),('A',(4,38),4,True),('L',(4,36)),('A',(8,32),4,True)],True)
        line('antenna',(24,28),(24,32));join('antenna','case')
        for n,a,b in [('left-foot',(12,42),(10,44)),('right-foot',(36,42),(38,44))]:line(n,a,b);join(n,'case')


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

