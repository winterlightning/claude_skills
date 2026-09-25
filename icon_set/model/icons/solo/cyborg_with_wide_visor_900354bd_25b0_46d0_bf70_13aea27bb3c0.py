'A front-facing cyborg wears a broad horizontal visor across the upper half of a rounded head. A small downturned mouth sits above a short neck, broad shoulders and a central suit seam.\nPlan: Wide visor helmet, circular jaw, curved shoulders. Jaw bottom30, shoulder top34 gives zero ink gap. Extrema6,6,42,42. Omit tiny frown/seam.\nConstruction reference: human_ref/user.svg: circular jaw and broad curved shoulders; wide visor from original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '900354bd-25b0-46d0-bf70-13aea27bb3c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-09/robocop_900354bd-25b0-46d0-bf70-13aea27bb3c0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cyborg-with-wide-visor'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('cyborg', 'with', 'wide', 'visor')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

        path('visor',(14,6),[('L',(34,6)),('A',(38,10),4,4,True),('L',(38,16)),('A',(34,20),4,4,True),('L',(14,20)),('A',(10,16),4,4,True),('L',(10,10)),('A',(14,6),4,4,True)],True)
        self.add_arc('jaw',(14,20),(34,20),radius_x=10,radius_y=10,sweep=False);join('visor','jaw')
        self.add_arc('body-top',(6,42),(42,42),radius_x=18,radius_y=8,sweep=True);self.add_contour('body','body-top');join('jaw','body')
