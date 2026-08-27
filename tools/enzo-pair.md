conda install: 

cmake
gfortran
hdf5
openmpi
gxx_linux-64
zlib


make grackle-yes
make uuid-no
make particles-64
make integers-64


Made a small cange to `phys_constants.h`

#ifdef pi
  #undef pi
#endif

// This acts as a protective layer against standard library namespaces
namespace {
    const double enzo_pi = 3.14159265358979323846;
}
#define pi enzo_pi



conda install for analysis: 

yt
h5py


MHD2DTestGlobalData.h
SphericalInfall.h

I had to comment out a lot of things in `InitializeNew.C`
Remove references to other problem types in `Grid_SetExternalBoundaryValues.C`
Remove references to other problem types in `EvolveHierarchy.C`
REmove references to other problems in `CallProblemSpecificRoutines.C`
REmove references to Problem 62 in `Grid_MultiSpeciesHandler.C`
Remove lines to 130-133 in `DebugTools.C`

*(Done in Script now)*
Remove `InitializeLocal.C`
Remove `enzo-foggie/src/enzo/ExternalBoundary_SetWengenCollidingFlowBoundary.C`
Remove `enzo-foggie/src/enzo/hydro_rk/Turbulence_Generator.C` 
Remove `enzo-foggie/src/enzo/Grid_AddExternalAcceleration.C`




**Error State 1:**

Grid_AddExternalAcceleration.o: warning: relocation against `SphericalInfallFixedMass' in read-only section `.text'

EvolveHierarchy.o: in function `EvolveHierarchy(HierarchyEntry&, TopGridData&, ExternalBoundary*, ImplicitProblemABC*, LevelHierarchyEntry**, double)':
EvolveHierarchy.C:754:(.text+0x1742): undefined reference to `TestGravityCheckResults(LevelHierarchyEntry**)'
EvolveHierarchy.C:756:(.text+0x176a): undefined reference to `TestGravitySphereCheckResults(LevelHierarchyEntry**)'

Grid_SphericalInfallGetProfile.o: in function `grid::SphericalInfallGetProfile(long long, long long)':
Grid_SphericalInfallGetProfile.C:80:(.text+0x181): undefined referenceto `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:158:(.text+0xa7d): undefined reference to `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:173:(.text+0xbda): undefined reference to `SphericalInfallCenter'

CosmologySimulationInitialize.o: in function `CosmologySimulationInitialize(_IO_FILE*, _IO_FILE*, HierarchyEntry&, TopGridData&)':
CosmologySimulationInitialize.C:658:(.text+0x2da3): undefined reference to `grid::CosmologySimulationInitializeGrid(long long, double, double, double, char*, char*, char*, char**, char*, char*,char*, char*, char*, char**, char**, char**, long long, long long, double, double, double, double, double, double, double,double, double, long long, long long&, long long, double, long long, double*)'
CosmologySimulationInitialize.o: in function `CosmologySimulationReInitialize(HierarchyEntry*, TopGridData&)':
CosmologySimulationInitialize.C:1088:(.text+0x4b88): undefined reference to `grid::CosmologySimulationInitializeGrid(long long, double, double, double, char*, char*, char*, char**, char*, char*, char*, char*, char*, char**, char**, char**, long long, long long, double, double, double, double, double, double, double, double, double, long long, long long&, long long, double, long long, double*)'

DrivenFlowInitialize.o: in function `DrivenFlowInitialize(_IO_FILE*, _IO_FILE*, HierarchyEntry&, TopGridData&, long long)':
DrivenFlowInitialize.C:161:(.text+0x73d): undefined reference to `grid::DrivenFlowInitializeGrid(double, double, double, long long)'

Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:47:(.text+0x4a): undefined reference to`SphericalInfallFixedAcceleration'
Grid_AddExternalAcceleration.C:62:(.text+0x15a): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:66:(.text+0x1c9): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:69:(.text+0x22b): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2a6): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2ae): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.o:Grid_AddExternalAcceleration.C:76: more undefined references to `SphericalInfallCenter' follow
Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:85:(.text+0x329): undefined reference to `SphericalInfallFixedMass'

Grid_MultiSpeciesHandler.o: in function `grid::MultiSpeciesHandler()':
Grid_MultiSpeciesHandler.C:54:(.text+0x142): undefined reference to `grid::CoolingTestResetEnergies()'

hydro_rk/Turbulence_Generator.o: in function `Turbulence_Generator(double**, long long, long long, long long, long long, double, double, double, double**, double**, long long)':
hydro_rk/Turbulence_Generator.C:80:(.text+0x367): undefined reference to `Gaussian(double)'

warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status


Step Reremove ` CosmologySimulationInitialize.C`

**Error State 2:**


Grid_AddExternalAcceleration.o: warning: relocation against `SphericalInfallFixedMass' in read-only section `.text'

EvolveHierarchy.o: in function `EvolveHierarchy(HierarchyEntry&, TopGridData&, ExternalBoundary*, ImplicitProblemABC*, LevelHierarchyEntry**, double)':
EvolveHierarchy.C:754:(.text+0x1742): undefined reference to `TestGravityCheckResults(LevelHierarchyEntry**)'
EvolveHierarchy.C:756:(.text+0x176a): undefined reference to `TestGravitySphereCheckResults(LevelHierarchyEntry**)'

Grid_SphericalInfallGetProfile.o: in function `grid::SphericalInfallGetProfile(long long, long long)':
Grid_SphericalInfallGetProfile.C:80:(.text+0x181): undefined referenceto `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:158:(.text+0xa7d): undefined reference to `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:173:(.text+0xbda): undefined reference to `SphericalInfallCenter'

DrivenFlowInitialize.o: in function `DrivenFlowInitialize(_IO_FILE*, _IO_FILE*, HierarchyEntry&, TopGridData&, long long)':
DrivenFlowInitialize.C:161:(.text+0x73d): undefined reference to `grid::DrivenFlowInitializeGrid(double, double, double, long long)'

Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:47:(.text+0x4a): undefined reference to`SphericalInfallFixedAcceleration'
Grid_AddExternalAcceleration.C:62:(.text+0x15a): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:66:(.text+0x1c9): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:69:(.text+0x22b): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2a6): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2ae): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.o:Grid_AddExternalAcceleration.C:76: more undefined references to `SphericalInfallCenter' follow
Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:85:(.text+0x329): undefined reference to `SphericalInfallFixedMass'

Grid_MultiSpeciesHandler.o: in function `grid::MultiSpeciesHandler()':
Grid_MultiSpeciesHandler.C:54:(.text+0x142): undefined reference to `grid::CoolingTestResetEnergies()'

DebugTools.o: in function `TracerParticlesAddToRestart_DoIt(char*, HierarchyEntry*, TopGridData*)':
DebugTools.C:132:(.text+0x477): undefined reference to `RecursivelySetParticleCount(HierarchyEntry*, long long*)'

