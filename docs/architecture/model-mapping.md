# veri-graph Model Mapping

## Purpose

This document defines how veri-graph concepts map across the repository, the knowledge graph, Codebeamer, and vTESTstudio.

## Canonical Chains

Formal graph chain:

`SPEC -> REQ -> TR -> TI -> TC -> TS`

Automated pre-requirement chain:

`SPEC -> SpecFragment -> CandidateRequirement -> Human Review -> REQ`

Minimum compliance gate:

`REQ -> TR -> TC -> TS`

## Layers

- source specification layer
- spec-ingestion and candidate-requirement layer
- formal verification and automotive semantics layer
- result layer for build, run, result, and evidence

## Mapping Table

| Concept | Keep | Independent ID | System of Record | Form | Purpose |
|---|---|---|---|---|---|
| `SPEC` | Yes | Yes | Repo | Markdown document | Source specification or upstream governing text |
| `SpecFragment` | Yes | Yes in graph | Knowledge graph / Repo | Ingested fragment node | Stable ingest unit derived from a spec |
| `CandidateRequirement` | Yes | Yes | Knowledge graph / Repo | Candidate requirement node | Auto-extracted requirement candidate awaiting review |
| `REQ` | Yes | Yes | Codebeamer | Requirement tracker item | Formal approved requirement |
| `TR` | Yes | Yes | Codebeamer | Test requirement tracker item | Requirement intent, verification rule, and acceptance logic |
| `TI` | Yes | Yes in graph | Knowledge graph / Codebeamer hierarchy | Scenario intent node carried by a hierarchy parent node | Scenario-level grouping between `TR` and `TC` |
| `TC` | Yes | Yes | Codebeamer | Test case tracker item | Managed test case |
| `TS` | Yes | Yes | vTESTstudio | Executable test asset | Executable implementation of a testcase |
| `Feature` | Yes | Yes in graph | Knowledge graph | Domain node | Functional feature context |
| `VehicleState` | Yes | Yes in graph | Knowledge graph | Domain node | Vehicle operating state context |
| `Signal` | Yes | Yes in graph | Knowledge graph | Domain node | Signal or interface dependency |
| `FaultReaction` | Yes | Yes in graph | Knowledge graph | Domain node | Expected reaction to a fault |
| `DiagnosticEvent` | Yes | Yes in graph | Knowledge graph | Domain node | Diagnostic-event context |
| `Variant` | Yes | Yes in graph | Knowledge graph | Domain node | Vehicle or equipment applicability |
| `SafetyGoal` | Yes | Yes in graph | Knowledge graph | Domain node | Safety objective context |
| `Build` | Yes | Yes | Result layer | Result node | Software or ECU build under test |
| `TestRun` | Yes | Yes | Result layer | Result node | Execution batch or run instance |
| `Result` | Yes | Yes | Result layer | Result node | Outcome produced by a test run |
| `Evidence` | Yes | Yes | Result layer | Result node | Collected proof such as log, capture, or artifact |

## Design Rules

1. `SPEC -> REQ` is not direct in the automated pipeline; it passes through `SpecFragment` and `CandidateRequirement`.
2. `CandidateRequirement` is not part of the formal requirement chain.
3. Every candidate must be human-reviewed before it can become a formal `REQ`.
4. Candidate risk is confidence-driven by default.
5. Candidates involving `safety`, regulatory obligation, `warning/telltale`, `fault reaction`, or `diagnostic behavior` override to `high risk`.
6. `TR` carries requirement intent.
7. `TI` carries scenario intent.
8. Automotive semantics nodes attach domain meaning to the verification chain.
9. Result-layer nodes attach execution evidence to tests.
10. Codebeamer is the formal system of record for approved `REQ/TR/TC`, not for candidate requirements.

## Field Guidance

- `SPEC` may be an internal ID-based source or an external-style source file such as `S6867-07-blocked.md`.
- `SpecFragment` should carry `fragment_id`, `source_spec_id`, `fragment_type`, `source_anchor`, and `source_text`.
- `fragment_type` should be one of `paragraph`, `clause`, or `table_row`.
- `CandidateRequirement` should carry `candidate_id`, `source_spec_id`, `source_anchor`, `source_text`, `normalized_statement`, `modality`, `confidence`, `risk_level`, and `review_status`.
- `CandidateRequirement.review_status` should be one of `pending`, `approved`, `rejected`, `needs_split`, or `needs_merge`.
- Approved `REQ` items must link to at least one `TR-*`.
- `TR` must describe the verification rule for the approved requirement.
- `TI` should group test cases by scenario intent.
- `TC` should carry `Automation Status` and `vTESTstudio ID` where applicable.
- `TS` should preserve the executable link back to its source `TC`.

## Non-Goals For V1

- no automatic promotion from candidate requirement to formal `REQ`
- no direct mapping of `CandidateRequirement` into a Codebeamer requirement tracker
- no direct `CandidateRequirement -> TR/TC` chain in the formal matrices
- no Markdown file as the authoritative source of executable `TS` content
- no requirement yet for a full extraction engine, LLM pipeline, or review UI in this repository
