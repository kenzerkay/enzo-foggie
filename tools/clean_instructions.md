# Removing the Extra from ENZO 

## Installation 

*Conda install:*

cmake
gfortran
hdf5
openmpi
gxx_linux-64
zlib

*Install ENZO*
git clone https://github.com/kenzerkay/enzo-foggie.git
cd enzo-foggie/
git checkout 14a0706
./configure
cd src/enzo

*Change ENZO flags*

make grackle-yes
make uuid-no
make particles-64
make integers-64

*Small change to `phys_constants.h`*

#ifdef pi
  #undef pi
#endif

// This acts as a protective layer against standard library namespaces
namespace {
    const double enzo_pi = 3.14159265358979323846;
}
#define pi enzo_pi

***Installs Successfully From Here***

## Removing Items


### Move Mach Files 

`python move_mach_files.py` from the `tools` folder into `enzo_trash`. 

Run with `python move_mach_files.py --apply` to finalize changes

### Move Problem Type Files

**Make sure to `mkdir hydro_rk` in `enzo_trash`**

Constructed to move one problem type at a time but you can have it move all problem types with 
`python enzo-foggie/tools/move_problem_type_files.py $(python -c 'import ast; tree=ast.parse(open("enzo-foggie/tools/move_problem_type_files.py").read()); d=next(n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="PROBLEM_TYPE_FILES" for t in n.targets)); print(*sorted(ast.literal_eval(d.value)))')`

To finalize changes use: 

`python move_problem_type_files.py $(python -c 'import ast; tree=ast.parse(open("enzo-foggie/tools/move_problem_type_files.py").read()); d=next(n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="PROBLEM_TYPE_FILES" for t in n.targets)); print(*sorted(ast.literal_eval(d.value)))') --apply --update-manifest`

**`--update-manifest` is really important as this changes the `Make.config.objects` file. Without making these changes enzo will not build** 


* We Need to make a number of changes to other files in order for this to work: 
  * Comment out most of `InitializeNew.C` leaving only ProblemType = 31
  * Remove references to other problem types in `Grid_SetExternalBoundaryValues.C`
  * Remove references to other problem types in `EvolveHierarchy.C`
  * Remove references to other problems in `CallProblemSpecificRoutines.C`
  * Remove references to Problem 62 in `Grid_MultiSpeciesHandler.C`
  * Remove lines to 130-133 in `DebugTools.C`


### Moving UUID Files

**Make sure to `mkdir uuid` in `enzo_trash`**

`python move_uuid_files.py` from the `tools` folder into `enzo_trash`. 

Run with `python move_uuid_files.py --apply --update-manifest` to finalize changes


### Moving ZEUS Files

`python move_zeus_files.py` from the `tools` folder into `enzo_trash`. 

Run with `python move_zeus_files.py --apply --update-manifest` to finalize changes

* Need to comment out `if (HydroMethod == Zeus_Hydro)` Section at line 565. 

### Moving Radiative Transfer

`python move_radiative_transfer.py` from the `tools` folder into `enzo_trash`. 

Run with `python move_radiative_transfer.py --apply --update-manifest` to finalize changes

* May need to resotre these files:
  * RadiativeTransferParameters.h
  * RadiativeTransferSpectrumTable
  * RadiativeTransferHealpixRoutines64.h


* Need to Edit: 
  * Comment out 772-778 in enzo.C
  * Comment out 127-133 in ConvertParticles2ActiveParticles.C
  * Comment out 449-464 in EvolveLevel.C
  * Comment out 105-115 in OutputCoolingTimeOnly.C
  * Comment out 109-119 in OutputDustTemperatureOnly.C
  * Comment out 97-100 in ProjectToPlane2.C
  * Comment out 1250-1259 in WriteParameterFile.C

### Moving Active Particle

`python move_active_particle_files.py` from the `tools` folder into `enzo_trash`. 

Run with `python move_active_particle_files.py --apply --update-manifest` to finalize changes

May Need to Restore: 
  * ActiveParticle.h
  * ActiveParticle_SmartStar.h
  * ActiveParticle_GalaxyParticle.h

* Comment out: 
  * 682-684; 414; 282-283 in RebuildHierarchy.C
  * 1522-1530 in Read ParameterFile.C
  * 385-386 in PrepareDensityField.C
  * 92-111 in Grid_UpdateParticlePosition.C
  * 187 Grid_MoveAllParticles.C
  * 61; 69 Grid_InterpolateParticlePositons.C
  * 797 NewGridWrite.C
  * 115-119 Grid_DepositRefinementZone.C
  * 80 Grid_DepositParticlePositionsLocal.C
  * 378 Grid_DepoistParticlePositions.C
  * 74-46 Grid_CommunicationMoveGrid.C
  * 455 Grid_AccreteOntoAccretingParticle.C
  * 151 Grid_AccreteOntoSmartParticle.C
  * 767-770; 696-698; 438-439 EvolveLevel.C
  
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