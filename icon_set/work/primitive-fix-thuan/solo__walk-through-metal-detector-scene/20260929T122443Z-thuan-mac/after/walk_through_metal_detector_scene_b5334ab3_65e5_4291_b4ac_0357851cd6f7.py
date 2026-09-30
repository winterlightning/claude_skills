"""The rejected metal detector reduced the person to a ring over a cup. Restore a complete standing person with shoulders, torso and two legs inside a smooth portal. Omit the small top control and beep rays to give the person enough room.
Symbol plan: human_ref/full_body_ref.png: complete stick figure and circular head; head bottom22 to shoulder30 gives exact4 ink gap.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b5334ab3-65e5-4291-b4ac-0357851cd6f7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walk-through-metal-detector-scene/20260929T122443Z-thuan-mac/reference/security officer scanner beep_b5334ab3-65e5-4291-b4ac-0357851cd6f7.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'walk-through-metal-detector-scene'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('walk', 'through', 'metal', 'detector', 'scene')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        line('wall-left',(8,44),(8,10));line('wall-right',(40,10),(40,44))
        path('arch',(8,10),[('A',(14,4),6,6,True),('L',(34,4)),('A',(40,10),6,6,True)])
        join('arch','wall-left');join('arch','wall-right')
        circle('head',24,18,4)
        line('torso',(24,30),(24,38))
        poly('arms',(16,30),(24,30),(32,30));join('torso','arms')
        poly('legs',(18,44),(24,38),(30,44));join('torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
