"""Rejected hand is angular and paper loses its upper edge and text. Restore a curved thumb gripping an outlined document with two legible text strokes.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: hand; file-text.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1a5b8e57-e476-5e0e-a43f-45bc8105f4e5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hand-holding-document/20260928T173014Z-thuan-mac/reference/digital policies data breach_1a5b8e57-e476-5e0e-a43f-45bc8105f4e5.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-holding-document'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('digital', 'policies', 'data', 'breach')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('paper',(16,18),[('L',(8,18)),('A',(4,22),4,False),('L',(4,40)),('A',(8,44),4,False),('L',(28,44)),('L',(28,24))])
        path('hand-top',(44,4),[('L',(36,10)),('L',(26,10)),('C',(16,18),(21,10),(19,14))]);join('hand-top','paper')
        path('thumb',(26,16),[('L',(20,22)),('C',(24,28),(16,26),(20,31)),('L',(28,24)),('L',(32,20)),('L',(38,20)),('L',(44,15))]);join('thumb','paper')
        line('text-one',(10,32),(20,32));line('text-two',(10,38),(20,38))


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

