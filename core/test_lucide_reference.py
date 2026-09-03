"""Paired reference lookup, exact geometry, and snapshot integrity tests."""
import hashlib
import json
from pathlib import Path
import unittest

from lucide_reference import REFERENCE_ROOT, inspect_reference, reference_paths, search


class LucideReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((REFERENCE_ROOT / "index.json").read_text())

    def test_snapshot_is_paired_and_hash_locked(self):
        self.assertEqual(self.index["iconCount"], len(self.index["icons"]))
        self.assertGreater(self.index["iconCount"], 1000)
        for entry in self.index["icons"]:
            original, debug = reference_paths(entry["name"])
            self.assertEqual(hashlib.sha256(original.read_bytes()).hexdigest(), entry["originalSha256"])
            self.assertEqual(hashlib.sha256(debug.read_bytes()).hexdigest(), entry["debugSha256"])

    def test_exact_names_and_semantic_aliases(self):
        self.assertEqual(search("house", self.index)[0]["name"], "house")
        self.assertEqual(search("handset", self.index)[0]["name"], "phone")
        self.assertEqual(search("envelope", self.index)[0]["name"], "mail")
        self.assertLessEqual(len(search("circle", self.index, 3)), 3)
        self.assertEqual(search("", self.index), [])

    def test_inspect_keeps_source_grouping_and_debug_segments(self):
        result = inspect_reference("search")
        self.assertEqual(len(result["sourceElements"]), 2)
        self.assertEqual(len(result["segments"]), 5)
        self.assertEqual(result["sourceElements"][1]["tag"], "circle")
        self.assertTrue(all(part["d"].startswith("M") for part in result["segments"]))

    def test_reference_names_cannot_escape_snapshot(self):
        for name in ("../house", "/tmp/a", "House", "house.svg", "a\\b"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                reference_paths(name)


if __name__ == "__main__":
    unittest.main()