hydro_rk/Turbulence_Generator.o: in function `Turbulence_Generator(double**, long long, long long, long long, long long, double, double, double, double**, double**, long long)':
hydro_rk/Turbulence_Generator.C:80:(.text+0x367): undefined reference to `Gaussian(double)'
warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status


Step remove `DrivenFlowInitialize.C`

**Error State 3:** 

Grid_AddExternalAcceleration.o: warning: relocation against `SphericalInfallFixedMass' in read-only section `.text'

EvolveHierarchy.o: in function `EvolveHierarchy(HierarchyEntry&, TopGridData&, ExternalBoundary*, ImplicitProblemABC*, LevelHierarchyEntry**, double)':
EvolveHierarchy.C:503:(.text+0xf18): undefined reference to `Forcing'
EvolveHierarchy.C:754:(.text+0x1742): undefined reference to `TestGravityCheckResults(LevelHierarchyEntry**)'
EvolveHierarchy.C:756:(.text+0x176a): undefined reference to `TestGravitySphereCheckResults(LevelHierarchyEntry**)'

Grid_SphericalInfallGetProfile.o: in function `grid::SphericalInfallGetProfile(long long, long long)':
Grid_SphericalInfallGetProfile.C:80:(.text+0x181): undefined referenceto `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:158:(.text+0xa7d): undefined reference to `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:173:(.text+0xbda): undefined reference to `SphericalInfallCenter'

Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:47:(.text+0x4a): undefined reference to`SphericalInfallFixedAcceleration'
Grid_AddExternalAcceleration.C:62:(.text+0x15a): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:66:(.text+0x1c9): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:69:(.text+0x22b): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2a6): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2ae): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.o:Grid_AddExternalAcceleration.C:76: more undefined references to `SphericalInfallCenter' follow
Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:85:(.text+0x329): undefined reference to `SphericalInfallFixedMass'

Grid_MultiSpeciesHandler.o: in function `grid::MultiSpeciesHandler()':
Grid_MultiSpeciesHandler.C:54:(.text+0x142): undefined reference to `grid::CoolingTestResetEnergies()'

Group_ReadAllData.o: in function `Group_ReadAllData(char*, HierarchyEntry*, TopGridData&, ExternalBoundary*, double*, bool)':
Group_ReadAllData.C:157:(.text+0x1fa): undefined reference to `Forcing'
Group_WriteAllData.o: in function `Group_WriteAllData(char*, long long, HierarchyEntry*, TopGridData&, ExternalBoundary*, ImplicitProblemABC*, double, long long)':
Group_WriteAllData.C:659:(.text+0x13b5): undefined reference to `Forcing'
ReadAllData.o: in function `ReadAllData(char*, HierarchyEntry*, TopGridData&, ExternalBoundary*, double*)':
ReadAllData.C:125:(.text+0x20f): undefined reference to `Forcing'
ReadParameterFile.o: in function `ReadParameterFile(_IO_FILE*, TopGridData&, double*)':
ReadParameterFile.C:1562:(.text+0x909a): undefined reference to `Forcing'
WriteAllData.o: in function `WriteAllData(char*, long long, HierarchyEntry*, TopGridData&, ExternalBoundary*, ImplicitProblemABC*, double)':
WriteAllData.C:428:(.text+0xc87): undefined reference to `Forcing'
WriteParameterFile.o:WriteParameterFile.C:535: more undefined references to `Forcing' follow
DebugTools.o: in function `TracerParticlesAddToRestart_DoIt(char*, HierarchyEntry*, TopGridData*)':
DebugTools.C:132:(.text+0x477): undefined reference to `RecursivelySetParticleCount(HierarchyEntry*, long long*)'
Grid_FTStochasticForcing.o: in function `grid::FTStochasticForcing(long long)':
Grid_FTStochasticForcing.C:43:(.text+0x1d): undefined reference to `Forcing'
Grid_FTStochasticForcing.C:74:(.text+0x2c1): undefined reference to `Forcing'
Grid_FTStochasticForcing.C:75:(.text+0x2e1): undefined reference to `Forcing'
Grid_Phases.o: in function `grid::Phases()':
Grid_Phases.C:28:(.text+0x1e): undefined reference to `Forcing'
Grid_Phases.C:28:(.text+0x36): undefined reference to `Forcing'
Grid_Phases.o:Grid_Phases.C:29: more undefined references to `Forcing' follow
hydro_rk/Turbulence_Generator.o: in function `Turbulence_Generator(double**, long long, long long, long long, long long, double, double, double, double**, double**, long long)':
hydro_rk/Turbulence_Generator.C:80:(.text+0x367): undefined reference to `Gaussian(double)'
warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status

ReAdd `DrivenFlowInitalize.C`

**ErrorState4:**

Grid_AddExternalAcceleration.o: warning: relocation against `SphericalInfallFixedMass' in read-only section `.text'

EvolveHierarchy.o: in function `EvolveHierarchy(HierarchyEntry&, TopGridData&, ExternalBoundary*, ImplicitProblemABC*, LevelHierarchyEntry**, double)':
EvolveHierarchy.C:754:(.text+0x1742): undefined reference to `TestGravityCheckResults(LevelHierarchyEntry**)'
EvolveHierarchy.C:756:(.text+0x176a): undefined reference to `TestGravitySphereCheckResults(LevelHierarchyEntry**)'

DrivenFlowInitialize.o: in function `DrivenFlowInitialize(_IO_FILE*, _IO_FILE*, HierarchyEntry&, TopGridData&, long long)':
DrivenFlowInitialize.C:161:(.text+0x73d): undefined reference to `grid::DrivenFlowInitializeGrid(double, double, double, long long)'

Grid_SphericalInfallGetProfile.o: in function `grid::SphericalInfallGetProfile(long long, long long)':
Grid_SphericalInfallGetProfile.C:80:(.text+0x181): undefined referenceto `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:158:(.text+0xa7d): undefined reference to `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:173:(.text+0xbda): undefined reference to `SphericalInfallCenter'

Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:47:(.text+0x4a): undefined reference to`SphericalInfallFixedAcceleration'
Grid_AddExternalAcceleration.C:62:(.text+0x15a): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:66:(.text+0x1c9): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:69:(.text+0x22b): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2a6): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2ae): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.o:Grid_AddExternalAcceleration.C:76: more undefined references to `SphericalInfallCenter' follow
Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:85:(.text+0x329): undefined reference to `SphericalInfallFixedMass'

Grid_MultiSpeciesHandler.o: in function `grid::MultiSpeciesHandler()':
Grid_MultiSpeciesHandler.C:54:(.text+0x142): undefined reference to `grid::CoolingTestResetEnergies()'

