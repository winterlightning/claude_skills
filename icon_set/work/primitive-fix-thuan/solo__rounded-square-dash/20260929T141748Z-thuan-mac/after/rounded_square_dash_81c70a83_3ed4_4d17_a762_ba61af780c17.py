"""The rejected border has large curved corners and dot-like middle dashes. Restore a clearly dashed square with short rounded corners and equal central dashes.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide square-minus: shared corner radii and square enclosure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='81c70a83-3ed4-4d17-a762-ba61af780c17'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rounded-square-dash/20260929T141748Z-thuan-mac/reference/rounded square dash_81c70a83-3ed4-4d17-a762-ba61af780c17.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='rounded-square-dash'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('rounded', 'square', 'dash')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('nw',(6,10),[('L',(6,8)),('A',(8,6),2,2,True),('L',(10,6))])
        path('ne',(38,6),[('L',(40,6)),('A',(42,8),2,2,True),('L',(42,10))])
        path('se',(42,38),[('L',(42,40)),('A',(40,42),2,2,True),('L',(38,42))])
        path('sw',(10,42),[('L',(8,42)),('A',(6,40),2,2,True),('L',(6,38))])
        for y in (6,42):line('horizontal'+str(y),(20,y),(28,y))
        for x in (6,42):line('vertical'+str(x),(x,20),(x,28))
