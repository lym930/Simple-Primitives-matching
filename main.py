import csv
import numpy as np
from algorithm.primitives_fitting import Distinguish_Type_of_Primitive
from algorithm.MPS import mps
from mayavi import mlab

if __name__ == "__main__":

    csv_path = r"data\examples\A teapot in Chinese style.csv"
    if not csv_path:
        raise ValueError("No file selected.")

    TSDF = np.genfromtxt(csv_path, delimiter=',').T

    voxel_grid = {}

    voxel_grid['size'] = np.ones(3, dtype=int) * int(TSDF[0])
    voxel_grid['range'] = TSDF[1:7]
    TSDF = TSDF[7:]

    voxel_grid['x'] = np.linspace(voxel_grid['range'][0], voxel_grid['range'][1], int(voxel_grid['size'][0]))
    voxel_grid['y'] = np.linspace(voxel_grid['range'][2], voxel_grid['range'][3], int(voxel_grid['size'][1]))
    voxel_grid['z'] = np.linspace(voxel_grid['range'][4], voxel_grid['range'][5], int(voxel_grid['size'][2]))

    x, y, z = np.meshgrid(voxel_grid['x'], voxel_grid['y'], voxel_grid['z'], indexing='ij')
    points = np.stack((x, y, z), axis=3)
    voxel_grid['points'] = points.reshape((-1, 3), order='F').T

    voxel_grid['interval'] = (voxel_grid['range'][1] - voxel_grid['range'][0]) / (voxel_grid['size'][0] - 1)
    voxel_grid['truncation'] = 1.2 * voxel_grid['interval']
    voxel_grid['disp_range'] = [-np.inf, voxel_grid['truncation']]
    voxel_grid['visualizeArclength'] = 0.01 * np.sqrt(voxel_grid['range'][1] - voxel_grid['range'][0])

    TSDF = np.clip(TSDF, -voxel_grid['truncation'], voxel_grid['truncation'])
    print('TSDF.shape: ', TSDF.shape)
    print('voxel_grid[\'points\'].shape: ', voxel_grid['points'].shape)


    # Superquadrics iterative fitting
    superquadrics = mps(TSDF, voxel_grid)

    fig = mlab.figure(size=(400, 400), bgcolor=(1, 1, 1))

    # Extracting parameters of superquadrics
    for sq in superquadrics:
        eps1, eps2 = sq[0], sq[1] # Shape parameters
        a, b, c = sq[2], sq[3], sq[4] # Size parameters
        euler_vec = sq[5:8]  # rotation vector
        tran_vec = sq[8:11]  # translation vector

        # Perform simple primitive matching and optimization operations
        Distinguish_Type_of_Primitive(eps1, eps2, a, b, c, euler_vec, tran_vec)

    filename = csv_path.strip('.csv') + '_model.csv'
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(superquadrics)

        print("model saved to" + filename + ".")

    mlab.show()