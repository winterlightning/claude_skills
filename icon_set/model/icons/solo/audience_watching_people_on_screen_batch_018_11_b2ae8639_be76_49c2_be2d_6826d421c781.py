from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2ae8639-be76-49c2-be2d-6826d421c781'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/movies/movies audience_b2ae8639-be76-49c2-be2d-6826d421c781.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/movies audience_b2ae8639-be76-49c2-be2d-6826d421c781.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/11-audience-watching-cinema-screen--b2ae8639-be76-49c2-be2d-6826d421c781.md'
DESIGN_PLAN = 'One small screen bust and two foreground viewers; each detached head has exactly 8 centerline units to its shoulder apex.'
DESIGN_NOTES = ['Five people reduced to three: one on-screen bust and two foreground viewers. The audience-watching-people-on-screen relationship is preserved. Head/shoulder ink gap is exactly 4 units for all three figures.']
CONSTRUCTION_REFERENCE = 'Human construction: icon_set/references/human_ref/user.svg; circular heads and open shoulder arcs.'

class BatchIcon(Solo48):
    icon_id = 'audience-watching-people-on-screen-batch-018-11'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "movies"
    keywords = ('audience', 'screen', 'cinema', 'viewers', 'people', 'movie', 'theater', 'group')

    def build(self):
        # One small screen bust and two foreground viewers; each detached head has exactly 8 centerline units to its shoulder apex.
        self.add_polyline('screen', (8, 24), (8, 4), (40, 4), (40, 24), closed=False)
        self.add_arc('screen-head-0', (22, 15), (24, 13), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('screen-head-1', (24, 13), (26, 15), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('screen-head-2', (26, 15), (24, 17), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('screen-head-3', (24, 17), (22, 15), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('screen-head', 'screen-head-0', 'screen-head-1', 'screen-head-2', 'screen-head-3', closed=True)
        self.add_arc('screen-shoulders', (21, 26), (27, 26), radius_x=3, radius_y=1, sweep=True, large_arc=False)
        self.add_arc('viewer-13-head-0', (11, 33), (13, 31), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('viewer-13-head-1', (13, 31), (15, 33), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('viewer-13-head-2', (15, 33), (13, 35), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('viewer-13-head-3', (13, 35), (11, 33), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('viewer-13-head', 'viewer-13-head-0', 'viewer-13-head-1', 'viewer-13-head-2', 'viewer-13-head-3', closed=True)
        self.add_arc('viewer-13-shoulders', (8, 44), (18, 44), radius_x=5, radius_y=1, sweep=True, large_arc=False)
        self.add_arc('viewer-35-head-0', (33, 33), (35, 31), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('viewer-35-head-1', (35, 31), (37, 33), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('viewer-35-head-2', (37, 33), (35, 35), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('viewer-35-head-3', (35, 35), (33, 33), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('viewer-35-head', 'viewer-35-head-0', 'viewer-35-head-1', 'viewer-35-head-2', 'viewer-35-head-3', closed=True)
        self.add_arc('viewer-35-shoulders', (30, 44), (40, 44), radius_x=5, radius_y=1, sweep=True, large_arc=False)