DebugTools.o: in function `TracerParticlesAddToRestart_DoIt(char*, HierarchyEntry*, TopGridData*)':
DebugTools.C:132:(.text+0x477): undefined reference to `RecursivelySetParticleCount(HierarchyEntry*, long long*)'
hydro_rk/Turbulence_Generator.o: in function `Turbulence_Generator(double**, long long, long long, long long, long long, double, double, double, double**, double**, long long)':
hydro_rk/Turbulence_Generator.C:80:(.text+0x367): undefined reference to `Gaussian(double)'
warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status


**Error State 5:**

Grid_AddExternalAcceleration.o: warning: relocation against `SphericalInfallFixedMass' in read-only section `.text'

EvolveHierarchy.o: in function `EvolveHierarchy(HierarchyEntry&, TopGridData&, ExternalBoundary*, ImplicitProblemABC*, LevelHierarchyEntry**, double)':
EvolveHierarchy.C:754:(.text+0x1742): undefined reference to `TestGravityCheckResults(LevelHierarchyEntry**)'
EvolveHierarchy.C:756:(.text+0x176a): undefined reference to `TestGravitySphereCheckResults(LevelHierarchyEntry**)'

DrivenFlowInitialize.o: in function `DrivenFlowInitialize(_IO_FILE*, _IO_FILE*, HierarchyEntry&, TopGridData&, long long)':
DrivenFlowInitialize.C:161:(.text+0x73d): undefined reference to `grid::DrivenFlowInitializeGrid(double, double, double, long long)'

Grid_SphericalInfallGetProfile.o: in function `grid::SphericalInfallGetProfile(long long, long long)':
Grid_SphericalInfallGetProfile.C:80:(.text+0x181): undefined reference to `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:158:(.text+0xa7d): undefined reference to `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:173:(.text+0xbda): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:47:(.text+0x4a): undefined reference to `SphericalInfallFixedAcceleration'
Grid_AddExternalAcceleration.C:62:(.text+0x15a): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:66:(.text+0x1c9): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:69:(.text+0x22b): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2a6): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2ae): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.o:Grid_AddExternalAcceleration.C:76: more undefined references to `SphericalInfallCenter' follow
Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:85:(.text+0x329): undefined reference to `SphericalInfallFixedMass'

Grid_MultiSpeciesHandler.o: in function `grid::MultiSpeciesHandler()':
Grid_MultiSpeciesHandler.C:54:(.text+0x142): undefined reference to `grid::CoolingTestResetEnergies()'

DebugTools.o: in function `TracerParticlesAddToRestart_DoIt(char*, HierarchyEntry*, TopGridData*)':
DebugTools.C:132:(.text+0x477): undefined reference to `RecursivelySetParticleCount(HierarchyEntry*, long long*)'

hydro_rk/Turbulence_Generator.o: in function `Turbulence_Generator(double**, long long, long long, long long, long long, double, double, double, double**, double**, long long)':
hydro_rk/Turbulence_Generator.C:80:(.text+0x367): undefined reference to `Gaussian(double)'
warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status


**Error State 6:**

Grid_AddExternalAcceleration.o: warning: relocation against `SphericalInfallFixedMass' in read-only section `.text'

EvolveHierarchy.o: in function `EvolveHierarchy(HierarchyEntry&, TopGridData&, ExternalBoundary*, ImplicitProblemABC*, LevelHierarchyEntry**, double)':
EvolveHierarchy.C:754:(.text+0x1742): undefined reference to `TestGravityCheckResults(LevelHierarchyEntry**)'
EvolveHierarchy.C:756:(.text+0x176a): undefined reference to `TestGravitySphereCheckResults(LevelHierarchyEntry**)''

Grid_SphericalInfallGetProfile.o: in function `grid::SphericalInfallGetProfile(long long, long long)':
Grid_SphericalInfallGetProfile.C:80:(.text+0x181): undefined reference to `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:158:(.text+0xa7d): undefined reference to `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:173:(.text+0xbda): undefined reference to `SphericalInfallCenter'

Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:47:(.text+0x4a): undefined reference to `SphericalInfallFixedAcceleration'
Grid_AddExternalAcceleration.C:62:(.text+0x15a): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:66:(.text+0x1c9): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:69:(.text+0x22b): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2a6): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2ae): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.o:Grid_AddExternalAcceleration.C:76: more undefined references to `SphericalInfallCenter' follow
Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:85:(.text+0x329): undefined reference to `SphericalInfallFixedMass'

Grid_MultiSpeciesHandler.o: in function `grid::MultiSpeciesHandler()':
Grid_MultiSpeciesHandler.C:54:(.text+0x142): undefined reference to `grid::CoolingTestResetEnergies()'

DebugTools.o: in function `TracerParticlesAddToRestart_DoIt(char*, HierarchyEntry*, TopGridData*)':
DebugTools.C:132:(.text+0x477): undefined reference to `RecursivelySetParticleCount(HierarchyEntry*, long long*)'

hydro_rk/Turbulence_Generator.o: in function `Turbulence_Generator(double**, long long, long long, long long, long long, double, double, double, double**, double**, long long)':
hydro_rk/Turbulence_Generator.C:80:(.text+0x367): undefined reference to `Gaussian(double)'

warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status


**Error State 7:**

Grid_AddExternalAcceleration.o: warning: relocation against `SphericalInfallFixedMass' in read-only section `.text'

Grid_SphericalInfallGetProfile.o: in function `grid::SphericalInfallGetProfile(long long, long long)':
Grid_SphericalInfallGetProfile.C:80:(.text+0x181): undefined reference to `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:158:(.text+0xa7d): undefined reference to `SphericalInfallCenter'
Grid_SphericalInfallGetProfile.C:173:(.text+0xbda): undefined reference to `SphericalInfallCenter'

Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:47:(.text+0x4a): undefined reference to `SphericalInfallFixedAcceleration'
Grid_AddExternalAcceleration.C:62:(.text+0x15a): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:66:(.text+0x1c9): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:69:(.text+0x22b): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2a6): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2ae): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.o:Grid_AddExternalAcceleration.C:76: more undefined references to `SphericalInfallCenter' follow
Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:85:(.text+0x329): undefined reference to `SphericalInfallFixedMass'

Grid_MultiSpeciesHandler.o: in function `grid::MultiSpeciesHandler()':
Grid_MultiSpeciesHandler.C:54:(.text+0x142): undefined reference to `grid::CoolingTestResetEnergies()'

DebugTools.o: in function `TracerParticlesAddToRestart_DoIt(char*, HierarchyEntry*, TopGridData*)':
DebugTools.C:132:(.text+0x477): undefined reference to `RecursivelySetParticleCount(HierarchyEntry*, long long*)'

hydro_rk/Turbulence_Generator.o: in function `Turbulence_Generator(double**, long long, long long, long long, long long, double, double, double, double**, double**, long long)':
hydro_rk/Turbulence_Generator.C:80:(.text+0x367): undefined reference to `Gaussian(double)'


warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status

**Error State 8:**
Grid_AddExternalAcceleration.o: warning: relocation against `SphericalInfallFixedMass' in read-only section `.text'

