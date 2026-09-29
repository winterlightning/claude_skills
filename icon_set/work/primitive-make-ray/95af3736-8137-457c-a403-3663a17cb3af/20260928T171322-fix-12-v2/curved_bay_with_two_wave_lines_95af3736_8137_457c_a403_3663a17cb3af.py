"""Rejected shoreline is a square step and its waves are thick short blobs. Restore the smooth inlet, broad curved basin and two longer gentle wave lines.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: No useful local Lucide bay/waves match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='95af3736-8137-457c-a403-3663a17cb3af'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__curved-bay-with-two-wave-lines/20260928T171322Z-thuan-mac/reference/bay_95af3736-8137-457c-a403-3663a17cb3af.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='curved-bay-with-two-wave-lines'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('bay',)
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('coast',(4,12),[('A',(8,8),4,True),('L',(18,8)),('C',(32,22),(28,8),(22,22)),('L',(40,22)),('L',(40,28)),('C',(28,40),(40,35),(36,40)),('L',(20,40)),('C',(4,26),(10,40),(4,35)),('L',(4,12))],True)
        path('right-shore',(40,22),[('L',(40,14)),('C',(44,8),(40,10),(41,8))]);join('right-shore','coast')
        path('wave-top',(10,21),[('C',(22,21),(14,18),(18,24))])
        path('wave-bottom',(14,31),[('C',(23,31),(17,28),(20,34)),('C',(32,31),(26,28),(29,34))])


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

