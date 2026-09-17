"""A large open heart accompanied by a small upper-right heart. Lucide heart informs paired lobes and tapering sides; intentional open right lobe retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='6188e665-7838-43fa-b5c8-8aecfca95ea0'
SOURCE_PATH='pictographic-primitives/symbol/three hearts_6188e665-7838-43fa-b5c8-8aecfca95ea0.svg'
AUTHOR = 'gpt-6'

class HeartsTwo(Solo48):
    icon_id='hearts-two'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords = ('hearts', 'love', 'like', 'romance', 'valentine', 'favorite', 'affection', 'care', 'sub icon')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def raw(self,n,points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(n+'-'+str(j),a,b)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.add_arc('large-left-top',(22,24),(6,24),radius_x=8,sweep=False)
        self.add_arc('large-left-side',(6,24),(12,32),radius_x=12,sweep=False)
        self.raw('large-tip',[(12,32),(24,42),(34,32)])
        self.add_arc('large-right-side',(34,32),(36,28),radius_x=12,sweep=False)
        self.add_contour('large','large-left-top','large-left-side',*['large-tip-'+str(j) for j in (1,2)],'large-right-side')
        self.add_arc('small-left',(34,10),(26,10),radius_x=4,sweep=False)
        self.raw('small-bottom',[(26,10),(28,14),(34,20),(40,14),(42,10)])
        self.add_arc('small-right',(42,10),(34,10),radius_x=4,sweep=False)
        self.add_contour('small','small-left',*['small-bottom-'+str(j) for j in range(1,5)],'small-right',closed=True)


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('76a3aff2-7ce1-498f-ac39-f41016299ef6', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/heart and hook_76a3aff2-7ce1-498f-ac39-f41016299ef6.svg')]