CallProblemSpecificRoutines.o: in function `CallProblemSpecificRoutines(TopGridData*, HierarchyEntry*, long long, double*, double, long long, long long*)':
CallProblemSpecificRoutines.C:42:(.text+0xa0): undefined reference to `grid::SphericalInfallGetProfile(long long, long long)'

Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:47:(.text+0x4a): undefined reference to `SphericalInfallFixedAcceleration'
Grid_AddExternalAcceleration.C:62:(.text+0x15a): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:66:(.text+0x1c9): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:69:(.text+0x22b): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2a6): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2ae): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.o:Grid_AddExternalAcceleration.C:76: more undefined references to `SphericalInfallCenter' follow
Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:85:(.text+0x329): undefined reference to `SphericalInfallFixedMass'

Grid_MultiSpeciesHandler.o: in function `grid::MultiSpeciesHandler()':
Grid_MultiSpeciesHandler.C:54:(.text+0x142): undefined reference to `grid::CoolingTestResetEnergies()'
DebugTools.o: in function `TracerParticlesAddToRestart_DoIt(char*, HierarchyEntry*, TopGridData*)':

DebugTools.C:132:(.text+0x477): undefined reference to `RecursivelySetParticleCount(HierarchyEntry*, long long*)'

hydro_rk/Turbulence_Generator.o: in function `Turbulence_Generator(double**, long long, long long, long long, long long, double, double, double, double**, double**, long long)':
hydro_rk/Turbulence_Generator.C:80:(.text+0x367): undefined reference to `Gaussian(double)'

warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status


**Error State 8**

Grid_AddExternalAcceleration.o: warning: relocation against `SphericalInfallFixedMass' in read-only section `.text'

CallProblemSpecificRoutines.o: in function `CallProblemSpecificRoutines(TopGridData*, HierarchyEntry*, long long, double*, double, long long, long long*)':
CallProblemSpecificRoutines.C:42:(.text+0xa0): undefined reference to `grid::SphericalInfallGetProfile(long long, long long)'

Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:47:(.text+0x4a): undefined reference to `SphericalInfallFixedAcceleration'
Grid_AddExternalAcceleration.C:62:(.text+0x15a): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:66:(.text+0x1c9): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:69:(.text+0x22b): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2a6): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.C:76:(.text+0x2ae): undefined reference to `SphericalInfallCenter'
Grid_AddExternalAcceleration.o:Grid_AddExternalAcceleration.C:76: more undefined references to `SphericalInfallCenter' follow
Grid_AddExternalAcceleration.o: in function `grid::AddExternalAcceleration()':
Grid_AddExternalAcceleration.C:85:(.text+0x329): undefined reference to `SphericalInfallFixedMass'

Grid_MultiSpeciesHandler.o: in function `grid::MultiSpeciesHandler()':
Grid_MultiSpeciesHandler.C:54:(.text+0x142): undefined reference to `grid::CoolingTestResetEnergies()'

warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status


**Error State ?**

CallProblemSpecificRoutines.o: in function `CallProblemSpecificRoutines(TopGridData*, HierarchyEntry*, long long, double*, double, long long, long long*)':
CallProblemSpecificRoutines.C:42:(.text+0xa0): undefined reference to `grid::SphericalInfallGetProfile(long long, long long)'


Grid_MultiSpeciesHandler.o: in function `grid::MultiSpeciesHandler()':
Grid_MultiSpeciesHandler.C:54:(.text+0x142): undefined reference to `grid::CoolingTestResetEnergies()'
collect2: error: ld returned 1 exit status


## 2nd run 

Grid_Phases.o: warning: relocation against `Forcing' in read-only section `.text'

EvolveHierarchy.o: in function `EvolveHierarchy(HierarchyEntry&, TopGridData&, ExternalBoundary*, ImplicitProblemABC*, LevelHierarchyEntry**, double)':
EvolveHierarchy.C:503:(.text+0xf18): undefined reference to `Forcing'

Group_ReadAllData.o: in function `Group_ReadAllData(char*,HierarchyEntry*, TopGridData&, ExternalBoundary*, double*, bool)':
Group_ReadAllData.C:157:(.text+0x1fa): undefined reference to `Forcing'
Group_WriteAllData.o: in function `Group_WriteAllData(char*, long long, HierarchyEntry*, TopGridData&, ExternalBoundary*, ImplicitProblemABC*, double, long long)':
Group_WriteAllData.C:659:(.text+0x13b5): undefined reference to `Forcing'

ReadAllData.o: in function `ReadAllData(char*, HierarchyEntry*, TopGridData&, ExternalBoundary*, double*)':
ReadAllData.C:125:(.text+0x20f): undefined reference to `Forcing'

ReadParameterFile.o: in function `ReadParameterFile(_IO_FILE*, TopGridData&, double*)':
ReadParameterFile.C:1562:(.text+0x909a): undefined reference to `Forcing'
WriteAllData.o:WriteAllData.C:428: more undefined references to `Forcing' follow

warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status



## NOW REMOVING ZEUS FILES 

Grid_SolveHydroEquations.o: in function `grid::SolveHydroEquations(long long, long long, fluxes**, long long)':
Grid_SolveHydroEquations.C:566:(.text+0x2137): undefined reference to `grid::ZeusSolver(double*, long long, long long, double*, double*, double*, long long, long long, long long*, fluxes**, long long, long long*, long long, double)'


## NOW REMOVING RADIATIVE TRANSFER

enzo.o: in function `main':
enzo.C:773:(.text+0xd13): undefined reference to `RadiativeTransferInitialize(char*, HierarchyEntry&, TopGridData&, ExternalBoundary&, ImplicitProblemABC*&, LevelHierarchyEntry**)'

ConvertParticles2ActiveParticles.o: in function `ConvertParticles2ActiveParticles(char*, LevelHierarchyEntry**, HierarchyEntry*, TopGridData&, ExternalBoundary&, ImplicitProblemABC*)':
ConvertParticles2ActiveParticles.C:128:(.text+0x322): undefined reference to `RadiativeTransferInitialize(char*, HierarchyEntry&, TopGridData&, ExternalBoundary&, ImplicitProblemABC*&, LevelHierarchyEntry**)'


EvolveLevel.o: in function `EvolveLevel(TopGridData*, LevelHierarchyEntry**, long long, double, ExternalBoundary*, ImplicitProblemABC*, double, SiblingGridList**)':
EvolveLevel.C:453:(.text+0x770): undefined reference to `RadiativeTransferPrepare(LevelHierarchyEntry**, long long, TopGridData*, Star*&, double)'
EvolveLevel.C:455:(.text+0x79e): undefined reference to `RadiativeTransferCallFLD(LevelHierarchyEntry**, long long, TopGridData*, Star*, ImplicitProblemABC*)'

