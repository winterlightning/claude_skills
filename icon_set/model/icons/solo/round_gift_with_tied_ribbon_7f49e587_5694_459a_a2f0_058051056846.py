"""Replaced the tangled bow with mirrored open lobes and regularized its ribbon junctions.
Symbol plan: Round gift with horizontal and vertical ribbon and mirrored broad bow loops. Lucide gift informs matched bow lobes, avoiding overlapped knotted strokes.
Final reduction: Fine ribbon tails and upper vertical ribbon section omitted to preserve bow openings.
References: Lucide gift original and atomic-debug: matching bow lobes.
Keyshape reason: Circular gift.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7f49e587-5694-459a-a2f0-058051056846'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/39-7f49e587-5694-459a-a2f0-058051056846.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='round-gift-with-tied-ribbon'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('round', 'gift', 'with', 'tied', 'ribbon')
    def build(self):

        def path(n,start,steps,closed=False):
            p=start; members=[]
            for i,step in enumerate(steps):
                m=f"{n}-{i}"
                if len(step)==2:
                    self.add_line(m,p,step);p=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(m,p,end,radius_x=rx,radius_y=ry,sweep=sweep);p=end
                members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[((x,y-r),r,r,True),((x+r,y),r,r,True),((x,y+r),r,r,True),((x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        circle('box',24,24,20)
        poly('ribbon-h',(4,24),(24,24),(44,24));poly('ribbon-v',(24,24),(24,44));join('ribbon-h','box');join('ribbon-v','box');join('ribbon-h','ribbon-v')
        path('bow-left',(24,24),[(16,22),((16,12),5,5,True),((24,20),8,8,True),(24,24)],True)
        path('bow-right',(24,24),[(24,20),((32,12),8,8,True),((32,22),5,5,True),(24,24)],True)
        for a in ['bow-left','bow-right']:
         join(a,'ribbon-h');join(a,'ribbon-v')
        join('bow-left','bow-right')
