# Query Requirements (Prototype)

1. Find `TR-*` items missing a source `REQ-*` and report them as non-compliant.
2. Find `TC-*` items missing a source `TR-*` and report them as non-compliant.
3. Find scenario intent coverage by listing `TI-*` under each `TR-*`.
4. Find `TC-*` items not grouped under any `TI-*`.
5. Find `TS-*` items not linked to a `TC-*` or declared as intentionally not automated.
6. Find orphan testcases with no test requirement or scenario intent context.
7. Find stale links using `last_reviewed_at`.
8. List every `SpecFragment` extracted from a given `SPEC` source.
9. List every `CandidateRequirement` yielded from a given `SpecFragment`.
10. Find every `CandidateRequirement` with `review_status=pending`.
11. Find every `CandidateRequirement` with `risk_level=high`.
12. Find every approved `CandidateRequirement` that does not map to a formal `REQ-*`.
13. Find every `CandidateRequirement` marked `needs_split` or `needs_merge`.
14. List every formal `REQ-*` and its originating `CandidateRequirement` when available.
15. Find every `Feature-*` linked to impacted `REQ/TR/TC` nodes.
16. Find every `VehicleState-*` linked to impacted `TI/TC` nodes.
17. Find every `Signal-*` linked to impacted `REQ/TR` nodes.
18. Find every `FaultReaction-*` linked to impacted `TI/TC` nodes.
19. Find every `DiagnosticEvent-*` linked to impacted `FAULT/TC` nodes.
20. Find every `Variant-*` linked to impacted `REQ/TC` nodes.
21. Find every `SafetyGoal-*` whose downstream `REQ-*` nodes remain uncovered.
22. Find every `Build-*` and the `TC-*` items executed on it.
23. Find every `Run-*` and the `Result-*` nodes it produced.
24. Find every `Evidence-*` node and the `TS-*` source that produced it.
25. Identify which verification or automotive semantics queries remain planned but not yet implemented.
