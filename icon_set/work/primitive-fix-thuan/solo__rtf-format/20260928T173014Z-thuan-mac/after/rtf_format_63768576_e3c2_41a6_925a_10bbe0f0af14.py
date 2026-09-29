"""Rejected page has irregular corners and cramped panel. Restore uniform rounded page corners and a taller two-cell panel; preserve source without adding literal letters.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: file.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='63768576-e3c2-41a6-925a-10bbe0f0af14'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rtf-format/20260928T173014Z-thuan-mac/reference/rtf format_63768576-e3c2-41a6-925a-10bbe0f0af14.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='rtf-format'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('rtf', 'format')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('page',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,40)),('A',(36,44),4,True),('L',(12,44)),('A',(8,40),4,True),('L',(8,8)),('A',(12,4),4,True)],True)
        path('panel',(20,17),[('L',(28,17)),('A',(31,20),3,True),('L',(31,25)),('L',(31,32)),('A',(28,35),3,True),('L',(20,35)),('A',(17,32),3,True),('L',(17,25)),('L',(17,20)),('A',(20,17),3,True)],True)
        line('divider',(17,25),(31,25));join('divider','panel')


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

