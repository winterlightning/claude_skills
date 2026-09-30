"""The rejected indentation control replaces the two outlined rows with solid strokes. Restore two rounded outlined rows beneath a rightward arrow.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide list-indent-increase: separate directional chevron and aligned rows.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bc08c07e-fd43-4866-85c6-472f38121c0c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__right-indentation-action/20260929T141743Z-thuan-mac/reference/align right move_bc08c07e-fd43-4866-85c6-472f38121c0c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='right-indentation-action'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('right', 'indentation', 'action')
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

        box('upper-row',8,20,27,28,2);box('lower-row',16,36,27,44,2)
        line('shaft',(30,10),(40,10));poly('arrow',(34,4),(40,10),(34,16));join('arrow','shaft')