OutputCoolingTimeOnly.o: in function `OutputCoolingTimeOnly(char*, LevelHierarchyEntry**, HierarchyEntry*, TopGridData&, ExternalBoundary&, ImplicitProblemABC*)':
OutputCoolingTimeOnly.C:112:(.text+0x2d3): undefined reference to `RadiativeTransferReadParameters(_IO_FILE*)'

OutputDustTemperatureOnly.o: in function `OutputDustTemperatureOnly(char*, LevelHierarchyEntry**, HierarchyEntry*, TopGridData&, ExternalBoundary&, ImplicitProblemABC*)':
OutputDustTemperatureOnly.C:116:(.text+0x2fa): undefined reference to `RadiativeTransferReadParameters(_IO_FILE*)'

ProjectToPlane2.o: in function `ProjectToPlane2(char*, HierarchyEntry&, TopGridData&, LevelHierarchyEntry**, long long*, long long*, double*, double*, long long, long long, char*, long long, ImplicitProblemABC*, ExternalBoundary*)':
ProjectToPlane2.C:98:(.text+0x76): undefined reference to `RadiativeTransferInitialize(char*, HierarchyEntry&, TopGridData&, ExternalBoundary&, ImplicitProblemABC*&, LevelHierarchyEntry**)'

WriteParameterFile.o: in function `WriteParameterFile(_IO_FILE*, TopGridData&, char*)':
WriteParameterFile.C:1251:(.text+0x713e): undefined reference to `RadiativeTransferWriteParameters(_IO_FILE*)'

EvolvePhotons.o: in function `EvolvePhotons(TopGridData*, LevelHierarchyEntry**, Star*&, double, long long, long long)':
EvolvePhotons.C:228:(.text+0x46b): undefined reference to `RadiativeTransferComputeTimestep(LevelHierarchyEntry**, TopGridData*, double, long long)'
EvolvePhotons.C:585:(.text+0x14f5): undefined reference to `RadiativeTransferLoadBalanceRevert(HierarchyEntry***, long long*)'

Grid_RegridPausedPhotonPackage.o: in function `grid::RegridPausedPhotonPackage(PhotonPackageEntry**, grid*, grid**, long long&, long long&, double const*, double)':
Grid_RegridPausedPhotonPackage.C:61:(.text+0x16e): undefined reference to `pix2vec_nest64'
Grid_RegridPausedPhotonPackage.C:97:(.text+0x452): undefined reference to `vec2pix_nest64'
Grid_RegridPausedPhotonPackage.C:99:(.text+0x48a): undefined reference to `pix2vec_nest64'

Grid_Shine.o: in function `grid::Shine(RadiationSourceEntry*)':
Grid_Shine.C:199:(.text+0x7bf): undefined reference to `pix2vec_nest64'
Grid_Shine.C:237:(.text+0xa5a): undefined reference to `pix2vec_nest64'

Grid_TransportPhotonPackages.o: in function `PhotonPackageEntry::PrintInfo()':
PhotonPackage.h:56:(.text._ZN18PhotonPackageEntry9PrintInfoEv[_ZN18PhotonPackageEntry9PrintInfoEv]+0x31): undefined reference to `pix2vec_nest64'

Grid_WalkPhotonPackage.o: in function `grid::WalkPhotonPackage(PhotonPackageEntry**, grid**, grid*, grid*, grid**, long long, long long&, long long&, long long&, double, double, long long, double)':
Grid_WalkPhotonPackage.C:144:(.text+0x4b4): undefined reference to `pix2vec_nest64'
Grid_WalkPhotonPackage.C:587:(.text+0x1f0e): undefined reference to `grid::RadiativeTransferIonization(PhotonPackageEntry**, double*, long long, long long, double, double, double*, double, long long const*, long long)'
Grid_WalkPhotonPackage.C:615:(.text+0x20ba): undefined reference to `grid::RadiativeTransferLWShielding(PhotonPackageEntry**, double&, double, double, long long, double, long long, long long, double)'
Grid_WalkPhotonPackage.C:626:(.text+0x216f): undefined reference to `grid::RadiativeTransferLW(PhotonPackageEntry**, double&, long long, double, double, double, long long)'
Grid_WalkPhotonPackage.C:648:(.text+0x2292): undefined reference to `grid::RadiativeTransferH2II(PhotonPackageEntry**, long long, double, double, double, long long)'
Grid_WalkPhotonPackage.C:669:(.text+0x23a8): undefined reference to `grid::RadiativeTransferIR(PhotonPackageEntry**, double&, long long, double, double, double*, double, long long, long long)'
Grid_WalkPhotonPackage.C:685:(.text+0x24a0): undefined reference to `grid::RadiativeTransferH2II(PhotonPackageEntry**, long long, double, double, double, long long)'
Grid_WalkPhotonPackage.C:728:(.text+0x2849): undefined reference to `grid::RadiativeTransferXRays(PhotonPackageEntry**, double*, long long, long long, double, double, double, double, double*, double*, double, long long const*, long long)'
Grid_WalkPhotonPackage.C:743:(.text+0x2989): undefined reference to `grid::RadiativeTransferComptonHeating(PhotonPackageEntry**, double*, long long, double, double, long long, double, double, double, long long)'



*Error State 2*

enzo.o: in function `main':
enzo.C:773:(.text+0xd13): undefined reference to `RadiativeTransferInitialize(char*, HierarchyEntry&, TopGridData&, ExternalBoundary&, ImplicitProblemABC*&, LevelHierarchyEntry**)'

ConvertParticles2ActiveParticles.o: in function `ConvertParticles2ActiveParticles(char*, LevelHierarchyEntry**, HierarchyEntry*, TopGridData&, ExternalBoundary&, ImplicitProblemABC*)':
ConvertParticles2ActiveParticles.C:128:(.text+0x322): undefined reference to `RadiativeTransferInitialize(char*, HierarchyEntry&, TopGridData&, ExternalBoundary&, ImplicitProblemABC*&, LevelHierarchyEntry**)'

EvolveLevel.o: in function `EvolveLevel(TopGridData*, LevelHierarchyEntry**, long long, double, ExternalBoundary*, ImplicitProblemABC*, double, SiblingGridList**)':
EvolveLevel.C:453:(.text+0x770): undefined reference to `RadiativeTransferPrepare(LevelHierarchyEntry**, long long, TopGridData*, Star*&, double)'
EvolveLevel.C:455:(.text+0x79e): undefined reference to `RadiativeTransferCallFLD(LevelHierarchyEntry**, long long, TopGridData*, Star*, ImplicitProblemABC*)'
EvolveLevel.C:461:(.text+0x80b): undefined reference to `EvolvePhotons(TopGridData*, LevelHierarchyEntry**, Star*&, double, long long, long long)'

