"""Restore separate chisel blade and handle above a flowing carved wood surface.
Plan: coherent named contours and repeated dimensions. SQUARE natural subject envelope.
Construction reference: No exact Lucide match; rounded tool grip and coherent wood contour.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '93d527dc-470b-58d5-8ae9-b6db1ca51be0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chisel-carving-wood/20260925T070532Z-thuan-mac/reference/wood carving_93d527dc-470b-58d5-8ae9-b6db1ca51be0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Allow the wood base to reach y=47 ink inside the 48px canvas, preserving a readable separate chisel blade, handle and wood grain recess. All spacing checks pass.', 'approved_by': 'user-delegated-to-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'c37355279459781ae263a0020d4b45581150e05fa62b9722d6101a794a6bd0c1'}
    icon_id = 'chisel-carving-wood'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('wood', 'carving')

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


        path('handle',(28,14),[('L',(36,6)),('C',(42,12),(40,6),(42,8)),('L',(34,20)),('L',(28,14))],True)
        line('tang',(24,18),(28,14));join('tang','handle')
        path('blade',(24,18),[('L',(16,26)),('A',(10,20),5,5,True),('L',(18,12)),('L',(24,18))],True)
        join('blade','tang')
        path('wood',(6,35),[('L',(14,35)),('C',(24,37),(18,35),(19,37)),('C',(36,32),(29,37),(30,32)),('L',(42,32)),('L',(42,45)),('L',(6,45)),('L',(6,35))],True)
