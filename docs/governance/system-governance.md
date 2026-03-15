# System Governance

## Purpose

This document defines operating ownership and update rules across the repository, Codebeamer, and vTESTstudio.

## System Ownership

| Artifact | System of record | Owner responsibility |
|---|---|---|
| `SPEC-*` | Repo | Maintain source specification content and provenance |
| `SpecFragment` | Knowledge graph / Repo | Maintain stable fragment extraction from a spec source |
| `CandidateRequirement` | Knowledge graph / Repo | Maintain candidate extraction, confidence, risk, and review status |
| `REQ-*` | Codebeamer | Maintain formal approved requirement content |
| `TR-*` | Codebeamer | Maintain `REQ -> TR -> TI -> TC` verification structure |
| `TI-*` | Knowledge graph / Codebeamer hierarchy | Maintain scenario intent grouping for related testcases |
| `TC-*` | Codebeamer | Maintain testcase design and automation linkage |
| `TS-*` | vTESTstudio | Maintain executable test assets |
| `FEAT-*` / `VSTATE-*` / `SIG-*` / `FAULT-*` / `DIAG-*` / `VAR-*` / `SG-*` | Knowledge graph | Maintain automotive semantics context |
| `BUILD-*` / `RUN-*` / `RES-*` / `EVID-*` | Result layer | Maintain result-layer execution evidence |
| `ADR-*` / `decision-log` | Repo | Maintain architecture and governance decisions |
| `trace-matrix.md` | Repo | Maintain formal traceability review view |
| `automotive-matrix.md` | Repo | Maintain automotive semantics review view |
| `result-matrix.md` | Repo | Maintain result-layer review view |
| `.github/workflows/verification-gates.yml` | Repo | Maintain CI verification entry points |

## Update Triggers

### Spec ingestion change

When a `SPEC-*` source changes:

1. update `SpecFragment` extraction for `paragraph`, `clause`, and `table_row` units as needed
2. regenerate or review `CandidateRequirement` items with stable `candidate_id` values
3. preserve accurate `source_anchor` and `source_text`
4. refresh candidate `confidence`, `risk_level`, and `review_status`

### Candidate requirement review

When `CandidateRequirement` items are reviewed:

1. `pending` candidates must not become formal `REQ-*`
2. candidate `risk_level` is confidence-driven by default
3. candidates involving `safety`, regulatory obligation, `warning/telltale`, `fault reaction`, or `diagnostic behavior` must be treated as `high risk`
4. only `approved` candidates may be promoted into formal `REQ-*`
5. `rejected`, `needs_split`, and `needs_merge` candidates stay outside the formal traceability chain

### Requirement change

When a `REQ-*` changes in Codebeamer:

1. verify its candidate provenance when applicable
2. confirm related `TR-*` items still cover the requirement intent
3. confirm related `TC-*` items still provide adequate coverage
4. update impacted `Feature`, `Signal`, `SafetyGoal`, and `Variant` context when needed
5. update repo-side docs or ADRs when the model or policy changes

### Test requirement change

When a `TR-*` changes in Codebeamer:

1. confirm `REQ -> TR` remains valid
2. confirm `TR -> TI` still represents the intended scenario structure
3. confirm `TR -> TC` still covers the verification rule
4. update signal and fault semantics if the scope changed
5. update repo review views when the formal links changed

### Testcase change

When a `TC-*` changes in Codebeamer:

1. confirm `TR -> TC` remains valid
2. confirm the assigned `TI` and `Automation Status` / `vTESTstudio ID` are still correct
3. confirm the `TI` name follows `TI_<Domain>_<Intent>`
4. confirm linked `TS-*` assets remain valid when automated
5. update related `VehicleState`, `Signal`, `FaultReaction`, `DiagnosticEvent`, and `Variant` semantics when applicable
6. update `BUILD-*`, `RUN-*`, `RES-*`, and `EVID-*` relations when execution behavior changed

### Result change

When build, run, or result artifacts change:

1. confirm `TC -> BUILD` is correct
2. confirm `TS -> RUN` is correct
3. confirm `RUN -> RES` is correct
4. confirm `TS -> EVID` and `EVID -> BUILD` are correct
5. update `result-matrix.md`

### Model or process change

When the architecture, governance, or tooling policy changes:

1. record the decision in an ADR
2. update `docs/decisions/decision-log.md`
3. update `model-mapping.md`, `README.md`, and CI/test expectations as needed

## Operating Rules

1. repository, Codebeamer, and vTESTstudio each keep their own system-of-record responsibilities
2. automated `SPEC -> REQ` flow must go through `SpecFragment` and `CandidateRequirement`; it is not direct
3. `trace-matrix.md` is a review view, not the formal system of record
4. `automotive-matrix.md` is a review view for the automotive semantics axis
5. `result-matrix.md` is a review view for the result layer
6. `CandidateRequirement` is not part of the formal `REQ -> TR -> TC -> TS` compliance gate
7. `TR-*` carries requirement intent and `TI-*` carries scenario intent
8. `FEAT-*`, `VSTATE-*`, `SIG-*`, `FAULT-*`, `DIAG-*`, `VAR-*`, and `SG-*` provide automotive semantics context
9. `BUILD-*`, `RUN-*`, `RES-*`, and `EVID-*` provide execution-evidence context
10. every normative `REQ-*` must trace to at least one `TR-*`
11. every `TR-*` must trace to at least one `TC-*`
12. `TI-*` improves scenario structure but is not the minimum compliance gate
13. automated `TC-*` items should link to executable `TS-*` assets
14. CI must run unittest plus `check_all.py`

## Review Checklist

- `SPEC -> SpecFragment -> CandidateRequirement` retains stable IDs and source anchors
- `CandidateRequirement` keeps `confidence` and the correct `high risk` override behavior
- only approved candidates are promoted to formal `REQ`
- `REQ -> TR` is complete
- `TR -> TI` still matches scenario intent
- `TI -> TC` is complete where scenario grouping is used
- `TC -> TS` is valid for automated tests
- `Feature`, `VehicleState`, `Signal`, `FaultReaction`, `DiagnosticEvent`, `Variant`, and `SafetyGoal` links remain correct
- `TC -> BUILD`, `TS -> RUN`, `RUN -> RES`, `TS -> EVID`, and `EVID -> BUILD` are correct
- `trace-matrix.md`, `automotive-matrix.md`, and `result-matrix.md` match the intended review views
- `.github/workflows/verification-gates.yml` still runs unittest and `check_all.py`
- ADR and decision log entries are updated when governance changes

## Verification Entry Points

- `python scripts\check_traceability.py`
  minimum compliance gate for `REQ -> TR -> TC -> TS`
- `python scripts\check_automotive_semantics.py`
  automotive semantics integrity against `automotive-matrix.md`
- `python scripts\check_result_evidence.py`
  result-layer integrity against `result-matrix.md`
- `python scripts\check_all.py`
  runs every verification gate together
- `python -m unittest discover -s tests -p 'test_*.py' -v`
  regression test suite for docs, fixtures, and script behavior
