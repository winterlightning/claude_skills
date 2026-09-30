"""Four solid lines lose the outlined bar-chart form. Restore three progressively shorter outlined bars beneath declining arrow.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No additional useful Lucide match; shared arrowhead construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ce30d25b-7e40-45e5-bb67-fb74f54f495f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__performance-decrease/20260929T135610Z-thuan-mac/reference/performance decrease_ce30d25b-7e40-45e5-bb67-fb74f54f495f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='performance-decrease'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('performance', 'decrease')
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

        line('baseline',(4,40),(44,40))
        for j,(x,top) in enumerate([(4,20),(20,28),(36,32)]):
         poly(f'bar{j}',(x,40),(x,top),(x+8,top),(x+8,40));join(f'bar{j}','baseline')
        line('trend',(6,8),(42,22));poly('arrow',(34,20),(42,22),(40,12));join('trend','arrow')
