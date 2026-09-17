"""pacman: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea992b74-1d7b-5d1a-9380-854e5151b7ed'
SOURCE_PATH = 'pictographic-primitives/video-games/pacman_ea992b74-1d7b-5d1a-9380-854e5151b7ed.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Pacman(Solo48):
    icon_id = 'pacman'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('pacman', 'video-games', 'sub icon')

    def build(self):
        # SQUARE (6,6)-(42,42) would distort this circle; use VRECT_L with an ellipse instead.
        # Construction reference: Lucide circle-check: coherent circle; source supplies the open wedge
        # VRECT_L (8,4)-(40,44); smooth body with a deliberate open mouth.
        self.add_bezier('upper-right',(40,14),((37,8),(31,4),(26,4)))
        self.add_arc('left-body',(26,4),(26,44),radius_x=18,radius_y=20,sweep=False)
        self.add_bezier('lower-right',(26,44),((31,44),(37,40),(40,34)))
        self.add_polyline('mouth',(40,34),(27,24),(40,14))
        self.add_contour('outline','upper-right','left-body','lower-right','mouth-1','mouth-2',closed=True)
        self.contours.pop(0)


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('d162e891-6c21-47e5-ab18-e1fc863c5dc5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-08/pacman_d162e891-6c21-47e5-ab18-e1fc863c5dc5.svg')]
