# Knowledge Graph Schema (NetworkX Prototype)

## Node Types

- Spec (`SPEC-*`)
- Requirement (`REQ-*`)
- TestRequirement (`TR-*`)
- TestIntent (`TI-*`)
- Testcase (`TC-*`)
- TestScript (`TS-*`)
- Feature (`FEAT-*`)
- VehicleState (`VSTATE-*`)
- Signal (`SIG-*`)
- FaultReaction (`FAULT-*`)
- DiagnosticEvent (`DIAG-*`)
- Variant (`VAR-*`)
- SafetyGoal (`SG-*`)
- Build (`BUILD-*`)
- TestRun (`RUN-*`)
- Result (`RES-*`)
- Evidence (`EVID-*`)

## Node Semantics

- `TR-*` carries requirement intent
- `TI-*` carries scenario intent
- `TI-*` is a graph node even if Codebeamer carries it through a hierarchy parent node
- `Feature-*`, `VehicleState-*`, `Signal-*`, `FaultReaction-*`, `DiagnosticEvent-*`, `Variant-*`, `SafetyGoal-*` belong to the automotive semantics axis
- `Build-*`, `TestRun-*`, `Result-*`, `Evidence-*` belong to the result layer

## Edge Types

- `derived_from`
- `validated_by`
- `organized_by`
- `specified_by`
- `implemented_by`
- `belongs_to_feature`
- `applies_in_state`
- `depends_on_signal`
- `covers_fault_reaction`
- `covers_diagnostic_event`
- `applies_to_variant`
- `satisfies_safety_goal`
- `executed_on_build`
- `executed_in_run`
- `produced_result`
- `measured_on_build`
- `produces_evidence`
- `collected_from_build`

## Edge Meanings

- `REQ -> TR` uses `validated_by`
- `TR -> TI` uses `organized_by`
- `TI -> TC` uses `specified_by`
- `TC -> TS` uses `implemented_by`
- `Feature -> REQ` uses `belongs_to_feature`
- `VehicleState -> TI` uses `applies_in_state`
- `Signal -> REQ` or `Signal -> TR` uses `depends_on_signal`
- `FaultReaction -> TI` or `FaultReaction -> TC` uses `covers_fault_reaction`
- `DiagnosticEvent -> FAULT` or `DiagnosticEvent -> TC` uses `covers_diagnostic_event`
- `Variant -> REQ` or `Variant -> TC` uses `applies_to_variant`
- `SafetyGoal -> REQ` uses `satisfies_safety_goal`
- `TC -> BUILD` uses `executed_on_build`
- `TS -> RUN` uses `executed_in_run`
- `RUN -> RES` uses `produced_result`
- `RES -> BUILD` uses `measured_on_build`
- `TS -> EVID` uses `produces_evidence`
- `EVID -> BUILD` uses `collected_from_build`

## Minimum Required Properties

- node: `id`, `type`, `status`, `version`
- edge: `relation`, `status`, `last_reviewed_at`
