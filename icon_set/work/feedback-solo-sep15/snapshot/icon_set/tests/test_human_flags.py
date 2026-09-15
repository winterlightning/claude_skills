"""Detached human metadata pairs real parts without changing their geometry."""
import json
from pathlib import Path
import unittest

from icon_set.model.icons.base import Icon
from icon_set.model.icons.combined import CombinedIcon
from icon_set.model.keyshapes import Keyshape
from icon_set.model.primitives import Position
from icon_set.model.profiles import Profile


def figure():
    icon = Icon("person", Profile.SOLO48, semantic_role="MAIN", keyshape=Keyshape.SQUARE)
    icon.add_arc("head-top", (20, 10), (28, 10), radius_x=4)
    icon.add_arc("head-bottom", (28, 10), (20, 10), radius_x=4)
    icon.add_contour("head", "head-top", "head-bottom", closed=True)
    icon.add_line("torso", (24, 22), (24, 32))
    return icon


class HumanFlagTests(unittest.TestCase):
    def test_flags_export_without_changing_ink_or_contact(self):
        icon = figure()
        before = icon.to_svg()
        icon.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.assertEqual(icon.to_svg(), before)
        self.assertEqual(icon.draw().relationships, ())
        flags = icon.to_record()["human_figures"]
        self.assertEqual(flags, [{"figure_id": "person", "head": "head", "torso": "torso",
                                 "torso_junction": "start", "centerline_gap": 8, "ink_gap": 4}])
        self.assertEqual(icon.draw().human_figures[0].head, "head")
        try:
            import jsonschema
        except ImportError:
            return
        schema = json.loads((Path(__file__).resolve().parents[1] / "schemas/icon-record.schema.json").read_text())
        jsonschema.validate(flags, schema["properties"]["human_figures"])

    def test_invalid_part_references_and_duplicate_ids_are_rejected(self):
        for head, torso, junction in (("missing", "torso", "start"),
                                     ("head", "missing", "start"),
                                     ("head", "head-bottom", "start"),
                                     ("torso", "torso", "start"),
                                     ("head", "torso", "middle")):
            with self.subTest(head=head, torso=torso, junction=junction), self.assertRaises(ValueError):
                figure().mark_human_figure("person", head=head, torso=torso, torso_junction=junction)
        icon = figure()
        icon.mark_human_figure("person", head="head", torso="torso", torso_junction="end")
        with self.assertRaises(ValueError):
            icon.mark_human_figure("person", head="head", torso="torso", torso_junction="start")

    def test_composed_people_keep_separate_pairings(self):
        person = figure()
        person.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        scene = CombinedIcon("people", "SIDE_COMBINE", Keyshape.SQUARE,
                             icons=[person, person], positions=[Position(0, 0), Position(10, 5)])
        drawing = scene.draw()
        self.assertEqual([f.figure_id for f in drawing.human_figures],
                         ["0:person:person", "1:person:person"])
        for f in drawing.human_figures:
            self.assertIn(f.torso, drawing.by_id())
            self.assertIn(f.head, {c.contour_id for c in drawing.contours})
        self.assertEqual(drawing.by_id()[drawing.human_figures[1].torso].start.as_tuple(), (34, 27))
        self.assertEqual(len(scene.to_record()["human_figures"]), 2)

    def test_unmarked_icons_keep_the_existing_record_shape(self):
        self.assertNotIn("human_figures", figure().to_record())


if __name__ == "__main__":
    unittest.main()
