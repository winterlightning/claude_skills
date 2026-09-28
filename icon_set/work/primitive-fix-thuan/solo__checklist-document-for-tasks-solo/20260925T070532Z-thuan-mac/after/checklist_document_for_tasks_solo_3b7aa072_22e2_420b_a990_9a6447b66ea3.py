"""Restore rounded document, square checkbox rows and visible horizontal text strokes.
Plan: coherent named contours and repeated dimensions. VRECT_L natural subject envelope.
Construction reference: Lucide mail rounded enclosure; repeated checklist rows from source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3b7aa072-22e2-420b-a990-9a6447b66ea3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__checklist-document-for-tasks-solo/20260925T070532Z-thuan-mac/reference/task list_3b7aa072-22e2-420b-a990-9a6447b66ea3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Allow 3px ink clearances between checkbox, page and text strokes. Both square openings are 4px wide; paired rows remain clearly separated and legible at 48px.', 'approved_by': 'user-delegated-to-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '09cf0eb1e212d42085704abd0d689c70e4a574d23ee24bee48ddb19b2a1cebc5'}
    icon_id = 'checklist-document-for-tasks-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('task', 'list')

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

        box('page',8,4,40,44,3)
        for y in (16,32):
            poly(f'box-{y}',(15,y-4),(23,y-4),(23,y+4),(15,y+4),closed=True)
            line(f'text-{y}',(30,y),(33,y))
