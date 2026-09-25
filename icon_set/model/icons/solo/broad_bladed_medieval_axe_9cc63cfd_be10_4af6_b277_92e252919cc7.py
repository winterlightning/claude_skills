"""Diagonal axe with a broad crescent blade and shared mounting nodes; extremes 6,6,42,42.
Construction: axe: convex blade and distinct handle attachment
Reduction: Handle reduced to one stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9cc63cfd-be10-4af6-b277-92e252919cc7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fantasy medieval excutioner axe_9cc63cfd-be10-4af6-b277-92e252919cc7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broad-bladed-medieval-axe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('broad', 'bladed', 'medieval', 'axe')
    def build(self):

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                else: self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m); here=end
            self.add_contour(name,*members,closed=closed)
        def poly(name,*pts,closed=False): self.add_polyline(name,*pts,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        poly('handle',(6,42),(24,24),(32,16))
        path('blade',(24,24),[('L',(18,18)),('L',(30,6)),('A',(42,18),12,12,False),('A',(26,38),16,20,True),('A',(24,24),12,16,False)])
        join('blade','handle')
