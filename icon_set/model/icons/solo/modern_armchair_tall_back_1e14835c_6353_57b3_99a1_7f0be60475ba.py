"""Modern Comfortable Armchair.

Modern armchair with tall rounded back, deep curved arms, compact seat and splayed legs. Centerline extremes (8,4)-(40,44). Lucide armchair informs integrated arm/seat geometry; mirrored halves preserve balance. Simplify extra cushion piping.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e14835c-6353-57b3-99a1-7f0be60475ba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/armchair modern 1_1e14835c-6353-57b3-99a1-7f0be60475ba.svg'
AUTHOR = 'gpt-6'

class ModernArmchairTallBack(Solo48):
    icon_id = 'modern-armchair-tall-back'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('modern', 'comfortable', 'armchair')

    def build(self):
        # Symbol plan: Modern armchair with tall rounded back, deep curved arms, compact seat and splayed legs. Centerline extremes (8,4)-(40,44). Lucide armchair informs integrated arm/seat geometry; mirrored halves preserve balance. Simplify extra cushion piping.

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
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
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

        path('back',(16,22),[('L',(16,10)),('A',(22,4),6,6,True),('L',(26,4)),('A',(32,10),6,6,True),('L',(32,22))])
        path('frame',(16,28),[('L',(16,22)),('A',(8,22),4,4,False),('L',(8,32)),('A',(12,36),4,4,False),('L',(16,36)),('L',(32,36)),('L',(36,36)),('A',(40,32),4,4,False),('L',(40,22)),('A',(32,22),4,4,False),('L',(32,28)),('L',(16,28))],True);join('back','frame')
        for n,a,b in [('left',(16,36),(12,44)),('right',(32,36),(36,44))]:line(n,a,b);join(n,'frame')