OutputCoolingTimeOnly.o: in function `OutputCoolingTimeOnly(char*, LevelHierarchyEntry**, HierarchyEntry*, TopGridData&, ExternalBoundary&, ImplicitProblemABC*)':
OutputCoolingTimeOnly.C:112:(.text+0x2d3): undefined reference to `RadiativeTransferReadParameters(_IO_FILE*)'

OutputDustTemperatureOnly.o: in function `OutputDustTemperatureOnly(char*, LevelHierarchyEntry**, HierarchyEntry*, TopGridData&, ExternalBoundary&, ImplicitProblemABC*)':
OutputDustTemperatureOnly.C:116:(.text+0x2fa): undefined reference to `RadiativeTransferReadParameters(_IO_FILE*)'

ProjectToPlane2.o: in function `ProjectToPlane2(char*, HierarchyEntry&, TopGridData&, LevelHierarchyEntry**, long long*, long long*, double*, double*, long long, long long, char*, long long, ImplicitProblemABC*, ExternalBoundary*)':
ProjectToPlane2.C:98:(.text+0x76): undefined reference to `RadiativeTransferInitialize(char*, HierarchyEntry&, TopGridData&, ExternalBoundary&, ImplicitProblemABC*&, LevelHierarchyEntry**)'

WriteParameterFile.o: in function `WriteParameterFile(_IO_FILE*, TopGridData&, char*)':
WriteParameterFile.C:1251:(.text+0x713e): undefined reference to `RadiativeTransferWriteParameters(_IO_FILE*)'

Grid_Shine.o: in function `grid::Shine(RadiationSourceEntry*)':
Grid_Shine.C:199:(.text+0x7bf): undefined reference to `pix2vec_nest64'
Grid_Shine.C:237:(.text+0xa5a): undefined reference to `pix2vec_nest64'

Grid_TransportPhotonPackages.o: in function `grid::TransportPhotonPackages(long long, long long, ListOfPhotonsToMove**, long long, grid**, long long, grid*, grid*)':
Grid_TransportPhotonPackages.C:180:(.text+0x79e): undefined reference to `grid::WalkPhotonPackage(PhotonPackageEntry**, grid**, grid*, grid*, grid**, long long, long long&, long long&, long long&, double, double, long long, double)'
Grid_TransportPhotonPackages.C:204:(.text+0x852): undefined reference to `grid::RegridPausedPhotonPackage(PhotonPackageEntry**, grid*, grid**, long long&, long long&, double const*, double)'
Grid_TransportPhotonPackages.o: in function `PhotonPackageEntry::PrintInfo()':

PhotonPackage.h:56:(.text._ZN18PhotonPackageEntry9PrintInfoEv[_ZN18PhotonPackageEntry9PrintInfoEv]+0x31): undefined reference to `pix2vec_nest64'

RestartPhotons.o: in function `RestartPhotons(TopGridData*, LevelHierarchyEntry**, long long, Star*)':
RestartPhotons.C:106:(.text+0x236): undefined reference to `EvolvePhotons(TopGridData*, LevelHierarchyEntry**, Star*&, double, long long, long long)'

collect2: error: ld returned 1 exit status


**Error State 3**

enzo.o: in function `main':
enzo.C:773:(.text+0xd13): undefined reference to `RadiativeTransferInitialize(char*, HierarchyEntry&, TopGridData&, ExternalBoundary&, ImplicitProblemABC*&, LevelHierarchyEntry**)'


ConvertParticles2ActiveParticles.o: in function `ConvertParticles2ActiveParticles(char*, LevelHierarchyEntry**, HierarchyEntry*, TopGridData&, ExternalBoundary&, ImplicitProblemABC*)':
ConvertParticles2ActiveParticles.C:128:(.text+0x322): undefined reference to `RadiativeTransferInitialize(char*, HierarchyEntry&, TopGridData&, ExternalBoundary&, ImplicitProblemABC*&, LevelHierarchyEntry**)'


EvolveLevel.o: in function `EvolveLevel(TopGridData*, LevelHierarchyEntry**, long long, double, ExternalBoundary*, ImplicitProblemABC*, double, SiblingGridList**)':
EvolveLevel.C:453:(.text+0x770): undefined reference to `RadiativeTransferPrepare(LevelHierarchyEntry**, long long, TopGridData*, Star*&, double)'
EvolveLevel.C:455:(.text+0x79e): undefined reference to `RadiativeTransferCallFLD(LevelHierarchyEntry**, long long, TopGridData*, Star*, ImplicitProblemABC*)'
EvolveLevel.C:461:(.text+0x80b): undefined reference to `EvolvePhotons(TopGridData*, LevelHierarchyEntry**, Star*&, double, long long, long long)'

OutputCoolingTimeOnly.o: in function `OutputCoolingTimeOnly(char*, LevelHierarchyEntry**, HierarchyEntry*, TopGridData&, ExternalBoundary&, ImplicitProblemABC*)':
OutputCoolingTimeOnly.C:112:(.text+0x2d3): undefined reference to `RadiativeTransferReadParameters(_IO_FILE*)'

OutputDustTemperatureOnly.o: in function `OutputDustTemperatureOnly(char*, LevelHierarchyEntry**, HierarchyEntry*, TopGridData&, ExternalBoundary&, ImplicitProblemABC*)':
OutputDustTemperatureOnly.C:116:(.text+0x2fa): undefined reference to `RadiativeTransferReadParameters(_IO_FILE*)'

ProjectToPlane2.o: in function `ProjectToPlane2(char*, HierarchyEntry&, TopGridData&, LevelHierarchyEntry**, long long*, long long*, double*, double*, long long, long long, char*, long long, ImplicitProblemABC*, ExternalBoundary*)':
ProjectToPlane2.C:98:(.text+0x76): undefined reference to `RadiativeTransferInitialize(char*, HierarchyEntry&, TopGridData&, ExternalBoundary&, ImplicitProblemABC*&, LevelHierarchyEntry**)'

WriteParameterFile.o: in function `WriteParameterFile(_IO_FILE*, TopGridData&, char*)':
WriteParameterFile.C:1251:(.text+0x713e): undefined reference to `RadiativeTransferWriteParameters(_IO_FILE*)'
collect2: error: ld returned 1 exit status




#### 

DetermineSEDParameters.o: warning: relocation against `_ZN28ActiveParticleType_SmartStar12RadiationSEDE' in read-only section `.text'

CommunicationCombineGrids.o: in function `CommunicationCombineGrids(HierarchyEntry*, HierarchyEntry**, double, long long)':
CommunicationCombineGrids.C:146:(.text+0x98e): undefined reference to `grid::CommunicationSendActiveParticles(grid*, long long, bool)'

