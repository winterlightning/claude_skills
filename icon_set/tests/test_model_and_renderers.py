"""Class model, topology, composition parity, and deterministic export."""

from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from icon_set.model.icons.base import Icon
from icon_set.model.icons.combined import CombinedIcon
from icon_set.model.icons.sub.shapes import Heart
from icon_set.model.keyshapes import Keyshape
from icon_set.model.position import PlacedIcon, Position
from icon_set.model.primitives import (
    Arc,
    Line,
    Point,
    primitive_from_dict,
    primitive_to_dict,
    translate,
)
from icon_set.model.profiles import Profile
from icon_set.renderers.svg import build_paths, render_svg
from icon_set.validation.svg_reader import parse_svg


class HeartApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.heart = Heart()

    def test_heart_is_an_icon(self) -> None:
        self.assertIsInstance(self.heart, Icon)

    def test_primitives_keep_stable_ids_and_drawing_order(self) -> None:
        self.assertEqual(
            [primitive.element_id for primitive in self.heart.primitives],
            [
                "lobe-left-inner", "lobe-left-outer", "shoulder-left", "side-left",
                "side-right", "shoulder-right", "lobe-right-outer", "lobe-right-inner",
            ],
        )

    def test_primitives_are_typed(self) -> None:
        kinds = [type(primitive).__name__ for primitive in self.heart.primitives]
        self.assertEqual(
            kinds, ["Arc", "Arc", "Arc", "Line", "Line", "Arc", "Arc", "Arc"]
        )

    def test_closed_contour_renders_as_one_joined_path(self) -> None:
        paths = build_paths(self.heart.draw())
        self.assertEqual(len(paths), 1)
        self.assertTrue(paths[0]["d"].endswith("Z"))

    def test_missing_contour_member_fails(self) -> None:
        icon = Icon("x", Profile.SUB32, semantic_role="SUB", keyshape=Keyshape.SQUARE)
        icon.add_line("a", (4, 4), (28, 4))
        icon.add_contour("outline", "a", "ghost")
        with self.assertRaises(ValueError):
            build_paths(icon.draw())

    def test_duplicate_contour_membership_fails(self) -> None:
        icon = Icon("x", Profile.SUB32, semantic_role="SUB", keyshape=Keyshape.SQUARE)
        icon.add_line("a", (4, 4), (28, 4))
        icon.add_contour("one", "a")
        icon.add_contour("two", "a")
        with self.assertRaises(ValueError):
            build_paths(icon.draw())

    def test_non_contiguous_contour_fails(self) -> None:
        icon = Icon("x", Profile.SUB32, semantic_role="SUB", keyshape=Keyshape.SQUARE)
        icon.add_line("a", (4, 4), (28, 4))
        icon.add_line("b", (4, 28), (28, 28))
        icon.add_contour("outline", "a", "b")
        with self.assertRaises(ValueError):
            build_paths(icon.draw())

    def test_unclosed_closed_contour_fails(self) -> None:
        icon = Icon("x", Profile.SUB32, semantic_role="SUB", keyshape=Keyshape.SQUARE)
        icon.add_line("a", (4, 4), (28, 4))
        icon.add_line("b", (28, 4), (28, 28))
        icon.add_contour("outline", "a", "b", closed=True)
        with self.assertRaises(ValueError):
            build_paths(icon.draw())


class PrimitiveAstTests(unittest.TestCase):
    def test_round_trip_through_the_interchange_format(self) -> None:
        for primitive in (
            Line("a", Point(1, 2), Point(3, 4)),
            Arc("b", Point(1, 2), Point(3, 4), 7, 9, True, False),
        ):
            with self.subTest(kind=type(primitive).__name__):
                self.assertEqual(primitive_from_dict(primitive_to_dict(primitive)), primitive)

    def test_translation_is_integer_only(self) -> None:
        moved = translate(Line("a", Point(1, 2), Point(3, 4)), Position(10, 20))
        self.assertEqual((moved.start, moved.end), (Point(11, 22), Point(13, 24)))


