"""The vendored Lucide bundle and its inspector."""

from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.scripts_lucide import (
    REFERENCE_ROOT,
    debug_path,
    inspect_reference,
    load_index,
    original_path,
    read_atoms,
    search,
)


class BundleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.index = load_index()

    def test_the_bundle_is_present(self) -> None:
        for name in ("index.json", "LICENSE", "PROVENANCE.md"):
            with self.subTest(file=name):
                self.assertTrue((REFERENCE_ROOT / name).is_file())
        for folder in ("original", "atomic-debug"):
            with self.subTest(folder=folder):
                self.assertTrue((REFERENCE_ROOT / folder).is_dir())

    def test_both_views_cover_every_indexed_icon(self) -> None:
        for folder, key in (("original", "original"), ("atomic-debug", "debug")):
            files = {p.name for p in (REFERENCE_ROOT / folder).glob("*.svg")}
            self.assertEqual(len(files), self.index["iconCount"], folder)
            for entry in self.index["icons"]:
                with self.subTest(icon=entry["name"], view=folder):
                    self.assertIn(Path(entry[key]).name, files)

    def test_the_indexed_hashes_match_what_is_on_disk(self) -> None:
        """Spot-checked rather than exhaustive: 3,596 hashes is a slow test."""
        for name in ("heart", "house", "circle"):
            entry = next(e for e in self.index["icons"] if e["name"] == name)
            for key, path in (("originalSha256", original_path(name)),
                              ("debugSha256", debug_path(name))):
                with self.subTest(icon=name, hash=key):
                    digest = hashlib.sha256(path.read_bytes()).hexdigest()
                    self.assertEqual(digest, entry[key])

    def test_the_segment_metadata_is_counted_from_the_debug_view(self) -> None:
        """The index's construction numbers and `atomic-debug/` cannot drift apart."""
        for name in ("heart", "house", "circle", "square", "chevron-right"):
            entry = next(e for e in self.index["icons"] if e["name"] == name)
            atoms = read_atoms(name)
            with self.subTest(icon=name):
                self.assertEqual(len(atoms), entry["segmentCount"])
                tally: dict[str, int] = {}
                for atom in atoms:
                    tally[atom["kind"]] = tally.get(atom["kind"], 0) + 1
                self.assertEqual(dict(sorted(tally.items())), entry["segmentKinds"])

    def test_the_geometry_reference_is_documented(self) -> None:
        """Carried deliberately, with its caveats written down."""
        self.assertIn("atomic-debug/", self.index["bundle"]["carried"])
        self.assertEqual(self.index["bundle"]["omitted"], [])
        provenance = (REFERENCE_ROOT / "PROVENANCE.md").read_text()
        self.assertIn("atomic-debug", provenance)
        for attribute in ("data-atom", "data-src", "data-kind"):
            with self.subTest(attribute=attribute):
                self.assertIn(attribute, provenance)

    def test_licence_is_retained(self) -> None:
        self.assertTrue((REFERENCE_ROOT / "LICENSE").read_text().strip())


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.index = load_index()

    def test_an_exact_name_ranks_first(self) -> None:
        self.assertEqual(search("heart", self.index, 5)[0]["name"], "heart")

    def test_limit_is_honoured(self) -> None:
        self.assertLessEqual(len(search("arrow", self.index, 3)), 3)

    def test_an_unmatched_query_returns_nothing(self) -> None:
        self.assertEqual(search("zzzznotathing", self.index, 5), [])


class AtomTests(unittest.TestCase):
    """`atomic-debug/` read as a geometry reference."""

    def test_atoms_come_back_in_document_order_with_their_kinds(self) -> None:
        atoms = read_atoms("heart")
        self.assertEqual([a["atom"] for a in atoms],
                         [f"0.{i}" for i in range(len(atoms))])
        self.assertEqual(atoms[0]["kind"], "arc/circular")
        self.assertTrue(all(a["d"].startswith("M") for a in atoms))
        self.assertTrue(all(a["source"] for a in atoms))

    def test_a_native_circle_arrives_as_four_quarter_arcs(self) -> None:
        """The caveat the docs state, asserted so it stays true of the bundle."""
        atoms = read_atoms("circle")
        self.assertTrue(any(a["source"] == "circle" for a in atoms))
        quarters = [a for a in atoms if a["kind"] == "arc/quarter-circle"]
        self.assertGreaterEqual(len(quarters), 4)

    def test_inspect_carries_the_atom_tally(self) -> None:
        report = inspect_reference("heart", Profile.SUB32)
        self.assertEqual(sum(report["atomKinds"].values()), len(report["atoms"]))
        self.assertEqual(report["atomKinds"]["arc/circular"], 4)

    def test_a_missing_debug_view_fails_clearly(self) -> None:
        with self.assertRaises(ValueError):
            debug_path("no-such-icon")

    def test_a_traversal_attempt_is_rejected_on_both_views(self) -> None:
        for reader in (original_path, debug_path):
            with self.subTest(reader=reader.__name__):
                with self.assertRaises(ValueError):
                    reader("../../../etc/passwd")


class InspectTests(unittest.TestCase):
    def test_a_missing_reference_fails_clearly(self) -> None:
        with self.assertRaises(ValueError):
            original_path("no-such-icon")

    def test_a_traversal_attempt_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            original_path("../../../etc/passwd")

    def test_inspect_reports_in_this_systems_terms(self) -> None:
        report = inspect_reference("heart", Profile.SUB32)
        self.assertEqual(report["viewBox"], "0 0 24 24")
        self.assertEqual(report["target"]["canvas"], 32)
        self.assertEqual(report["target"]["stroke"], 4)
        self.assertTrue(report["sourceElements"])
        self.assertIn("referenceBounds", report)
        self.assertIn("suggestedKeyshapes", report)

    def test_the_heart_reference_points_at_the_keyshape_we_chose(self) -> None:
        report = inspect_reference("heart", Profile.SUB32)
        suggested = [row["keyshape"] for row in report["suggestedKeyshapes"]]
        self.assertEqual(suggested[0], Keyshape.HRECT_XL.name)

    def test_suggestions_resolve_against_the_requested_profile(self) -> None:
        report = inspect_reference("heart", Profile.CONTAINER64)
        top = report["suggestedKeyshapes"][0]
        shape = Keyshape[top["keyshape"]]
        self.assertEqual(top["visible_bounds"], list(shape.bounds_for(Profile.CONTAINER64)))

    def test_the_stroke_weight_gap_is_stated(self) -> None:
        note = inspect_reference("heart", Profile.SUB32)["target"]["relative_weight_note"]
        self.assertIn("1.50x heavier", note)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
