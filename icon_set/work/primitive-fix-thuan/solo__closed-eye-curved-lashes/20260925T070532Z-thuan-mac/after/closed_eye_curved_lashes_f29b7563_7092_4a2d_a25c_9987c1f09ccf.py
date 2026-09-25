"""Shallower graceful eyelid with five fanned lashes and exact shared attachment nodes.
Plan: coherent named contours and repeated dimensions. HRECT_M natural subject envelope.
Construction reference: Lucide eye-closed: broad continuous lid and radial lashes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f29b7563-7092-4a2d-a25c-9987c1f09ccf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__closed-eye-curved-lashes/20260925T070532Z-thuan-mac/reference/lashes_f29b7563-7092-4a2d-a25c-9987c1f09ccf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Use a naturally shallow eyelid envelope with ink y=11..37 instead of stretching it to y=8..40. Five evenly fanned lashes and continuous lid read clearly at 48px.', 'approved_by': 'user-delegated-to-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '58191e32de407a4d2f041f41a49c5e4db667ed8a72e9d17e8fe356af8f77bf23'}
    icon_id = 'closed-eye-curved-lashes'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('lashes',)

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

        # Eye remains naturally shallow; exact named cubic endpoints own all five lashes.
        path('lid',(4,13),[('C',(9,19),(6,16),(7,17)),('C',(16,23),(11,21),(13,22)),('C',(24,25),(19,24),(21,25)),('C',(32,23),(27,25),(29,24)),('C',(39,19),(35,22),(37,21)),('C',(44,13),(41,17),(42,16))])
        for j,(a,b) in enumerate([((9,19),(4,24)),((16,23),(12,32)),((24,25),(24,35)),((32,23),(36,32)),((39,19),(44,24))]):
            line(f'lash-{j}',a,b);join('lid',f'lash-{j}')
