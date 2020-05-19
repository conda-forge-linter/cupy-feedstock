# Configure CuPy to use 1 GPU for testing
import os
os.environ["CUPY_TEST_GPU_LIMIT"] = "1"

# Check CUDA_PATH is set
cuda_path = os.environ.get('CUDA_PATH')
assert cuda_path is not None
print("CUDA_PATH:", cuda_path)

# Check CUDA libraries are available
assert os.path.isfile(os.path.join(cuda_path, 'lib/libcudart.so'))

# Check for CuPy (without importing)
import pkgutil
pkgutil.find_loader("cupy")

# Try to import CuPy
import sys
try:
    import cupy
    
    # Print CuPy runtime info
    # this line would fail if there is no GPU
    cupy.show_config()
except Exception as e:
    print('Got an error: \n%s' % str(e))
    print("No GPU available. Exiting without running CuPy's tests.")
    sys.exit(0)

## The tests below are commented out because the conda-forge docker images
## now have libcuda.so, so "import cupy" would not fail, but tests would
## fail on the Azure CI since there is no GPU. See the discussion in
## https://github.com/conda-forge/cupy-feedstock/pull/59#issuecomment-629584090
#
## Run CuPy's test suite
#import py
#py.test.cmdline.main(["tests/cupy_tests"])
#py.test.cmdline.main(["tests/cupyx_tests"])
