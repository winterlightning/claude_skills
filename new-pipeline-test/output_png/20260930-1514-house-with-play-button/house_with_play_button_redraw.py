"""house-with-play-button (redraw of the new-pipeline traced SVG).

Subject: a house outline with a large hollow play triangle inside -- home video,
home media, "watch at home".

Plan: SQUARE, centerline box (6,6)-(42,42), mirrored about x=24 for the house.
- house: one gable roof run (6,14)-(24,6)-(42,14) (pitch 4:9) and one wall run
  (6,14)-(6,42)-(42,42)-(42,14) that shares both eave corners with the roof
  (declared connect), so the outline is a closed pentagon with round joins.
- play: one closed right-pointing triangle, left edge x=17 from y=18 to 34, tip
  (34,26). Its centroid (22.7,26) sits just left of the house axis, the usual
  optical centring of a play glyph.
Extremes: x 6/42 from the walls, y 6 from the roof apex and 42 from the floor.

Budget that decided the shape: the triangle needs 8 on centerlines from the
floor, both walls and both roof slopes, and a centerline inradius of 5 for a
6-wide hole at stroke 4. An exhaustive integer search over roof pitch, wall
position and triangle size showed no layout with eaves overhanging the walls
(the trace's roof stubs) or a roof steeper than about 1:2 reaches a 6-wide hole;
the best eave layout left a 5.3 hole. So the eave stubs were dropped (the
choice brief itself calls for "a single closed house outline") and the roof was
flattened to 4:9, which gives an inradius of 5.08 (hole 6.1).

Metric issues fixed:
- clearance e0/e2 (roof vs play, 7.27): the triangle's top vertex and upper
  edge now sit 8.0 or more from both roof slopes.
- clearance e1/e2 (floor vs play, 5.78): the triangle's bottom vertex is at
  y=34, exactly 8 above the floor; its tip is 8 from the right wall and its
  left edge 11 from the left wall.
- hole (play hole 5.0 wide): now 6.1 inscribed at stroke 4.
- stroke-width (info): redrawn at the profile stroke 4, and every gap above
  was budgeted at that width.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7e3b79f2-dcc5-4988-ab08-8460306de315"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1514-house-with-play-button/"
    "house-with-play-button_raw.svg"
)
AUTHOR = "claude-opus-5-5"

# House: apex on the axis, eave corners where the roof meets the walls.
AXIS, APEX_Y, EAVE_Y, WALL, FLOOR_Y = 24, 6, 14, 18, 42
# Play triangle: left edge x, top y, height, width (tip at mid-height).
PLAY_X, PLAY_TOP, PLAY_H, PLAY_W = 17, 18, 16, 17


class HouseWithPlayButtonRedraw(Solo48):
    icon_id = "house-with-play-button-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ("home video", "home media", "house play", "watch at home")
    keywords = ("house", "home", "play", "video", "media", "stream", "movie", "watch")

    def build(self) -> None:
        left, right = (AXIS - WALL, EAVE_Y), (AXIS + WALL, EAVE_Y)

        # -- house: gable roof + walls and floor, joined at the eaves -------
        self.add_polyline("roof", left, (AXIS, APEX_Y), right)
        self.add_polyline(
            "walls", left, (AXIS - WALL, FLOOR_Y), (AXIS + WALL, FLOOR_Y), right,
        )
        self.relate("connect", "walls", "roof")

        # -- play triangle ----------------------------------------------------
        self.add_polyline(
            "play",
            (PLAY_X, PLAY_TOP),
            (PLAY_X + PLAY_W, PLAY_TOP + PLAY_H // 2),
            (PLAY_X, PLAY_TOP + PLAY_H),
            closed=True,
        )
