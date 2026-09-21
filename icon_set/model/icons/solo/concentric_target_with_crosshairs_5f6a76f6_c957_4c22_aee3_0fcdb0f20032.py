"""Precision Target Aiming Symbol.

Plan: Target radius20 with inner radius11 and center dot. Four cardinal ticks attach to middle ring. Reduce tiny central ring to a dot.
Construction reference: Lucide radio: concentric geometric construction
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f6a76f6-c957-4c22-aee3-0fcdb0f20032'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/center_5f6a76f6-c957-4c22-aee3-0fcdb0f20032.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'concentric-target-with-crosshairs'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('concentric', 'target', 'with', 'crosshairs')

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

        circle('outer',24,24,20)
        for name,a,b in [('top',(24,13),(35,24)),('right',(35,24),(24,35)),('bottom',(24,35),(13,24)),('left',(13,24),(24,13))]:
         self.add_arc(name,a,b,radius_x=11)
        self.add_contour('middle','top','right','bottom','left',closed=True)
        self.add_dot('center',(24,24))
        for name,a,b in [('north',(24,13),(24,16)),('east',(32,24),(35,24)),('south',(24,32),(24,35)),('west',(13,24),(16,24))]:
         line(name,a,b);join(name,'middle')
