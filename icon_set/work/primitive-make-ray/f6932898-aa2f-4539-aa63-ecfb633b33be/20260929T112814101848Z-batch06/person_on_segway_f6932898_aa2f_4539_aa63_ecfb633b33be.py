"""Rejected rider had an undersized head and rigid boxed torso. Enlarge head, curve the rider into the wheel, soften the handlebar and preserve two speed strokes. Omit smallest speed mark.
Symbol plan: human_ref/full_body_ref.png; circular head radius5, lower edge14, torso starts22: exact 4 ink gap.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f6932898-aa2f-4539-aa63-ecfb633b33be'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-on-segway/20260929T112503Z-thuan-mac/reference/segway person_f6932898-aa2f-4539-aa63-ecfb633b33be.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'person-on-segway'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'on', 'segway')

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

        circle('head',30,9,5)
        path('torso',(30,22),[('C',(28,30),(30,25),(29,28))])
        path('arm',(30,22),[('L',(36,22)),('A',(40,26),4,4,True),('L',(35,37))])
        circle('wheel',28,37,7)
        join('torso','arm');join('torso','wheel');join('arm','wheel')
        line('speed-top',(8,17),(18,17));line('speed-bottom',(8,25),(16,25))
        self.mark_human_figure('rider',head='head',torso='torso-0',torso_junction='start')
