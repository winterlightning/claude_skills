"""Horned dragon: rejected head is a long rectangle and the body an open squiggle. Restore a rounded snout and coherent S-curve through the curled body. Restore rounded snout and a smooth open S body with two distinct horns.
Symbol plan: Original horned dragon; rounded muzzle and coherent S curve. Tail interior outline omitted for spacing.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '740f43e8-d537-4ec2-bbd4-d4ce268b541b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curled-dragon-with-two-small-horns/20260929T115456Z-thuan-mac/reference/dragon_740f43e8-d537-4ec2-bbd4-d4ce268b541b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'curled-dragon-with-two-small-horns'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('curled', 'dragon', 'with', 'two', 'small', 'horns')

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

        path('head',(18,10),[('C',(27,12),(22,9),(25,10)),('L',(37,12)),('A',(37,22),5,5,True),('L',(22,22)),('C',(18,10),(10,22),(10,10))],True)
        path('body',(22,22),[('C',(36,34),(22,27),(36,28)),('C',(24,42),(36,40),(30,42)),('C',(6,34),(14,42),(6,42)),('C',(10,25),(6,29),(11,28))]);join('head','body')
        line('horn-left',(18,10),(12,6));line('horn-right',(27,12),(27,6));join('horn-left','head');join('horn-right','head')
