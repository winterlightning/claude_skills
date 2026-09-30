"""The rejected licorice uses hard polygon corners and straight bands. Restore smooth interwoven diagonal strands with rounded ends.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct Lucide match; source supplies diagonal twist and soft contours.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1585cb8b-c5e4-42ee-9bc9-6f53342a6281'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__twisted-licorice-strands/20260929T145934Z-thuan-mac/reference/licorice_1585cb8b-c5e4-42ee-9bc9-6f53342a6281.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='twisted-licorice-strands'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('twisted', 'licorice', 'strands')
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

        path('left-strand',(6,36),[('C',(14,22),(6,31),(10,25)),('C',(30,14),(20,19),(26,19)),('L',(36,6)),('A',(42,12),5,5,True),('C',(34,26),(42,18),(38,23)),('C',(18,34),(28,29),(22,29)),('L',(12,42)),('A',(6,36),5,5,True)],True)
        path('wrap1',(6,36),[('C',(34,26),(14,36),(28,28))]);join('wrap1','left-strand')
        path('wrap2',(14,22),[('C',(42,12),(23,22),(35,15))]);join('wrap2','left-strand')
