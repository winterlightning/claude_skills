"""Poster with Picture and Text.

Plan: Poster bounds10,4,38,44 with blank picture square and one text line. Omit the second line to protect lower margin; abstract layout marks are not typeface characters.
Construction reference: Lucide briefcase: rounded outer contour; source page layout
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c88bbee-f426-473e-938c-923d813a4e83'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/poster_7c88bbee-f426-473e-938c-923d813a4e83.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'poster-with-picture-placeholder'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('poster', 'with', 'picture', 'placeholder')

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

        rect('page',10,4,28,40,4)
        poly('picture',(19,13),(29,13),(29,23),(19,23),closed=True)
        line('caption',(19,34),(29,34))
