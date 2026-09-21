"""Fax Machine with Paper.

Plan: Fax with left handset and projecting folded paper. Bounds6,6,42,42; blank paper and body replace tiny text and keypad.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ccbc89d-f370-4d34-8f44-d0cfa8369fa7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/answer machine paper_4ccbc89d-f370-4d34-8f44-d0cfa8369fa7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fax-machine-with-upright-paper'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('fax', 'machine', 'with', 'upright', 'paper')

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

        poly('base',(18,24),(42,24),(42,42),(18,42),(6,42),(6,24),closed=True)
        poly('handset',(6,24),(6,16),(18,16),(18,24),(18,42));join('base','handset')
        poly('paper',(26,24),(26,6),(34,6),(42,14),(42,24));join('paper','base')
