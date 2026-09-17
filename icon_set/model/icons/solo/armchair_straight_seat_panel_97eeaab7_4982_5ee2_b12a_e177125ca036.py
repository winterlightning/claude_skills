"""Comfortable Living Room Armchair.

Armchair with straight armrests, a flat seat panel and slim angled legs. Centerline extremes (6,6)-(42,42). Lucide armchair informs shared back/frame endpoints; deliberate square arm corners distinguish this source. No extra upholstery detail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97eeaab7-4982-5ee2-b12a-e177125ca036'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/armchair_97eeaab7-4982-5ee2-b12a-e177125ca036.svg'
AUTHOR = 'gpt-6'

class ArmchairStraightSeatPanel(Solo48):
    icon_id = 'armchair-straight-seat-panel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('comfortable', 'living', 'room', 'armchair')

    def build(self):
        # Symbol plan: Armchair with straight armrests, a flat seat panel and slim angled legs. Centerline extremes (6,6)-(42,42). Lucide armchair informs shared back/frame endpoints; deliberate square arm corners distinguish this source. No extra upholstery detail.

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

        back_radius=6;arm_y=20;seat_y=28;bottom=36;inner=16 if False else 14;other=48-inner
        path('back',(inner,arm_y),[('L',(inner,6+back_radius)),('A',(inner+back_radius,6),back_radius,back_radius,True),('L',(other-back_radius,6)),('A',(other,6+back_radius),back_radius,back_radius,True),('L',(other,arm_y))])
        if True:
            left=[('L',(inner,arm_y)),('L',(6,arm_y)),('L',(6,bottom-4)),('A',(10,bottom),4,4,False)]
        elif False:
            left=[('L',(inner,arm_y)),('C',(6,arm_y),(inner,arm_y-6),(6,arm_y-6)),('L',(8,bottom-4)),('C',(12,bottom),(8,bottom-1),(9,bottom))]
        else:
            left=[('L',(inner,arm_y)),('A',(6,arm_y),4,4,False),('L',(6,bottom-4)),('A',(10,bottom),4,4,False)]
        # Reflect the arm run, reversing direction for the other side.
        segments=[];here=(inner,seat_y)
        for kind,end,*args in left:segments.append((kind,here,end,args));here=end
        mirror=lambda p:(48-p[0],p[1]);right=[]
        for kind,start,end,args in reversed(segments):
            if kind=='C':right.append((kind,mirror(start),mirror(args[1]),mirror(args[0])))
            elif kind=='A':right.append((kind,mirror(start),*args))
            else:right.append((kind,mirror(start)))
        base=[('L',(18,bottom)),('L',(30,bottom)),('L',(mirror(here)[0],bottom))]
        path('frame',(inner,seat_y),left+base+right)
        if False:path('seat',(inner,seat_y),[('C',(other,seat_y),(18,seat_y-2),(30,seat_y-2))])
        else:line('seat',(inner,seat_y),(other,seat_y))
        join('seat','frame');join('back','frame')
        if 'slant'=='block':
            for n,a,z in [('left',10,18),('right',30,38)]:
                self.add_polyline(n+'-foot',(a,bottom),(a,42),(z,42),(z,bottom));join(n+'-foot','frame')
        else:
            for n,x,z in [('left',18,16 if 'slant'=='slant' else 18),('right',30,32 if 'slant'=='slant' else 30)]:
                line(n+'-leg',(x,bottom),(z,42));join(n+'-leg','frame')
