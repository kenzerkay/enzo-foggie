#!/usr/bin/env python3
"""Move explicitly mapped Enzo problem-type files to and from enzo-trash.

Run without --apply to preview file moves and manifest edits.

python move_problem_type_files.py $(python -c 'import ast; tree=ast.parse(open("enzo-foggie/tools/move_problem_type_files.py").read()); d=next(n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="PROBLEM_TYPE_FILES" for t in n.targets)); print(*sorted(ast.literal_eval(d.value)))') --apply --update-manifest
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


PROBLEM_TYPE_FILES = {
    1: (
        "HydroShockTubesInitialize.C",
        "Grid_HydroShockTubesInitializeGrid.C",
    ),
    2: (
        "WavePoolInitialize.C",
        "WavePoolGlobalData.h",
        "ExternalBoundary_SetWavePoolBoundary.C",
    ),
    3: (
        "ShockPoolInitialize.C",
        "ShockPoolGlobalData.h",
        "ExternalBoundary_SetShockPoolBoundary.C",
    ),
    4: (
        "DoubleMachInitialize.C",
        "Grid_DoubleMachInitializeGrid.C",
        "ExternalBoundary_SetDoubleMachBoundary.C",
    ),
    5: ("ShockInABoxInitialize.C",),
    6: (
        "ImplosionInitialize.C",
        "Grid_ImplosionInitializeGrid.C",
        "ImplosionGlobalData.h",
    ),
    7: (
        "SedovBlastInitialize.C",
        "Grid_SedovBlastInitializeGrid.C",
        "Grid_SedovBlastInitializeGrid3D.C",
        "SedovBlastGlobalData.h",
    ),
    8: (
        "KHInitialize.C",
        "Grid_KHInitializeGrid.C",
        "Grid_KHInitializeGridRamp.C",
    ),
    9: (
        "NohInitialize.C",
        "Grid_NohInitializeGrid.C",
        "Grid_ComputeExternalNohBoundary.C",
    ),
    10: (
        "RotatingCylinderInitialize.C",
        "Grid_RotatingCylinderInitialize.C",
        "ProblemType_RotatingCylinder.C",
    ),
    11: (
        "RadiatingShockInitialize.C",
        "Grid_RadiatingShockInitializeGrid.C",
        "RadiatingShockGlobalData.h",
    ),
    12: (
        "FreeExpansionInitialize.C",
        "Grid_FreeExpansionInitializeGrid.C",
    ),
    13: (
        "RotatingDiskInitialize.C",
        "Grid_RotatingDiskInitializeGrid.C",
    ),
    14: (
        "RotatingSphereInitialize.C",
        "Grid_RotatingSphereInitialize.C",
    ),
    20: (
        "ZeldovichPancakeInitialize.C",
        "Grid_ZeldovichPancakeInitializeGrid.C",
    ),
    21: (
        "PressurelessCollapseInitialize.C",
        "Grid_PressurelessCollapseInitialize.C",
    ),
    22: ("AdiabaticExpansionInitialize.C",),
    23: (
        "TestGravityInitialize.C",
        "Grid_TestGravityInitializeGrid.C",
        "TestGravityCheckResults.C",
        "Grid_TestGravityCheckResults.C",
    ),
    24: (
        "SphericalInfallInitialize.C",
        "Grid_SphericalInfallInitializeGrid.C",
        "Grid_SphericalInfallGetProfile.C",
    ),
    25: (
        "TestGravitySphereInitialize.C",
        "Grid_TestGravitySphereInitializeGrid.C",
        "TestGravitySphereCheckResults.C",
        "Grid_TestGravitySphereCheckResults.C",
        "TestGravitySphereGlobalData.h",
    ),
    26: (
        "GravityEquilibriumTestInitialize.C",
        "Grid_GravityEquilibriumTestInitializeGrid.C",
    ),
    27: (
        "CollapseTestInitialize.C",
        "Grid_CollapseTestInitializeGrid.C",
    ),
    28: (
        "TestGravityMotion.C",
        "Grid_TestGravityMotionInitializeGrid.C",
    ),
    29: (
        "TestOrbitInitialize.C",
        "Grid_TestOrbitInitializeGrid.C",
    ),
    30: (
        "CosmologySimulationInitialize.C",
        "NestedCosmologySimulationInitialize.C",
        "Grid_CosmologySimulationInitializeGrid.C",
        "Grid_NestedCosmologySimulationInitializeGrid.C",
        "Grid_CosmologyInitializeParticles.C",
        "Grid_CosmologyReadParticles3D.C",
    ),
    35: (
        "ShearingBoxInitialize.C",
        "Grid_ShearingBoxInitializeGrid.C",
    ),
    36: (
        "ShearingBox2DInitialize.C",
        "Grid_ShearingBox2DInitializeGrid.C",
    ),
    37: (
        "ShearingBoxStratifiedInitialize.C",
        "Grid_ShearingBoxStratifiedInitializeGrid.C",
    ),
    40: (
        "SupernovaRestartInitialize.C",
        "Grid_SupernovaRestartInitialize.C",
    ),
    50: (
        "PhotonTestInitialize.C",
        "Grid_PhotonTestInitializeGrid.C",
    ),
    51: (
        "PhotonTestRestartInitialize.C",
        "Grid_PhotonTestRestartInitializeGrid.C",
    ),
    # 59: (
    #     "DrivenFlowInitialize.C",
    #     "Grid_DrivenFlowInitializeGrid.C",
    # ),
    60: (
        "hydro_rk/TurbulenceSimulationInitialize.C",
        "hydro_rk/Grid_TurbulenceSimulationInitializeGrid.C",
    ),
    61: (
        "ProtostellarCollapseInitialize.C",
        "Grid_ProtostellarCollapseInitializeGrid.C",
    ),
    62: (
        "CoolingTestInitialize.C",
        "Grid_CoolingTestInitializeGrid.C",
        "Grid_CoolingTestResetEnergies.C",
    ),
    63: (
        "OneZoneFreefallTestInitialize.C",
        "Grid_OneZoneFreefallTestInitializeGrid.C",
    ),
    70: (
        "ConductionTestInitialize.C",
        "Grid_ConductionTestInitialize.C",
    ),
    71: (
        "ConductionTestInitialize.C",
        "Grid_ConductionTestInitialize.C",
    ),
    72: (
        "ConductionBubbleInitialize.C",
        "Grid_ConductionBubbleInitialize.C",
    ),
    73: (
        "ConductionCloudInitialize.C",
        "Grid_ConductionCloudInitialize.C",
    ),
    80: (
        "StratifiedMediumExplosionInitialize.C",
        "Grid_StratifiedMediumExplosionInitialize.C",
    ),
    90: (
        "TestStarParticleInitialize.C",
        "Grid_TestStarParticleInitializeGrid.C",
    ),
    91: (
        "TestDoubleStarParticleInitialize.C",
        "Grid_TestDoubleStarParticleInitializeGrid.C",
    ),
    101: (
        "hydro_rk/Collapse3DInitialize.C",
        "hydro_rk/Grid_Collapse3DInitializeGrid.C",
    ),
    102: (
        "hydro_rk/Collapse1DInitialize.C",
        "hydro_rk/Grid_Collapse1DInitializeGrid.C",
    ),
    103: (
        "MHDOrszagTangInit.C",
        "Grid_MHDOrszagTangInitGrid.C",
    ),
    104: (
        "MHDLoopInit.C",
        "Grid_MHDLoopInitGrid.C",
    ),
    106: (
        "hydro_rk/TurbulenceInitialize.C",
        "hydro_rk/Grid_TurbulenceInitializeGrid.C",
        "hydro_rk/Turbulence_Generator.C",
    ),
    107: (
        "PutSinkRestartInitialize.C",
        "Grid_PutSinkRestartInitialize.C",
    ),
    108: (
        "ClusterInitialize.C",
        "Grid_ClusterInitializeGrid.C",
    ),
    190: (
        "LightBosonInitialize.C",
        "Grid_LightBosonInitialize.C",
    ),
    191: (
        "FDMCollapse.C",
        "Grid_FDMCollapse.C",
    ),
    192: (
        "ParallelFDMCollapseInitialize.C",
        "Grid_ParallelFDMCollapseInitialize.C",
    ),
    200: (
        "hydro_rk/MHD1DTestInitialize.C",
        "hydro_rk/Grid_MHD1DTestInitializeGrid.C",
    ),
    201: (
        "hydro_rk/MHD2DTestInitialize.C",
        "hydro_rk/Grid_MHD2DTestInitializeGrid.C",
    ),
    202: (
        "hydro_rk/CollapseMHD3DInitialize.C",
        "hydro_rk/Grid_CollapseMHD3DInitializeGrid.C",
    ),
    203: (
        "hydro_rk/MHDTurbulenceInitialize.C",
        "hydro_rk/Grid_MHDTurbulenceInitializeGrid.C",
    ),
    204: (
        "hydro_rk/MHD3DTestInitialize.C",
        "hydro_rk/Grid_MHD3DTestInitializeGrid.C",
    ),
    207: (
        "hydro_rk/GalaxyDiskInitialize.C",
        "hydro_rk/Grid_GalaxyDiskInitializeGrid.C",
    ),
    208: (
        "hydro_rk/AGNDiskInitialize.C",
        "hydro_rk/Grid_AGNDiskInitializeGrid.C",
    ),
    209: (
        "hydro_rk/MHD1DTestWavesInitialize.C",
        "hydro_rk/Grid_MHD1DTestWavesInitializeGrid.C",
    ),
    210: (
        "hydro_rk/MHDDecayingRandomFieldInitialize.C",
        "hydro_rk/Grid_MHDDecayingRandomFieldInitializeGrid.C",
    ),
    250: (
        "CRShockTubesInitialize.C",
        "Grid_CRShockTubesInitializeGrid.C",
    ),
    251: (
        "CRTransportTestInitialize.C",
        "Grid_CRTransportTestInitialize.C",
    ),
    300: (
        "PoissonSolverTestInitialize.C",
        "Grid_PoissonSolverTestInitializeGrid.C",
    ),
    400: (
        "RadHydroConstTestInitialize.C",
        "Grid_RadHydroConstTestInitializeGrid.C",
    ),
    401: (
        "RadHydroStreamTestInitialize.C",
        "Grid_RadHydroStreamTestInitializeGrid.C",
    ),
    402: (
        "RadHydroPulseTestInitialize.C",
        "Grid_RadHydroPulseTestInitializeGrid.C",
    ),
    403: (
        "RadHydroGreyMarshakWaveInitialize.C",
        "Grid_RadHydroGreyMarshakWaveInitializeGrid.C",
    ),
    404: (
        "RadHydroRadShockInitialize.C",
        "Grid_RadHydroRadShockInitializeGrid.C",
    ),
    405: (
        "RadHydroRadShockInitialize.C",
        "Grid_RadHydroRadShockInitializeGrid.C",
    ),
    410: (
        "RHIonizationTestInitialize.C",
        "Grid_RHIonizationTestInitializeGrid.C",
    ),
    411: (
        "RHIonizationTestInitialize.C",
        "Grid_RHIonizationTestInitializeGrid.C",
    ),
    412: (
        "RHIonizationClumpInitialize.C",
        "Grid_RHIonizationClumpInitializeGrid.C",
    ),
    413: (
        "RHIonizationSteepInitialize.C",
        "Grid_RHIonizationSteepInitializeGrid.C",
    ),
    414: (
        "CosmoIonizationInitialize.C",
        "Grid_CosmoIonizationInitializeGrid.C",
    ),
    415: (
        "CosmoIonizationInitialize.C",
        "Grid_CosmoIonizationInitializeGrid.C",
    ),
    450: (
        "FSMultiSourceInitialize.C",
        "Grid_FSMultiSourceInitializeGrid.C",
    ),
    451: (
        "FSMultiSourceInitialize.C",
        "Grid_FSMultiSourceInitializeGrid.C",
    ),
    452: (
        "FSMultiSourceInitialize.C",
        "Grid_FSMultiSourceInitializeGrid.C",
    ),
    500: (
        "MHDBlastInitialize.C",
        "Grid_MHDBlastInitializeGrid.C",
    ),
    501: ( # Other removes
        "InitializeLocal.C",
        "ExternalBoundary_SetWengenCollidingFlowBoundary.C",
        "Grid_AddExternalAcceleration.C",
    ),
}


def files_for_problem_types(problem_types: list[int]) -> list[str]:
    files: list[str] = []
    for problem_type in problem_types:
        try:
            candidates = PROBLEM_TYPE_FILES[problem_type]
        except KeyError as error:
            supported = ", ".join(str(value) for value in sorted(PROBLEM_TYPE_FILES))
            raise SystemExit(
                f"No explicit file mapping for ProblemType {problem_type}. "
                f"Supported values: {supported}."
            ) from error
        files.extend(candidates)
    return list(dict.fromkeys(files))


def move_files(source_root: Path, trash_root: Path, files: list[str], apply: bool) -> None:
    for filename in files:
        source = source_root / filename
        destination = trash_root / filename
        if not source.exists():
            print(f"missing: {source}")
            continue
        if destination.exists():
            raise SystemExit(f"Refusing to overwrite existing file: {destination}")
        print(f"move: {source} -> {destination}")
        if apply:
            trash_root.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))


def restore_files(source_root: Path, trash_root: Path, files: list[str], apply: bool) -> None:
    for filename in files:
        source = trash_root / filename
        destination = source_root / filename
        if not source.exists():
            print(f"missing from trash: {source}")
            continue
        if destination.exists():
            raise SystemExit(f"Refusing to overwrite existing file: {destination}")
        print(f"restore: {source} -> {destination}")
        if apply:
            source_root.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))


def object_files_for_sources(files: list[str]) -> list[str]:
    return list(dict.fromkeys(
        str(Path(filename).with_suffix(".o"))
        for filename in files
        if filename.endswith(".C")
    ))


def remove_object_entries(manifest: Path, files: list[str], apply: bool) -> None:
    object_files = set(object_files_for_sources(files))
    if not manifest.exists():
        raise SystemExit(f"Manifest not found: {manifest}")

    original_lines = manifest.read_text().splitlines(keepends=True)
    kept_lines = []
    removed = []
    for line in original_lines:
        object_name = line.strip().rstrip("\\").strip()
        if object_name in object_files:
            removed.append(object_name)
        else:
            kept_lines.append(line)

    for object_name in sorted(removed):
        print(f"remove manifest entry: {object_name} from {manifest}")

    if apply and removed:
        manifest.write_text("".join(kept_lines))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preview or apply moves of explicitly mapped Enzo problem files."
    )
    parser.add_argument(
        "problem_types",
        metavar="PROBLEM_TYPE",
        nargs="+",
        type=int,
        help="ProblemType values to move or restore.",
    )
    parser.add_argument(
        "--enzo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "src" / "enzo",
        help="Enzo source directory (default: ../src/enzo relative to this script).",
    )
    parser.add_argument(
        "--trash-root",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "enzo-trash",
        help="Archive directory (default: workspace-level enzo-trash).",
    )
    parser.add_argument(
        "--restore",
        action="store_true",
        help="Restore files from enzo-trash instead of moving them there.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually perform the moves. Without this flag, only preview them.",
    )
    parser.add_argument(
        "--update-manifest",
        action="store_true",
        help="Remove mapped .o entries from Make.config.objects.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=None,
        help="Make.config.objects path (default: ../src/enzo/Make.config.objects).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    files = files_for_problem_types(args.problem_types)
    if args.update_manifest:
        manifest = args.manifest or args.enzo_root / "Make.config.objects"
        remove_object_entries(manifest, files, args.apply)
    if args.restore:
        restore_files(args.enzo_root, args.trash_root, files, args.apply)
    else:
        move_files(args.enzo_root, args.trash_root, files, args.apply)


if __name__ == "__main__":
    main()
