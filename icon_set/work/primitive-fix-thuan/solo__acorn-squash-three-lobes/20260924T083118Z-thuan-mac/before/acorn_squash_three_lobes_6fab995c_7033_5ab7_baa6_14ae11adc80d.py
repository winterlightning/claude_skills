"""Whole Acorn Squash.

Three-lobed acorn squash with two mirrored ribs and a short curved stem. Centerline extremes (6,6)-(42,42). Lucide apple informs the fruit/stem attachment; simplify the rib ends to detached strokes so all three bands remain clear.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6fab995c-7033-5ab7-baa6-14ae11adc80d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/acornsquash_6fab995c-7033-5ab7-baa6-14ae11adc80d.svg'
AUTHOR = 'gpt-6'

class AcornSquashThreeLobes(Solo48):
    icon_id = 'acorn-squash-three-lobes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('whole', 'acorn', 'squash')

    def build(self):
        # Symbol plan: Three-lobed acorn squash with two mirrored ribs and a short curved stem. Centerline extremes (6,6)-(42,42). Lucide apple informs the fruit/stem attachment; simplify the rib ends to detached strokes so all three bands remain clear.

        def path(name, start, commands, closed=False):
            members=[]
            for i, command in enumerate(commands):
                kind,end,*args=command
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,start,end)
                elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
                members.append(member)
                start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def bilateral(name, start, right, closed=True):
            # One half owns geometry; mirror and reverse it about the shared axis.
            axis=24
            mirror=lambda p:(2*axis-p[0],p[1])
            segments=[]
            here=start
            for kind,end,*args in right:
                segments.append((kind,here,end,args));here=end
            left=[]
            for kind,begin,end,args in reversed(segments):
                if kind=='C': left.append((kind,mirror(begin),mirror(args[1]),mirror(args[0])))
                elif kind=='A': left.append((kind,mirror(begin),*args))
                else:left.append((kind,mirror(begin)))
            if closed:path(name,start,right+left,True)
            else:path(name,mirror(here),left+right)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        bilateral('body',(24,12),[('A',(42,27),18,15,True),('A',(24,42),18,15,True)])
        path('stem',(24,12),[('C',(28,6),(24,8),(25,6))]);join('stem','body')
        for side in (-1,1):
            x=24+side*5
            path(f'rib-{side}',(x,22),[('C',(x,32),(24+side*8,24),(24+side*8,30))])