CommunicationCollectParticles.o: in function `CommunicationCollectParticles(LevelHierarchyEntry**, long long, bool, bool, bool, long long)':
CommunicationCollectParticles.C:201:(.text+0x5bb): undefined reference to `grid::TransferSubgridActiveParticles(grid**, long long, long long*&, long long, long long, ActiveParticleList<ActiveParticleType>&, bool, bool, long long, long long, long long)'
CommunicationCollectParticles.C:243:(.text+0x8cb): undefined reference to `grid::TransferSubgridActiveParticles(grid**, long long, long long*&, long long, long long, ActiveParticleList<ActiveParticleType>&, bool, bool, long long, long long, long long)'
CommunicationCollectParticles.C:292:(.text+0xaca): undefined reference to `CommunicationShareActiveParticles(long long*, ActiveParticleList<ActiveParticleType>&, long long&, ActiveParticleList<ActiveParticleType>&)'
CommunicationCollectParticles.C:368:(.text+0xdfb): undefined reference to `grid::TransferSubgridActiveParticles(grid**, long long, long long*&, long long, long long, ActiveParticleList<ActiveParticleType>&, bool, bool, long long, long long, long long)'
CommunicationCollectParticles.C:543:(.text+0x13fa): undefined reference to `grid::CollectActiveParticles(long long, long long*&, long long&, long long&, ActiveParticleList<ActiveParticleType>&, long long)'
CommunicationCollectParticles.C:555:(.text+0x14a6): undefined reference to `CommunicationShareActiveParticles(long long*, ActiveParticleList<ActiveParticleType>&, long long&, ActiveParticleList<ActiveParticleType>&)'
CommunicationCollectParticles.C:628:(.text+0x1782): undefined reference to `grid::CollectActiveParticles(long long, long long*&, long long&, long long&, ActiveParticleList<ActiveParticleType>&, long long)'

CommunicationReceiveHandler.o: in function `CommunicationReceiveHandler(fluxes***, long long*, long long, TopGridData*)':
CommunicationReceiveHandler.C:304:(.text+0xc2e): undefined reference to `grid::CommunicationSendActiveParticles(grid*, long long, bool)'

CommunicationSyncNumberOfParticles.o: in function `CommunicationSyncNumberOfParticles(HierarchyEntry**, long long)':
CommunicationSyncNumberOfParticles.C:50:(.text+0x1a6): undefined reference to `grid::ReturnNumberOfActiveParticlesOfThisType(long long)'

CommunicationTransferSubgridParticles.o: in function `CommunicationTransferSubgridParticles(LevelHierarchyEntry**, TopGridData*, long long)':
CommunicationTransferSubgridParticles.C:165:(.text+0x4c2): undefined reference to `grid::TransferSubgridActiveParticles(grid**, long long, long long*&, long long, long long, ActiveParticleList<ActiveParticleType>&, bool, bool, long long, long long, long long)'
CommunicationTransferSubgridParticles.C:199:(.text+0x765): undefined reference to `grid::TransferSubgridActiveParticles(grid**, long long, long long*&, long long, long long, ActiveParticleList<ActiveParticleType>&, bool, bool, long long, long long, long long)'
CommunicationTransferSubgridParticles.C:217:(.text+0x84e): undefined reference to `CommunicationShareActiveParticles(long long*, ActiveParticleList<ActiveParticleType>&, long long&, ActiveParticleList<ActiveParticleType>&)'
CommunicationTransferSubgridParticles.C:303:(.text+0xb74): undefined reference to `grid::TransferSubgridActiveParticles(grid**, long long, long long*&, long long, long long, ActiveParticleList<ActiveParticleType>&, bool, bool, long long, long long, long long)'

DetermineSEDParameters.o: in function `DetermineSEDParameters(ActiveParticleType_SmartStar*, double, double)':
DetermineSEDParameters.C:135:(.text+0x29a): undefined reference to `ActiveParticleType_SmartStar::RadiationEnergyBins'
DetermineSEDParameters.C:136:(.text+0x2b4): undefined reference to `ActiveParticleType_SmartStar::RadiationSED'
DetermineSEDParameters.C:177:(.text+0x3d2): undefined reference to `ActiveParticleType_SmartStar::RadiationLifetime'
DetermineSEDParameters.C:178:(.text+0x3e2): undefined reference to `ActiveParticleType_SmartStar::LuminosityPerSolarMass'
DetermineSEDParameters.C:180:(.text+0x3f3): undefined reference to `ActiveParticleType_SmartStar::RadiationEnergyBins'
DetermineSEDParameters.C:181:(.text+0x421): undefined reference to `ActiveParticleType_SmartStar::RadiationSED'
DetermineSEDParameters.C:190:(.text+0x499): undefined reference to `ActiveParticleType_SmartStar::RadiationLifetime'
DetermineSEDParameters.C:191:(.text+0x4a9): undefined reference to `ActiveParticleType_SmartStar::LuminosityPerSolarMass'
DetermineSEDParameters.C:194:(.text+0x4ba): undefined reference to `ActiveParticleType_SmartStar::RadiationEnergyBins'
DetermineSEDParameters.C:195:(.text+0x4e8): undefined reference to `ActiveParticleType_SmartStar::RadiationSED'
DetermineSEDParameters.C:207:(.text+0x565): undefined reference to `ActiveParticleType_SmartStar::RadiationLifetime'
DetermineSEDParameters.C:216:(.text+0x6cf): undefined reference to `ActiveParticleType_SmartStar::LuminosityPerSolarMass'
DetermineSEDParameters.C:230:(.text+0x82f): undefined reference to `ActiveParticleType_SmartStar::LuminosityPerSolarMass'
DetermineSEDParameters.C:240:(.text+0x8a0): undefined reference to `ActiveParticleType_SmartStar::LuminosityPerSolarMass'
DetermineSEDParameters.C:240:(.text+0x8b0): undefined reference to `ActiveParticleType_SmartStar::LuminosityPerSolarMass'
DetermineSEDParameters.C:244:(.text+0x8c1): undefined reference to `ActiveParticleType_SmartStar::RadiationEnergyBins'
DetermineSEDParameters.C:245:(.text+0x8f7): undefined reference to `ActiveParticleType_SmartStar::RadiationSED'

EvolveLevel.o: in function `EvolveLevel(TopGridData*, LevelHierarchyEntry**, long long, double, ExternalBoundary*, ImplicitProblemABC*, double, SiblingGridList**)':
EvolveLevel.C:438:(.text+0x6bf): undefined reference to `ActiveParticleInitialize(HierarchyEntry**, TopGridData*, long long, LevelHierarchyEntry**, long long)'
EvolveLevel.C:697:(.text+0x1189): undefined reference to `grid::ActiveParticleHandler(HierarchyEntry*, long long, double, long long&)'
EvolveLevel.C:768:(.text+0x14f5): undefined reference to `ActiveParticleFinalize(HierarchyEntry**, TopGridData*, long long, LevelHierarchyEntry**, long long, long long*)'

Grid_AccreteOntoAccretingParticle.o: in function `grid::AccreteOntoAccretingParticle(ActiveParticleType*, double, double*)':
Grid_AccreteOntoAccretingParticle.C:455:(.text+0x2abb): undefined reference to `ActiveParticleType::SetVelocity(double*)'

Grid_AccreteOntoSmartStarParticle.o: in function `grid::AccreteOntoSmartStarParticle(ActiveParticleType*, double, double*)':
Grid_AccreteOntoSmartStarParticle.C:151:(.text+0x7eb): undefined reference to `ActiveParticleType::SetVelocity(double*)'

Grid_ApplySmartStarParticleFeedback.o: in function `grid::ApplySmartStarParticleFeedback(ActiveParticleType**)':
Grid_ApplySmartStarParticleFeedback.C:334:(.text+0x1c90): undefined reference to `ActiveParticleType_SmartStar::EjectedMassThreshold'
Grid_ApplySmartStarParticleFeedback.C:337:(.text+0x1d0e): undefined reference to `ActiveParticleType_SmartStar::EjectedMassThreshold'
Grid_ApplySmartStarParticleFeedback.C:338:(.text+0x1d1c): undefined reference to `ActiveParticleType_SmartStar::EjectedMassThreshold'
Grid_ApplySmartStarParticleFeedback.C:372:(.text+0x200b): undefined reference to `ActiveParticleType_SmartStar::EjectedMassThreshold'
Grid_ApplySmartStarParticleFeedback.C:386:(.text+0x211e): undefined reference to `ActiveParticleType_SmartStar::CalculateAccretedAngularMomentum()'
Grid_ApplySmartStarParticleFeedback.C:659:(.text+0x3c6b): undefined reference to `ActiveParticleType_SmartStar::EjectedMassThreshold'
Grid_ApplySmartStarParticleFeedback.C:660:(.text+0x3c73): undefined reference to `ActiveParticleType_SmartStar::EjectedMassThreshold'
Grid_ApplySmartStarParticleFeedback.C:661:(.text+0x3c91): undefined reference to `ActiveParticleType_SmartStar::EjectedMassThreshold'
Grid_ApplySmartStarParticleFeedback.C:664:(.text+0x3ccb): undefined reference to `ActiveParticleType_SmartStar::EjectedMassThreshold'

Grid_CommunicationMoveGrid.o: in function `grid::CommunicationMoveGrid(long long, long long, long long, long long)':
Grid_CommunicationMoveGrid.C:75:(.text+0x1ef): undefined reference to `grid::CommunicationSendActiveParticles(grid*, long long, bool)'

Grid_DepositParticlePositions.o: in function `grid::DepositParticlePositions(grid*, double, long long)':
Grid_DepositParticlePositions.C:378:(.text+0x12a5): undefined reference to `grid::GetActiveParticlePosition(double**)'

Grid_DepositParticlePositionsLocal.o: in function `grid::DepositParticlePositionsLocal(double, long long, bool)':
Grid_DepositParticlePositionsLocal.C:80:(.text+0x295): undefined reference to `grid::GetActiveParticlePosition(double**)'

Grid_DepositRefinementZone.o: in function `grid::DepositRefinementZone(long long, double*, double)':
Grid_DepositRefinementZone.C:115:(.text+0x71b): undefined reference to `calc_dist2(double, double, double, double, double, double, double*)'

New_Grid_WriteGrid.o: in function `grid::Group_WriteGrid(_IO_FILE*, char*, long long, long long, long long)':
New_Grid_WriteGrid.C:797:(.text+0x327e): undefined reference to `grid::SortActiveParticlesByNumber()'

Grid_InterpolateParticlePositions.o: in function `grid::InterpolateParticlePositions(grid*, long long)':
Grid_InterpolateParticlePositions.C:61:(.text+0x200): undefined reference to `grid::GetActiveParticlePosition(double**)'
Grid_InterpolateParticlePositions.C:69:(.text+0x29e): undefined reference to `ActiveParticleResetAccelerations(double*)'

