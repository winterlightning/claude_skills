"""Stylized genie with domed turban/head, paired curled mustache edges, and a curling smoke body. VRECT_L fits the stacked silhouette. Omit jewel, wrap seams and facial detail. Shared human references informed the head/body relationship, but the ornate head silhouette remains a substantial reduction. Head bottom y20 and upper torso y28 give exactly8 centerline /4 ink gap; checker cannot certify mustache-left versus torso and returns review. Incomplete; never count this warning as a pass.

Symbol plan: VRECT_L; visible bounds (6, 2, 42, 46). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9d2a78b-2eb0-40a5-bcec-c567992dd9f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/genie_f9d2a78b-2eb0-40a5-bcec-c567992dd9f2.svg'
AUTHOR = 'gpt-6'

def _circle(icon, name, x, y, r):
    icon.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
    icon.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
    icon.add_contour(name,name+'-top',name+'-bottom',closed=True)

def _path(icon, name, start, commands, closed=False):
    members=[]; p=start
    for i,c in enumerate(commands):
        n=f'{name}-{i}'; q=c[1]
        if c[0]=='L': icon.add_line(n,p,q)
        else: icon.add_arc(n,p,q,radius_x=c[2],radius_y=c[3] if len(c)>3 else c[2],sweep=c[4] if len(c)>4 else True)
        p=q; members.append(n)
    icon.add_contour(name,*members,closed=closed)

class Batch051Icon(Solo48):
    icon_id = 'genie-with-turban-and-curling-body-batch-051'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('genie', 'turban', 'mustache', 'magic', 'spirit', 'tail', 'fantasy')

    def build(self):
        # Turban dome and curled mustache form one expressive head silhouette.
        # The separate smoke body begins at28: head bottom20 gives exact8 centerline gap.
        _path(self,'head',(14,20),[('L',(14,14)),('A',(34,14),10),('L',(34,20))])
        self.add_arc('mustache-left',(14,20),(24,20),radius_x=5)
        self.add_arc('mustache-right',(24,20),(34,20),radius_x=5)
        self.relate('connect','head','mustache-left')
        self.relate('connect','head','mustache-right')
        self.relate('connect','mustache-left','mustache-right')
        _path(self,'smoke',(8,34),[('A',(24,32),16,2),('A',(40,34),16,2),('A',(24,44),16,10),('L',(16,44))])
        self.add_line('torso',(24,28),(24,32))
        self.relate('connect','torso','smoke')
