# Side sub-icons and container symbols

These are actual families: side sub-icons belong to `sub` / `SUB32`; container symbols belong to `symbol` / `SYMBOL32`. Their numeric drawing rules remain identical.

- **Side sub-icon:** used beside a main icon.
- **Container symbol:** used inside a container.
- 532 side-only originals, 711 symbol-only originals, 293 originals used in both.
- 825 side entries, 1,004 symbol entries, 1,829 role entries total.

The authoritative assignments and reciprocal links are in `icon_set/data/sub-usage-categories.json`. Each shared original retains its existing side model and has an independent `-symbol` Python model. The symbol copies contain their own drawing code, not a subclass of the side drawing. Both retain source provenance. `related_group` records common origin; it does not synchronize edits. Unused library models remain unassigned.

The main gallery supports `family=symbol` and `family=sub`, including model editing and reciprocal links. Symbol models live in `icon_set/model/icons/symbol/`; their validated release folder is `icon_set/dist/symbol32/`. Existing review drafts remain explicitly unvalidated managed models.

The browser links directly to each editable model and can show both linked versions. Export assets live in separate `icon_set/assets/sub-usage/side/` and `symbol/` directories. Published preview copies are under `icon_set/dist/gallery/sub-usage/`.

After changing either model, validate the edited version with `python3 -m icon_set.scripts.sub_usage_categories --validate ICON_ID`. Without a new validation result, changed geometry is marked stale. Refresh the combination catalog with `python3 -m icon_set.scripts.combination_catalog`, the category browser with `python3 -m icon_set.scripts.build_sub_usage_report`, and the container pair gallery with `python3 -m icon_set.scripts.build_paired_container_combinations`. Normal gallery generation also applies the role selection. Side inputs keep their original identities.

Initial migration copies geometry exactly, including existing source drawing failures; categorization is not a claim of design approval. All 293 copied models were compared to their originals. Existing side pair choices and container placements/fit states are preserved. One repeated identical gift/people preview was consolidated; all 2,709 defined container pairs remain covered.