Grid_MoveAllParticles.o: in function `grid::MoveAllParticles(long long, grid**)':
Grid_MoveAllParticles.C:187:(.text+0xebe): undefined reference to `grid::AddActiveParticles(ActiveParticleList<ActiveParticleType>&, long long, long long)'

Grid_UpdateParticlePosition.o: in function `grid::UpdateParticlePosition(double, long long)':
Grid_UpdateParticlePosition.C:103:(.text+0x35b): undefined reference to `ActiveParticleType::SetPosition(double*)'
Grid_UpdateParticlePosition.C:109:(.text+0x3db): undefined reference to `ActiveParticleType::SetPositionPeriod(double*)'

Grid_UpdateParticleVelocity.o: in function `grid::UpdateParticleVelocity(double)':
Grid_UpdateParticleVelocity.C:180:(.text+0x5c6): undefined reference to `ActiveParticleType::SetVelocity(double*)'
Grid_UpdateParticleVelocity.C:193:(.text+0x6bd): undefined reference to `ActiveParticleType::SetVelocity(double*)'

PrepareDensityField.o: in function `PrepareDensityField(LevelHierarchyEntry**, long long, TopGridData*, double, SiblingGridList**)':
PrepareDensityField.C:385:(.text+0x8f4): undefined reference to `ActiveParticleDepositMass(HierarchyEntry**, TopGridData*, long long, LevelHierarchyEntry**, long long)'

ReadParameterFile.o: in function `ReadParameterFile(_IO_FILE*, TopGridData&, double*)':
ReadParameterFile.C:1527:(.text+0x8d8b): undefined reference to `EnableActiveParticleType(char*)'

RebuildHierarchy.o: in function `RebuildHierarchy(TopGridData*, LevelHierarchyEntry**, long long)':
RebuildHierarchy.C:282:(.text+0x7e0): undefined reference to `CommunicationTransferActiveParticles(grid**, long long, long long*)'
RebuildHierarchy.C:414:(.text+0xba1): undefined reference to `DepositActiveParticleMassFlaggingField(LevelHierarchyEntry**, long long, long long*)'
RebuildHierarchy.C:682:(.text+0x18de): undefined reference to `grid::MoveSubgridActiveParticles(long long, grid**, long long)'


/home/kenzerkay/miniforge3/envs/enzo_pair/bin/x86_64-conda-linux-gnu-ld: Grid_UpdateParticleVelocity.o: in function `grid::UpdateParticleVelocity(double)':
/home/kenzerkay/pair_down_ENZO/enzo-foggie/src/enzo/Grid_UpdateParticleVelocity.C:180:(.text+0x5c6): undefined reference to `ActiveParticleType::SetVelocity(double*)'
/home/kenzerkay/miniforge3/envs/enzo_pair/bin/x86_64-conda-linux-gnu-ld: /home/kenzerkay/pair_down_ENZO/enzo-foggie/src/enzo/Grid_UpdateParticleVelocity.C:193:(.text+0x6bd): undefined reference to `ActiveParticleType::SetVelocity(double*)'
collect2: error: ld returned 1 exit status