"""Segmented Insect Larva.

Plan: Retained the upward-curving larva and four body sections. Shared division endpoints preserve the curved silhouette without overlapping outlines.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68ca282c-1871-444e-a545-328fd1662da7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/maggot_68ca282c-1871-444e-a545-328fd1662da7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'segmented-larva-curving-upward'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('segmented', 'larva', 'curving', 'upward')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('larva',(4,32),[('A',(12,24),8,8,True),('L',(14,24)),('C',(25,21),(20,24),(22,23)),('L',(32,13)),('C',(38,8),(36,8),(36,8)),('C',(44,16),(44,8),(44,12)),('C',(40,22),(44,20),(42,21)),('L',(29,34)),('C',(14,40),(25,38),(20,40)),('L',(12,40)),('A',(4,32),8,8,True)],True)
        for name,a,b in [('a',(14,24),(14,40)),('b',(25,21),(29,34)),('c',(32,13),(40,22))]:line(name,a,b);join(name,'larva')
