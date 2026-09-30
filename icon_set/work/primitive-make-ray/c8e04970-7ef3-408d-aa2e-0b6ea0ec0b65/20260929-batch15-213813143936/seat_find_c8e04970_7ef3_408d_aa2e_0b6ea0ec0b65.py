"""The rejected scene uses a stiff frontal figure and an angular chair. Restore a walking step, a forward arm and a smoothly rounded seat corner while retaining the direction arrow.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/full_body_ref.png: round head and coherent limbs; Lucide armchair: rounded seat junctions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c8e04970-7ef3-408d-aa2e-0b6ea0ec0b65'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__seat-find/20260929T141805Z-thuan-mac/reference/seat find_c8e04970-7ef3-408d-aa2e-0b6ea0ec0b65.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='seat-find'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('seat', 'find')
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

        oval('head',14,10,4,4)
        line('torso',(14,22),(14,32));poly('arms',(8,28),(14,22),(20,28));join('torso','arms')
        poly('legs',(6,42),(14,32),(20,35),(22,42));join('torso','legs')
        self.mark_human_figure('walker',head='head',torso='torso',torso_junction='start')
        line('shaft',(23,18),(30,18));poly('arrow',(26,14),(30,18),(26,22));join('shaft','arrow')
        path('chair',(40,12),[('L',(42,20)),('L',(40,30)),('C',(36,34),(40,33),(39,34)),('L',(30,34))])
        line('base',(30,42),(40,42))
