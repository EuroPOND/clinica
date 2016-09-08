# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# compile CXX with clang-omp++
CXX_FLAGS =    -fopenmp  

CXX_DEFINES = -DITK_IO_FACTORY_REGISTER_MANAGER -DvtkDomainsChemistry_AUTOINIT="1(vtkDomainsChemistryOpenGL2)" -DvtkRenderingContext2D_AUTOINIT="1(vtkRenderingContextOpenGL2)" -DvtkRenderingCore_AUTOINIT="3(vtkInteractionStyle,vtkRenderingFreeType,vtkRenderingOpenGL2)" -DvtkRenderingVolume_AUTOINIT="1(vtkRenderingVolumeOpenGL2)"

CXX_INCLUDES = -I/Users/pietro.gori/Softwares/clinica/clinica/lib/weighted_prototypes_lib/cpp_code/bin/ITKIOFactoryRegistration -I/Users/pietro.gori/Softwares/ITKb/fftw/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/Watersheds/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/Voronoi/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Video/IO/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Video/Filtering/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Video/Core/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Bridge/VTK/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Core/TestKernel/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/SpatialFunction/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Registration/RegistrationMethodsv4/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/RegionGrowing/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/QuadEdgeMeshFiltering/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Numerics/NeuralNetworks/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Registration/Metricsv4/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Numerics/Optimizersv4/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/MarkovRandomFieldsClassifiers/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/LevelSetsv4/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/LabelVoting/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/KLMRegionGrowing/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/ImageNoise/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/ImageFusion/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/VTK/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/TransformMatlab/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/TransformInsightLegacy/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/TransformHDF5/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/TransformBase/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/Stimulate/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/Siemens/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/RAW/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/PNG/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/PNG/src -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/PNG/src -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/NRRD/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/NrrdIO/src/NrrdIO -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/NrrdIO/src/NrrdIO -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/NIFTI/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/Meta/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/Mesh/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/MRC/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/LSM/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/TIFF/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/TIFF/src -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/TIFF/src/itktiff -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/TIFF/src -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/JPEG/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/JPEG/src -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/JPEG/src -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/HDF5/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/GIPL/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/GE/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/IPL/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/GDCM/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/CSV/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/BioRad/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/BMP/include -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/HDF5/src -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/HDF5/src -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/GPUThresholding/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/GPUSmoothing/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Registration/GPUPDEDeformable/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Registration/GPUCommon/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/GPUImageFilterBase/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/GPUAnisotropicSmoothing/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Core/GPUFiniteDifference/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Core/GPUCommon/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/GIFTI/src/gifticlib -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/NIFTI/src/nifti/znzlib -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/NIFTI/src/nifti/niftilib -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/GDCM/src/gdcm/Source/DataStructureAndEncodingDefinition -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/GDCM/src/gdcm/Source/MessageExchangeDefinition -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/GDCM/src/gdcm/Source/InformationObjectDefinition -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/GDCM/src/gdcm/Source/Common -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/GDCM/src/gdcm/Source/DataDictionary -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/GDCM/src/gdcm/Source/Common -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/GDCM -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Registration/FEM/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Registration/PDEDeformable/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Numerics/FEM/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Registration/Common/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/SpatialObjects/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/XML/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/Expat/src/expat -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/Expat/src/expat -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Numerics/Eigen/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/DisplacementField/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/DiffusionTensorImage/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/Denoising/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/DeformableMesh/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/Deconvolution/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/DICOMParser/src/DICOMParser -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/DICOMParser/src/DICOMParser -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/Convolution/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/FFT/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/Colormap/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/Classifiers/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/BioCell/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/BiasCorrection/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Numerics/Polynomials/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/AntiAlias/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/LevelSets/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/SignedDistanceFunction/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Numerics/Optimizers/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/ImageFeature/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/ImageSources/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/ImageGradient/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/Smoothing/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/ImageCompare/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/IO/ImageBase/include -I/Users/pietro.gori/Softwares/ITKb/Modules/IO/ImageBase -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/FastMarching/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Core/QuadEdgeMesh/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/DistanceMap/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Numerics/NarrowBand/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/ImageLabel/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/BinaryMathematicalMorphology/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/MathematicalMorphology/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Segmentation/ConnectedComponents/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/Thresholding/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/ImageIntensity/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/Path/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/ImageStatistics/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Core/SpatialObjects/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/MetaIO/src/MetaIO/src -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/MetaIO/src/MetaIO/src -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/ZLIB/src -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/ZLIB/src -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Core/Mesh/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/ImageCompose/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/LabelMap/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/AnisotropicSmoothing/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/ImageGrid/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Core/ImageFunction/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Core/Transform/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Numerics/Statistics/include -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/Netlib -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Core/ImageAdaptors/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/CurvatureFlow/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Filtering/ImageFilterBase/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Core/FiniteDifference/include -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/Core/Common/include -I/Users/pietro.gori/Softwares/ITKb/Modules/Core/Common -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/VNLInstantiation/include -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/VNL/src/vxl/core -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/VNL/src/vxl/vcl -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/VNL/src/vxl/v3p/netlib -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/VNL/src/vxl/core -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/VNL/src/vxl/vcl -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/VNL/src/vxl/v3p/netlib -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/KWSys/src -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/KWIML/src -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/KWIML/src -I/Users/pietro.gori/Softwares/ITKb/Modules/ThirdParty/DoubleConversion/src/double-conversion -I/Users/pietro.gori/Softwares/InsightToolkit-4.9.1/Modules/ThirdParty/DoubleConversion/src/double-conversion -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/alglib -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/alglib -I/Users/pietro.gori/Softwares/VTKb/Charts/Core -I/Users/pietro.gori/Softwares/VTK-7.0.0/Charts/Core -I/Users/pietro.gori/Softwares/VTKb/Common/Color -I/Users/pietro.gori/Softwares/VTK-7.0.0/Common/Color -I/Users/pietro.gori/Softwares/VTKb/Common/DataModel -I/Users/pietro.gori/Softwares/VTK-7.0.0/Common/DataModel -I/Users/pietro.gori/Softwares/VTKb/Common/Math -I/Users/pietro.gori/Softwares/VTK-7.0.0/Common/Math -I/Users/pietro.gori/Softwares/VTKb/Common/Core -I/Users/pietro.gori/Softwares/VTK-7.0.0/Common/Core -I/Users/pietro.gori/Softwares/VTKb/Utilities/KWSys -I/Users/pietro.gori/Softwares/VTK-7.0.0/Utilities/KWSys -I/Users/pietro.gori/Softwares/VTKb/Common/Misc -I/Users/pietro.gori/Softwares/VTK-7.0.0/Common/Misc -I/Users/pietro.gori/Softwares/VTKb/Common/System -I/Users/pietro.gori/Softwares/VTK-7.0.0/Common/System -I/Users/pietro.gori/Softwares/VTKb/Common/Transforms -I/Users/pietro.gori/Softwares/VTK-7.0.0/Common/Transforms -I/Users/pietro.gori/Softwares/VTKb/Infovis/Core -I/Users/pietro.gori/Softwares/VTK-7.0.0/Infovis/Core -I/Users/pietro.gori/Softwares/VTKb/Filters/Extraction -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Extraction -I/Users/pietro.gori/Softwares/VTKb/Common/ExecutionModel -I/Users/pietro.gori/Softwares/VTK-7.0.0/Common/ExecutionModel -I/Users/pietro.gori/Softwares/VTKb/Filters/Core -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Core -I/Users/pietro.gori/Softwares/VTKb/Filters/General -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/General -I/Users/pietro.gori/Softwares/VTKb/Common/ComputationalGeometry -I/Users/pietro.gori/Softwares/VTK-7.0.0/Common/ComputationalGeometry -I/Users/pietro.gori/Softwares/VTKb/Filters/Statistics -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Statistics -I/Users/pietro.gori/Softwares/VTKb/Imaging/Fourier -I/Users/pietro.gori/Softwares/VTK-7.0.0/Imaging/Fourier -I/Users/pietro.gori/Softwares/VTKb/Imaging/Core -I/Users/pietro.gori/Softwares/VTK-7.0.0/Imaging/Core -I/Users/pietro.gori/Softwares/VTKb/Rendering/Context2D -I/Users/pietro.gori/Softwares/VTK-7.0.0/Rendering/Context2D -I/Users/pietro.gori/Softwares/VTKb/Rendering/Core -I/Users/pietro.gori/Softwares/VTK-7.0.0/Rendering/Core -I/Users/pietro.gori/Softwares/VTKb/Filters/Geometry -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Geometry -I/Users/pietro.gori/Softwares/VTKb/Filters/Sources -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Sources -I/Users/pietro.gori/Softwares/VTKb/Rendering/FreeType -I/Users/pietro.gori/Softwares/VTK-7.0.0/Rendering/FreeType -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/freetype -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/freetype -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/zlib -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/zlib -I/Users/pietro.gori/Softwares/VTKb/Utilities/DICOMParser -I/Users/pietro.gori/Softwares/VTK-7.0.0/Utilities/DICOMParser -I/Users/pietro.gori/Softwares/VTKb/Domains/Chemistry -I/Users/pietro.gori/Softwares/VTK-7.0.0/Domains/Chemistry -I/Users/pietro.gori/Softwares/VTKb/IO/XML -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/XML -I/Users/pietro.gori/Softwares/VTKb/IO/Geometry -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/Geometry -I/Users/pietro.gori/Softwares/VTKb/IO/Core -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/Core -I/Users/pietro.gori/Softwares/VTKb/IO/XMLParser -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/XMLParser -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/expat -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/expat -I/Users/pietro.gori/Softwares/VTKb/Domains/ChemistryOpenGL2 -I/Users/pietro.gori/Softwares/VTK-7.0.0/Domains/ChemistryOpenGL2 -I/Users/pietro.gori/Softwares/VTKb/Rendering/OpenGL2 -I/Users/pietro.gori/Softwares/VTK-7.0.0/Rendering/OpenGL2 -I/Users/pietro.gori/Softwares/VTKb/Imaging/Hybrid -I/Users/pietro.gori/Softwares/VTK-7.0.0/Imaging/Hybrid -I/Users/pietro.gori/Softwares/VTKb/IO/Image -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/Image -I/Users/pietro.gori/Softwares/VTKb/Utilities/MetaIO/vtkmetaio -I/Users/pietro.gori/Softwares/VTKb/Utilities/MetaIO -I/Users/pietro.gori/Softwares/VTK-7.0.0/Utilities/MetaIO -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/jpeg -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/jpeg -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/png -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/png -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/tiff -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/tiff -I/Users/pietro.gori/Softwares/VTKb/Utilities/EncodeString -I/Users/pietro.gori/Softwares/VTK-7.0.0/Utilities/EncodeString -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/glew -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/glew -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/exodusII -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/exodusII -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/netcdf/vtknetcdf/include -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/netcdf/vtknetcdf -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/netcdf -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/netcdf -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/hdf5/vtkhdf5 -isystem /Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/hdf5/vtkhdf5/hl/src -isystem /Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/hdf5/vtkhdf5/src -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/hdf5 -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/hdf5 -I/Users/pietro.gori/Softwares/VTKb/Filters/AMR -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/AMR -I/Users/pietro.gori/Softwares/VTKb/Parallel/Core -I/Users/pietro.gori/Softwares/VTK-7.0.0/Parallel/Core -I/Users/pietro.gori/Softwares/VTKb/IO/Legacy -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/Legacy -I/Users/pietro.gori/Softwares/VTKb/Utilities/HashSource -I/Users/pietro.gori/Softwares/VTK-7.0.0/Utilities/HashSource -I/Users/pietro.gori/Softwares/VTKb/Filters/FlowPaths -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/FlowPaths -I/Users/pietro.gori/Softwares/VTKb/Filters/Generic -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Generic -I/Users/pietro.gori/Softwares/VTKb/Filters/Hybrid -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Hybrid -I/Users/pietro.gori/Softwares/VTKb/Imaging/Sources -I/Users/pietro.gori/Softwares/VTK-7.0.0/Imaging/Sources -I/Users/pietro.gori/Softwares/VTKb/Filters/HyperTree -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/HyperTree -I/Users/pietro.gori/Softwares/VTKb/Filters/Imaging -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Imaging -I/Users/pietro.gori/Softwares/VTKb/Imaging/General -I/Users/pietro.gori/Softwares/VTK-7.0.0/Imaging/General -I/Users/pietro.gori/Softwares/VTKb/Filters/Modeling -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Modeling -I/Users/pietro.gori/Softwares/VTKb/Filters/Parallel -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Parallel -I/Users/pietro.gori/Softwares/VTKb/Filters/ParallelImaging -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/ParallelImaging -I/Users/pietro.gori/Softwares/VTKb/Filters/Programmable -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Programmable -I/Users/pietro.gori/Softwares/VTKb/Filters/Selection -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Selection -I/Users/pietro.gori/Softwares/VTKb/Filters/SMP -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/SMP -I/Users/pietro.gori/Softwares/VTKb/Filters/Texture -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Texture -I/Users/pietro.gori/Softwares/VTKb/Filters/Verdict -I/Users/pietro.gori/Softwares/VTK-7.0.0/Filters/Verdict -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/verdict -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/verdict -I/Users/pietro.gori/Softwares/VTKb/Geovis/Core -I/Users/pietro.gori/Softwares/VTK-7.0.0/Geovis/Core -I/Users/pietro.gori/Softwares/VTKb/Infovis/Layout -I/Users/pietro.gori/Softwares/VTK-7.0.0/Infovis/Layout -I/Users/pietro.gori/Softwares/VTKb/Interaction/Style -I/Users/pietro.gori/Softwares/VTK-7.0.0/Interaction/Style -I/Users/pietro.gori/Softwares/VTKb/Interaction/Widgets -I/Users/pietro.gori/Softwares/VTK-7.0.0/Interaction/Widgets -I/Users/pietro.gori/Softwares/VTKb/Rendering/Annotation -I/Users/pietro.gori/Softwares/VTK-7.0.0/Rendering/Annotation -I/Users/pietro.gori/Softwares/VTKb/Imaging/Color -I/Users/pietro.gori/Softwares/VTK-7.0.0/Imaging/Color -I/Users/pietro.gori/Softwares/VTKb/Rendering/Volume -I/Users/pietro.gori/Softwares/VTK-7.0.0/Rendering/Volume -I/Users/pietro.gori/Softwares/VTKb/Views/Core -I/Users/pietro.gori/Softwares/VTK-7.0.0/Views/Core -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/libproj4/vtklibproj4 -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/libproj4/vtklibproj4 -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/libproj4 -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/libproj4 -I/Users/pietro.gori/Softwares/VTKb/Imaging/Math -I/Users/pietro.gori/Softwares/VTK-7.0.0/Imaging/Math -I/Users/pietro.gori/Softwares/VTKb/Imaging/Morphological -I/Users/pietro.gori/Softwares/VTK-7.0.0/Imaging/Morphological -I/Users/pietro.gori/Softwares/VTKb/Imaging/Statistics -I/Users/pietro.gori/Softwares/VTK-7.0.0/Imaging/Statistics -I/Users/pietro.gori/Softwares/VTKb/Imaging/Stencil -I/Users/pietro.gori/Softwares/VTK-7.0.0/Imaging/Stencil -I/Users/pietro.gori/Softwares/VTKb/Interaction/Image -I/Users/pietro.gori/Softwares/VTK-7.0.0/Interaction/Image -I/Users/pietro.gori/Softwares/VTKb/IO/AMR -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/AMR -I/Users/pietro.gori/Softwares/VTKb/IO/EnSight -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/EnSight -I/Users/pietro.gori/Softwares/VTKb/IO/Exodus -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/Exodus -I/Users/pietro.gori/Softwares/VTKb/IO/Export -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/Export -I/Users/pietro.gori/Softwares/VTKb/Rendering/Label -I/Users/pietro.gori/Softwares/VTK-7.0.0/Rendering/Label -I/Users/pietro.gori/Softwares/VTKb/IO/Import -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/Import -I/Users/pietro.gori/Softwares/VTKb/IO/Infovis -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/Infovis -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/libxml2/vtklibxml2 -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/libxml2 -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/libxml2 -I/Users/pietro.gori/Softwares/VTKb/IO/LSDyna -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/LSDyna -I/Users/pietro.gori/Softwares/VTKb/IO/MINC -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/MINC -I/Users/pietro.gori/Softwares/VTKb/IO/Movie -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/Movie -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/oggtheora -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/oggtheora -I/Users/pietro.gori/Softwares/VTKb/IO/NetCDF -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/NetCDF -I/Users/pietro.gori/Softwares/VTKb/IO/Parallel -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/Parallel -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/jsoncpp -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/jsoncpp -I/Users/pietro.gori/Softwares/VTKb/IO/ParallelXML -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/ParallelXML -I/Users/pietro.gori/Softwares/VTKb/IO/PLY -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/PLY -I/Users/pietro.gori/Softwares/VTKb/IO/SQL -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/SQL -I/Users/pietro.gori/Softwares/VTKb/ThirdParty/sqlite -I/Users/pietro.gori/Softwares/VTK-7.0.0/ThirdParty/sqlite -I/Users/pietro.gori/Softwares/VTKb/IO/Video -I/Users/pietro.gori/Softwares/VTK-7.0.0/IO/Video -I/Users/pietro.gori/Softwares/VTKb/Rendering/ContextOpenGL2 -I/Users/pietro.gori/Softwares/VTK-7.0.0/Rendering/ContextOpenGL2 -I/Users/pietro.gori/Softwares/VTKb/Rendering/Image -I/Users/pietro.gori/Softwares/VTK-7.0.0/Rendering/Image -I/Users/pietro.gori/Softwares/VTKb/Rendering/LOD -I/Users/pietro.gori/Softwares/VTK-7.0.0/Rendering/LOD -I/Users/pietro.gori/Softwares/VTKb/Rendering/VolumeOpenGL2 -I/Users/pietro.gori/Softwares/VTK-7.0.0/Rendering/VolumeOpenGL2 -I/Users/pietro.gori/Softwares/VTKb/Views/Context2D -I/Users/pietro.gori/Softwares/VTK-7.0.0/Views/Context2D -I/Users/pietro.gori/Softwares/VTKb/Views/Infovis -I/Users/pietro.gori/Softwares/VTK-7.0.0/Views/Infovis -I/Users/pietro.gori/Softwares/VTKb/Wrapping/Tools -I/Users/pietro.gori/Softwares/VTK-7.0.0/Wrapping/Tools -I/Users/pietro.gori/Softwares/clinica/clinica/lib/weighted_prototypes_lib/cpp_code -I/Users/pietro.gori/Softwares/clinica/clinica/lib/weighted_prototypes_lib/cpp_code/../../eigen -isystem /Users/pietro.gori/Softwares/VTKb/ThirdParty/hdf5/vtkhdf5/hl/src -isystem /Users/pietro.gori/Softwares/VTKb/ThirdParty/hdf5/vtkhdf5/src 