class CombinedIconTests(unittest.TestCase):
    def _child(self) -> Icon:
        icon = Icon("plus", Profile.SUB32, semantic_role="SUB", keyshape=Keyshape.SQUARE)
        icon.add_line("bar", (4, 16), (28, 16))
        icon.add_anchor("centre", (16, 16))
        icon.relate("connect", "bar")
        return icon

    def test_unequal_arrays_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            CombinedIcon(
                "x", "SIDE_COMBINE", Keyshape.SQUARE,
                icons=[self._child()], positions=[],
            )

    def test_nth_icon_maps_to_nth_position(self) -> None:
        first, second = self._child(), self._child()
        combined = CombinedIcon(
            "x", "SIDE_COMBINE", Keyshape.SQUARE,
            icons=[first, second], positions=[Position(0, 0), Position(8, 8)],
        )
        self.assertEqual(combined.icons, [first, second])
        self.assertEqual(combined.positions, [Position(0, 0), Position(8, 8)])

    def test_mutating_a_returned_array_cannot_break_parity(self) -> None:
        combined = CombinedIcon(
            "x", "SIDE_COMBINE", Keyshape.SQUARE,
            icons=[self._child()], positions=[Position(0, 0)],
        )
        combined.icons.append(self._child())
        self.assertEqual(len(combined.icons), len(combined.positions))

    def test_add_icon_appends_one_pair_atomically(self) -> None:
        combined = CombinedIcon("x", "SIDE_COMBINE", Keyshape.SQUARE)
        combined.add_icon(self._child(), Position(4, 4))
        self.assertEqual(len(combined.children), 1)
        self.assertIsInstance(combined.children[0], PlacedIcon)

    def test_children_are_namespaced_translated_and_unchanged(self) -> None:
        child = self._child()
        before = list(child.primitives)
        combined = CombinedIcon(
            "x", "SIDE_COMBINE", Keyshape.SQUARE,
            icons=[child], positions=[Position(10, 20)],
        )
        drawing = combined.draw()
        self.assertEqual([p.element_id for p in drawing.primitives], ["0:plus:bar"])
        self.assertEqual(drawing.primitives[0].start, Point(14, 36))
        self.assertEqual(dict(drawing.anchors)["0:plus:centre"], Point(26, 36))
        self.assertEqual(drawing.relationships[0].members, ("0:plus:bar",))
        self.assertEqual(child.primitives, before)

    def test_unknown_composition_class_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            CombinedIcon("x", "NONSENSE", Keyshape.SQUARE)

    def test_combined_icons_emit_container64(self) -> None:
        combined = CombinedIcon("x", "SIDE_COMBINE", Keyshape.SQUARE)
        self.assertIs(combined.profile, Profile.CONTAINER64)
        self.assertEqual(combined.family, "container")


class RendererTests(unittest.TestCase):
    def setUp(self) -> None:
        self.heart = Heart()

    def test_exact_viewbox_and_canonical_style(self) -> None:
        parsed = parse_svg(render_svg(self.heart))
        self.assertEqual(parsed.view_box, (0.0, 0.0, 32.0, 32.0))
        self.assertEqual((parsed.width, parsed.height), (32, 32))
        self.assertEqual(parsed.style, {
            "fill": "none", "stroke": "currentColor", "stroke-width": "4",
            "stroke-linecap": "round", "stroke-linejoin": "round",
        })

    def test_no_transform_survives_a_round_trip(self) -> None:
        self.assertNotIn("transform", render_svg(self.heart))

    def test_repeated_renders_are_identical(self) -> None:
        self.assertEqual(render_svg(self.heart), render_svg(Heart()))

    def test_svg_and_png_resolve_from_the_same_scene(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            svg = self.heart.export_icon_to(root / "heart.svg")
            png = self.heart.export_icon_to(root / "heart.png")
            self.assertEqual(svg.read_text(), render_svg(self.heart))
            self.assertTrue(png.read_bytes().startswith(b"\x89PNG"))

    def test_repeated_exports_are_deterministic(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            first = self.heart.export_icon_to(root / "a.svg").read_text()
            second = Heart().export_icon_to(root / "b.svg").read_text()
            self.assertEqual(first, second)

    def test_unsupported_format_fails_clearly(self) -> None:
        with TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                self.heart.export_icon_to(Path(directory) / "heart.pdf")

    def test_a_scaled_group_is_rejected_even_with_stroke_reset(self) -> None:
        document = render_svg(self.heart).replace(
            "<path", '<g transform="scale(2)" stroke-width="4"><path', 1
        ).replace("</svg>", "</g></svg>")
        from icon_set.validation.svg_reader import SvgRoundTripError

        with self.assertRaises(SvgRoundTripError):
            parse_svg(document)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
