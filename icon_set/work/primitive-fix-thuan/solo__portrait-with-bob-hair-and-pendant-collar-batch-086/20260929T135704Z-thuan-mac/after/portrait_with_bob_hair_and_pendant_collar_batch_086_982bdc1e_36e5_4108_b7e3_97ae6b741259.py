"""The rejected portrait has a narrow open hair arch and dot ornament. Broaden the bob, restore its flat ends and show a small horizontal pendant below the shoulder arch.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular jaw and rounded shoulder arch; touching bust ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='982bdc1e-36e5-4108-b7e3-97ae6b741259'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__portrait-with-bob-hair-and-pendant-collar-batch-086/20260929T135704Z-thuan-mac/reference/magneto_982bdc1e-36e5-4108-b7e3-97ae6b741259.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='portrait-with-bob-hair-and-pendant-collar-batch-086'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('portrait', 'with', 'bob', 'hair', 'and', 'pendant', 'collar', 'batch', '086')
    human_construction = "bust"
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

        path('bob',(9,27),[('L',(6,27)),('L',(6,24)),('A',(42,24),18,18,True),('L',(42,27)),('L',(39,27))])
        oval('face',24,22,7,7)
        path('shoulders',(6,42),[('A',(24,33),18,9,True),('A',(42,42),18,9,True)]);join('face','shoulders')
        line('pendant',(22,42),(26,42))
