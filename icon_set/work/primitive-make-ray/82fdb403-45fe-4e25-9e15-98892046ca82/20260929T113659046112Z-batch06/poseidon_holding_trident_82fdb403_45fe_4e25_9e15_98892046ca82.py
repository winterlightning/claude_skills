"""Rejected Poseidon had tiny head, rigid triangular robe and angular trident. Restore larger head, a draped open robe and rounded trident prongs. Omit cramped crown band and robe fold.
Symbol plan: human_ref/full_body_ref.png; radius5 head and neck24 give exact4 ink gap.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '82fdb403-45fe-4e25-9e15-98892046ca82'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__poseidon-holding-trident/20260929T112503Z-thuan-mac/reference/poseidon_82fdb403-45fe-4e25-9e15-98892046ca82.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'poseidon-holding-trident'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('poseidon', 'holding', 'trident')

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

        circle('head',12,11,5)
        line('torso',(12,24),(12,26))
        path('robe',(12,26),[('C',(6,42),(10,30),(6,38)),('L',(24,42))]);join('torso','robe')
        poly('arm',(12,24),(24,30),(34,30));join('arm','torso')
        path('trident',(26,6),[('L',(26,14)),('A',(34,22),8,8,False),('A',(42,14),8,8,False),('L',(42,6))])
        poly('shaft',(34,6),(34,22),(34,30),(34,42));join('shaft','trident');join('shaft','arm')
        self.mark_human_figure('poseidon',head='head',torso='torso',torso_junction='start')
