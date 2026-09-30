"""The rejected tactile paving became two uninterrupted bars. Restore three separate dashed paving tracks and a bent-arm walking pose.
Symbol plan: human_ref/full_body_ref.png: outlined head, articulated limbs, head outline14 to torso22 gives exact4 ink gap. Two dashed tracks retain tactile paving.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ba6234d6-f75b-454d-b652-1944239a63bc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walker-beside-tactile-paving/20260929T122443Z-thuan-mac/reference/blind walk path_ba6234d6-f75b-454d-b652-1944239a63bc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'walker-beside-tactile-paving'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('walker', 'beside', 'tactile', 'paving')

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

        circle('head',31,10,4)
        line('torso',(31,22),(31,32))
        poly('arms',(25,27),(31,22),(38,26),(42,26));join('arms','torso')
        poly('legs',(25,42),(31,32),(40,42));join('legs','torso')
        self.mark_human_figure('walker',head='head',torso='torso',torso_junction='start')
        for x in (6,14):
         for j,y in enumerate((6,22,38)):line(f'paving-{x}-{j}',(x,y),(x,y+4))
