"""Restore gently sloping seat back, raised front lip and fine runner supports.
Plan: coherent named contours and repeated dimensions. HRECT_L natural subject envelope.
Construction reference: No useful exact Lucide match; smooth coherent sleigh contours.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '002679b5-86e3-4c02-8bd6-d8930f4e6d89'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__christmas-sleigh/20260925T070532Z-thuan-mac/reference/sled_002679b5-86e3-4c02-8bd6-d8930f4e6d89.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'christmas-sleigh'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('sled',)

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('body',(4,8),[('L',(17,10)),('C',(21,18),(21,10),(21,13)),('L',(21,20)),('L',(30,20)),('C',(39,16),(32,17),(35,16)),('L',(39,28)),('L',(12,28)),('A',(4,20),8,8,True),('L',(4,8))],True)
        path('runner',(4,40),[('L',(34,40)),('A',(44,30),10,10,False)])
        for name,a,b in [('rear',(16,28),(10,40)),('front',(28,28),(34,40))]:
            line(name,a,b);join(name,'body');join(name,'runner')
