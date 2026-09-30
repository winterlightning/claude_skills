"""The rejected bob is an open hair arch and its pendant is just a detached dot. Restore flat bob ends and a prominent pointed pendant attached to the collar.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular jaw and rounded shoulder arch; touching bust ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='982bdc1e-36e5-4108-b7e3-97ae6b741259'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__portrait-with-bob-hair-and-pendant-collar-batch-086/20260929T135704Z-thuan-mac/reference/magneto_982bdc1e-36e5-4108-b7e3-97ae6b741259.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='portrait-with-bob-hair-and-pendant-collar-batch-086'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('portrait', 'with', 'bob', 'hair', 'and', 'pendant', 'collar', 'batch', '086')
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

        path('bob',(15,28),[('L',(8,28)),('L',(8,20)),('A',(40,20),16,16,True),('L',(40,28)),('L',(33,28))])
        oval('face',24,20,7,7)
        path('shoulders',(8,40),[('A',(24,31),16,9,True),('A',(40,40),16,9,True)]);join('face','shoulders')
        poly('pendant',(24,31),(20,39),(24,44),(28,39),(24,31));join('pendant','shoulders')
