"""The rejected detector omitted the beep rays and reduced the person to a head over a tiny cup. Restore a recognisable central standing figure and side sound marks in an open portal.
Symbol plan: human_ref/full_body_ref.png: round outlined head and minimal body; head bottom22 to torso30 exact4 ink gap.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b5334ab3-65e5-4291-b4ac-0357851cd6f7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walk-through-metal-detector-scene/20260929T122443Z-thuan-mac/reference/security officer scanner beep_b5334ab3-65e5-4291-b4ac-0357851cd6f7.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'walk-through-metal-detector-scene'
    keyshape = Keyshape.SQUARE
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

        path('portal',(14,42),[('L',(14,10)),('A',(18,6),4,4,True),('L',(30,6)),('A',(34,10),4,4,True),('L',(34,42))])
        circle('head',24,19,3)
        line('torso',(24,30),(24,34))
        poly('legs',(23,42),(24,34),(25,42));join('torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        for x in (6,42):
         line(f'beep-{x}',(x,22),(x,28))
