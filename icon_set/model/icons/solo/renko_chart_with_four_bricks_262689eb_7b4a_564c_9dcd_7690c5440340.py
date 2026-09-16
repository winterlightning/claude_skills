"""Renko Chart with Four Bricks.

Symbol plan: Four equal open bricks arranged in a staggered fall-and-rise chart. Shared brick dimensions retain the source pattern with wider spacing.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: No exact Lucide Renko match; repeated chart symbols follow the same common-dimension principle as Lucide chart-no-axes-combined inspected earlier.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '262689eb-7b4a-564c-9dcd-7690c5440340'
SOURCE_PATH = 'pictographic-primitives/business/renko chart_262689eb-7b4a-564c-9dcd-7690c5440340.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'renko-chart-with-four-bricks'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('renko', 'chart', 'graph', 'data', 'analytics', 'trend', 'statistics', 'finance', 'comparison')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def box(n,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w//2,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+w//2,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            curves={2,4,7,9}
            for j in range(10):
                a,b=pts[j],pts[(j+1)%10]
                if a==b: continue
                if j in curves: arc(n+str(j),a,b,r)
                else: line(n+str(j),a,b)
            join(n,*(n+str(j) for j in range(10) if pts[j]!=pts[(j+1)%10]),closed=True)


        for j,(x,y) in enumerate(((6,18),(16,34),(32,22),(34,6))):box('brick-'+str(j),x,y,8,8,1)
