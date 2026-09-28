"""Smooth horse neck, distinct muzzle and ear, wider stable pedestal.
Plan: coherent named contours and repeated dimensions. VRECT_L natural subject envelope.
Construction reference: No useful exact Lucide match; coherent horse contour.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '48042cfb-02f3-5fbd-b3d2-694663a8c5e3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chess-knight-piece-batch-019-15/20260925T070532Z-thuan-mac/reference/strategy chess_48042cfb-02f3-5fbd-b3d2-694663a8c5e3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Retain the horse muzzle undercut and curved neck: the short local opening remains visible at 48px in both themes; broad neck and pedestal preserve recognition.', 'approved_by': 'user-delegated-to-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '49132699ef62afbf11d58d589047d0fcb1f67b8f59614239992b21b1b430e678'}
    icon_id = 'chess-knight-piece-batch-019-15'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('strategy', 'chess')

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

        path('horse',(12,34),[('C',(22,21),(12,28),(23,27)),('L',(15,23)),('C',(8,20),(11,26),(8,23)),('C',(13,13),(8,18),(11,15)),('L',(20,7)),('L',(20,4)),('C',(36,17),(29,7),(36,12)),('C',(34,34),(38,23),(34,29))])
        box('base',8,34,40,44,3)
        join('horse','base')
