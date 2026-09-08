"""Icon records must conform to the published JSON Schema.

``jsonschema`` is not a dependency of this package, so when it is absent the
test falls back to a targeted structural check driven by the schema document
itself: required keys, enum and const values, and the primitive variants. That
covers the parts a record can realistically get wrong without turning this
module into a second JSON Schema implementation.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from icon_set.model.icons.registry import all_icons

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schemas" / "icon-record.schema.json"
SCHEMA = json.loads(SCHEMA_PATH.read_text())


def _check_value(case: unittest.TestCase, spec: dict, value: object, where: str) -> None:
    if "const" in spec:
        case.assertEqual(value, spec["const"], where)
    if "enum" in spec:
        case.assertIn(value, spec["enum"], where)


class SchemaConformanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.records = [icon.to_record() for icon in all_icons()]

    def test_schema_is_declared_against_a_known_draft(self) -> None:
        self.assertEqual(SCHEMA["$schema"], "https://json-schema.org/draft/2020-12/schema")

    def test_reserved_xs_tokens_are_absent_from_the_keyshape_enum(self) -> None:
        tokens = SCHEMA["properties"]["keyshape"]["enum"]
        self.assertNotIn("HRECT_XS", tokens)
        self.assertNotIn("VRECT_XS", tokens)

    def test_family_is_required_and_bound_to_profile(self) -> None:
        from icon_set.model import contracts

        self.assertIn("family", SCHEMA["required"])
        self.assertEqual(set(SCHEMA["properties"]["family"]["enum"]), set(contracts.families()))
        for record in self.records:
            with self.subTest(icon=record["icon_id"]):
                self.assertEqual(
                    contracts.families()[record["family"]]["profile"], record["profile"]
                )

    def test_records_validate(self) -> None:
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema not installed; structural checks cover the rest")
        validator = jsonschema.Draft202012Validator(SCHEMA)
        for record in self.records:
            with self.subTest(icon=record["icon_id"]):
                errors = sorted(validator.iter_errors(record), key=lambda e: e.path)
                self.assertEqual(errors, [], [error.message for error in errors])

    def test_required_keys_are_present(self) -> None:
        for record in self.records:
            with self.subTest(icon=record["icon_id"]):
                for key in SCHEMA["required"]:
                    self.assertIn(key, record)

    def test_no_unexpected_keys(self) -> None:
        allowed = set(SCHEMA["properties"])
        for record in self.records:
            with self.subTest(icon=record["icon_id"]):
                self.assertEqual(set(record) - allowed, set())

    def test_enums_and_constants_hold(self) -> None:
        properties = SCHEMA["properties"]
        for record in self.records:
            with self.subTest(icon=record["icon_id"]):
                for key, value in record.items():
                    _check_value(self, properties[key], value, f"{record['icon_id']}.{key}")
                for key, value in record["style"].items():
                    _check_value(
                        self, properties["style"]["properties"][key], value,
                        f"{record['icon_id']}.style.{key}",
                    )

    def test_primitives_match_a_schema_variant(self) -> None:
        variants = {
            variant["properties"]["kind"]["const"]: variant
            for variant in SCHEMA["$defs"]["primitive"]["oneOf"]
        }
        for record in self.records:
            for primitive in record["primitives"]:
                with self.subTest(icon=record["icon_id"], element=primitive["element_id"]):
                    variant = variants[primitive["kind"]]
                    self.assertEqual(set(primitive) - set(variant["properties"]), set())
                    for key in variant["required"]:
                        self.assertIn(key, primitive)
                    for axis in ("start", "end"):
                        point = primitive[axis]
                        self.assertEqual(len(point), 2)
                        self.assertTrue(all(isinstance(value, int) for value in point))

    def test_ids_follow_the_naming_pattern(self) -> None:
        import re

        pattern = re.compile(SCHEMA["properties"]["icon_id"]["pattern"])
        for record in self.records:
            with self.subTest(icon=record["icon_id"]):
                self.assertRegex(record["icon_id"], pattern)

    def test_contour_members_reference_real_primitives(self) -> None:
        for record in self.records:
            ids = {primitive["element_id"] for primitive in record["primitives"]}
            for contour in record["contours"]:
                with self.subTest(icon=record["icon_id"], contour=contour["contour_id"]):
                    self.assertTrue(set(contour["members"]) <= ids)

    def test_relationship_members_reference_real_primitives(self) -> None:
        for record in self.records:
            ids = {primitive["element_id"] for primitive in record["primitives"]}
            ids |= {contour["contour_id"] for contour in record["contours"]}
            for relation in record["relationships"]:
                with self.subTest(icon=record["icon_id"]):
                    self.assertTrue(set(relation["members"]) <= ids)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
