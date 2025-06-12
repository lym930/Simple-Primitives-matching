import numpy as np
from mayavi import mlab
from algorithm.primitives_fitting import Distinguish_Type_of_Primitive

model_path = 'data/examples/A teapot in Chinese style_model.csv'

primitives = np.genfromtxt(model_path, delimiter=',')
fig = mlab.figure(size=(400, 400), bgcolor=(1, 1, 1))

for primitive in primitives:
    eps1, eps2 = primitive[0], primitive[1]
    a, b, c = primitive[2], primitive[3], primitive[4]
    euler_vec = primitive[5:8]
    tran_vec = primitive[8:11]
    Distinguish_Type_of_Primitive(eps1, eps2, a, b, c, euler_vec, tran_vec)

mlab.show()
