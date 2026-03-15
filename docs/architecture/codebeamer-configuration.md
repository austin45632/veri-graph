# Codebeamer Configuration

## Purpose

This document defines the formal Codebeamer configuration boundary for veri-graph.

## Scope Boundary

The following concepts stay outside Codebeamer formal trackers:

- raw `SPEC` ingestion
- `SpecFragment`
- `CandidateRequirement`
- candidate review workflow before requirement approval

Those concepts remain in the repository and knowledge-graph layer. Only approved requirements are admitted into Codebeamer as formal `REQ-*` items.

## Tracker Layout

| Concept | Codebeamer object | Key fields | Required links |
|---|---|---|---|
| `REQ-*` | Requirement tracker item | ID, Title, Status, Owner, Priority | At least one `TR-*` via `validated_by` |
| `TR-*` | Test requirement tracker item | ID, Title, Status, Owner, Verification Rule, Coverage Status, Source Requirement | One source `REQ-*`, optional one or more `TI-*`, at least one `TC-*` via `verified_by` |
| `TI-*` | Scenario intent node carried by the test case hierarchy | Name, Description | Groups related `TC-*` items under one `TR-*` |
| `TC-*` | Test case tracker item | ID, Title, Status, Owner, Automation Status, vTESTstudio ID | One source `TR-*`, one source `TI-*`, optional one or more `TS-*` |

## Requirement Admission Rule

- only `CandidateRequirement.review_status=approved` may be promoted to a formal `REQ-*`
- `rejected`, `needs_split`, and `needs_merge` candidates remain outside Codebeamer
- Codebeamer stores only formal approved requirements

## Field Guidance

### Requirement tracker

Required fields:
- `ID`
- `Title`
- `Status`
- `Owner`
- `Priority`

Required relation:
- `validated_by` to at least one `TR-*`

Recommended provenance fields:
- `Source Spec ID`
- `Source Anchor`
- `Candidate Requirement ID`

### Test requirement tracker

Required fields:
- `ID`
- `Title`
- `Status`
- `Owner`
- `Verification Rule`
- `Coverage Status`
- `Source Requirement`

Recommended status values:
- `draft`
- `active`
- `reviewed`
- `obsolete`

Required relations:
- exactly one source `REQ-*`
- at least one `TC-*` via `verified_by`

### Test intent node

Minimum fields:
- `Name`
- `Description`

Semantics:
- graph-level `TI-*` is a scenario intent node
- Codebeamer carries it through the test case hierarchy
- no independent tracker workflow is required

### Test case tracker

Required fields:
- `ID`
- `Title`
- `Status`
- `Owner`
- `Automation Status`
- `vTESTstudio ID`

Recommended `Automation Status` values:
- `not_automated`
- `planned`
- `automated`
- `retired`

Required relations:
- exactly one source `TR-*`
- exactly one source `TI-*` in the graph model
- zero or more linked `TS-*` in vTESTstudio

## TI Parent Node Rules

- `TI` is not an independent tracker
- each `TI` acts as a hierarchy parent node such as `TI_Speed_Normal`
- each `TI` should provide a `Name` and `Description`
- `TC-*` items should be grouped under an appropriate `TI`
- `TI` exists to preserve scenario intent without adding workflow overhead

## TI Naming Convention

- format: `TI_<Domain>_<Intent>`
- `Domain` should be a functional or signal domain such as `Speed`, `Brake`, or `CAN`
- `Intent` should describe the scenario type such as `Normal`, `Boundary`, or `Timeout`
- do not encode testcase numbers or step details in the `TI` name
- names must be unique under the same `TR-*`

## Traceability Rules

1. every normative `REQ-*` must have at least one `TR-*`
2. every `TR-*` must have at least one `TC-*`
3. when scenario grouping is used, each `TR-*` should organize its `TC-*` through one or more `TI-*`
4. every `TC-*` must declare `Automation Status`
5. every `TC-*` with `Automation Status=automated` must carry a `vTESTstudio ID`
6. repo matrices remain review views; the formal minimum gate is still `REQ -> TR -> TC -> TS`
