"""Gentleman with Monocle.

Plan: Circular portrait with monocle, swept hair and tie. Bounds8,4,40,44. Jaw bottom30 shoulders34 touch in ink.
Construction reference: human_ref/user.svg.
Final review: Circular jaw radius14 centered24,18; jaw bottom32 and shoulder top36 give zero ink gap. Single eyeglass and temple retained; omitted swept hair and collar points.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d953f5b-fcd9-41c4-b7e4-d3f5f0027730'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/snob_4d953f5b-fcd9-41c4-b7e4-d3f5f0027730.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-with-monocle-and-necktie'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ()
    keywords = ('person', 'with', 'monocle', 'and', 'necktie')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        self.add_arc('jaw',(10,18),(38,18),radius_x=14,radius_y=14,sweep=False)
        self.add_arc('forehead',(38,18),(10,18),radius_x=14,radius_y=14,sweep=False)
        self.add_contour('face','jaw','forehead',closed=True)
        self.add_arc('body-left',(8,44),(16,36),radius_x=8,radius_y=8,sweep=True)
        self.add_line('body-top',(16,36),(24,36));self.add_line('body-top-right',(24,36),(32,36))
        self.add_arc('body-right',(32,36),(40,44),radius_x=8,radius_y=8,sweep=True)
        self.add_contour('shoulders','body-left','body-top','body-top-right','body-right');join('face','shoulders')
        circle('monocle',26,18,3)
        line('temple',(29,18),(38,18));join('temple','monocle');join('temple','face')
        line('tie',(24,36),(24,44));join('tie','shoulders')
