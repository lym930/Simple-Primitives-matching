from scipy.spatial.transform import Rotation as R
import numpy as np
from mayavi import mlab


def euler2rotm(euler_vec):
    _r = R.from_euler('ZYX', euler_vec)
    return _r.as_matrix()

def draw_rectangular_prism(hx, hy, hz, rotm, tran_vec, color, resolution=100):

    x_bottom, y_bottom = np.meshgrid(
        np.linspace(-hx, hx, resolution),
        np.linspace(-hy, hy, resolution)
    )
    z_bottom, z_top = np.full_like(x_bottom, -hz), np.full_like(x_bottom, hz)

    grid_transformation_elliptical_frustum(x_bottom, y_bottom, z_bottom, rotm, tran_vec, color)
    grid_transformation_elliptical_frustum(x_bottom, y_bottom, z_top, rotm, tran_vec, color)

    x_front, z_front = np.meshgrid(
        np.linspace(-hx, hx, resolution),
        np.linspace(-hz, hz, resolution)
    )
    y_front, y_back = np.full_like(x_front, hy), -np.full_like(x_front, hy)
    grid_transformation_elliptical_frustum(x_front, y_front, z_front, rotm, tran_vec, color)
    grid_transformation_elliptical_frustum(x_front, y_back, z_front, rotm, tran_vec, color)
    y_left, z_left = np.meshgrid(
        np.linspace(-hy, hy, resolution),
        np.linspace(-hz, hz, resolution)
    )
    x_left, x_right = -np.full_like(y_left, hx), np.full_like(y_left, hx)

    grid_transformation_elliptical_frustum(x_left, y_left, z_left, rotm, tran_vec, color)
    grid_transformation_elliptical_frustum(x_right, y_left, z_left, rotm, tran_vec, color)

def draw_superellipse_prism(eps2, a, b, c, rotm, tran_vec, color, resolution=100):

    theta = np.linspace(0, 2 * np.pi, resolution)
    r = np.linspace(0, 1, 100)
    R, Theta = np.meshgrid(r, theta)


    X_bottom, Y_bottom = superellipse_coords(Theta, a, b, 2/eps2)
    X_bottom *= R
    Y_bottom *= R
    Z_bottom = np.full_like(X_bottom, -c)
    grid_transformation_elliptical_frustum(X_bottom, Y_bottom, Z_bottom, rotm, tran_vec, color, )

    Z_top = np.full_like(X_bottom, c)
    grid_transformation_elliptical_frustum(X_bottom, Y_bottom, Z_top, rotm, tran_vec, color, )

    theta_side = np.linspace(0, 2 * np.pi, resolution)
    t = np.linspace(-c, c, resolution)
    Theta_side, T_side = np.meshgrid(theta_side, t)

    X_side, Y_side = superellipse_coords(Theta_side, a, b, 2/eps2)
    Z_side = T_side

    grid_transformation_elliptical_frustum(X_side, Y_side, Z_side, rotm, tran_vec, color, )

def plot_starry_cylinder(eps2, a, b, c, rotm, tran_vec, color):

    resolution = 100

    r = np.linspace(0, 1, resolution)
    theta = np.linspace(0, 2 * np.pi, resolution)
    R, Theta = np.meshgrid(r, theta)

    x_bottom = R * a * np.cos(Theta) ** eps2
    y_bottom = R * b * np.sin(Theta) ** eps2

    z_bottom = -c * np.ones_like(x_bottom)
    z_top = c * np.ones_like(x_bottom)

    theta_side = np.linspace(0, 2 * np.pi, resolution)
    z_points = np.linspace(-c, c, resolution)
    theta_grid, z = np.meshgrid(theta_side, z_points)

    x = a * np.cos(theta_grid) ** eps2
    y = b * np.sin(theta_grid) ** eps2

    if eps2 % 2 != 1:
        grid_transformation_elliptical_frustum(x_bottom, y_bottom, z_bottom, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(-x_bottom, y_bottom, z_bottom, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(x_bottom, -y_bottom, z_bottom, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(-x_bottom, -y_bottom, z_bottom, rotm, tran_vec, color)

        grid_transformation_elliptical_frustum(x_bottom, y_bottom, z_top, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(-x_bottom, y_bottom, z_top, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(x_bottom, -y_bottom, z_top, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(-x_bottom, -y_bottom, z_top, rotm, tran_vec, color)


        grid_transformation_elliptical_frustum(x, y, z, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(-x, y, z, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(x, -y, z, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(-x, -y, z, rotm, tran_vec, color)
    else:
        grid_transformation_elliptical_frustum(x_bottom, y_bottom, z_bottom, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(x_bottom, y_bottom, z_top, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(x, y, z, rotm, tran_vec, color)

def draw_rectangular_cube(eps1, a, b, c, rotm, tran_vec, color, resolution=100):

    if eps1 != 2:
        # 0-np.arctan(b/a)
        phi1 = np.linspace(0, np.pi / 2, resolution)
        xita1 = np.linspace(0, np.arctan(b / a), resolution)
        phi1_grid, xita1_grid = np.meshgrid(phi1, xita1)

        X1 = a * np.sin(phi1_grid)
        Y1 = a * np.sin(phi1_grid) * np.tan(xita1_grid)
        Z1 = c * np.cos(phi1_grid) ** eps1

        phi2 = np.linspace(0, np.pi / 2, resolution)
        xita2 = np.linspace(np.arctan(b / a), np.pi / 2, resolution)
        phi2_grid, xita2_grid = np.meshgrid(phi2, xita2)

        X2 = b * np.sin(phi2_grid) / np.tan(xita2_grid)
        Y2 = b * np.sin(phi2_grid)
        Z2 = c * np.cos(phi2_grid) ** eps1

        grid_transformation_elliptical_frustum(X1, Y1, Z1, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(X2, Y2, Z2, rotm, tran_vec, color)

        grid_transformation_elliptical_frustum(-X1, Y1, Z1, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(-X2, Y2, Z2, rotm, tran_vec, color)

        grid_transformation_elliptical_frustum(X1, -Y1, Z1, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(X2, -Y2, Z2, rotm, tran_vec, color)

        grid_transformation_elliptical_frustum(-X1, -Y1, Z1, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(-X2, -Y2, Z2, rotm, tran_vec, color)

        grid_transformation_elliptical_frustum(X1, Y1, -Z1, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(X2, Y2, -Z2, rotm, tran_vec, color)

        grid_transformation_elliptical_frustum(-X1, Y1, -Z1, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(-X2, Y2, -Z2, rotm, tran_vec, color)

        grid_transformation_elliptical_frustum(X1, -Y1, -Z1, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(X2, -Y2, -Z2, rotm, tran_vec, color)

        grid_transformation_elliptical_frustum(-X1, -Y1, -Z1, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(-X2, -Y2, -Z2, rotm, tran_vec, color)

    else:
        u = np.linspace(0, 1, resolution)
        v = np.linspace(0, 1, resolution)
        U, V = np.meshgrid(u, v)

        X_front = (-a + U * a * 2) * (1 - V)
        Y_front = b * (1 - V)
        Z_front = c * V

        grid_transformation_elliptical_frustum(X_front, Y_front, Z_front, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(X_front, Y_front, -Z_front, rotm, tran_vec, color)

        Y_back = -b * (1 - V)
        grid_transformation_elliptical_frustum(X_front, Y_back, Z_front, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(X_front, Y_back, -Z_front, rotm, tran_vec, color)

        X_right = a * (1 - V)
        Y_right = (-b + U * b * 2) * (1 - V)
        grid_transformation_elliptical_frustum(X_right, Y_right, Z_front, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(X_right, Y_right, -Z_front, rotm, tran_vec, color)

        X_left = -a * (1 - V)
        Y_left = (-b + U * b * 2) * (1 - V)
        grid_transformation_elliptical_frustum(X_left, Y_left, Z_front, rotm, tran_vec, color)
        grid_transformation_elliptical_frustum(X_left, Y_left, -Z_front, rotm, tran_vec, color)

def draw_superellipse_frustum_pair(eps1, eps2, a, b, c, rotm, tran_vec, color, resolution=100):
    phi = np.linspace(0, np.pi / 2, resolution)
    theta = np.linspace(0, np.pi / 2, resolution)
    phi_grid, theta_grid = np.meshgrid(phi, theta)

    x = a * (np.sin(phi_grid) * np.cos(theta_grid)) ** eps2
    y = b * (np.sin(phi_grid) * np.sin(theta_grid)) ** eps2
    z = c * (np.cos(phi_grid)) ** eps1

    grid_transformation_elliptical_frustum(x, y, z, rotm, tran_vec, color, )
    grid_transformation_elliptical_frustum(-x, y, z, rotm, tran_vec, color, )
    grid_transformation_elliptical_frustum(-x, -y, z, rotm, tran_vec, color, )
    grid_transformation_elliptical_frustum(x, -y, z, rotm, tran_vec, color, )
    grid_transformation_elliptical_frustum(x, y, -z, rotm, tran_vec, color, )
    grid_transformation_elliptical_frustum(-x, y, -z, rotm, tran_vec, color, )
    grid_transformation_elliptical_frustum(-x, -y, -z, rotm, tran_vec, color, )
    grid_transformation_elliptical_frustum(x, -y, -z, rotm, tran_vec, color, )

def draw_star_frustum_pair(eps1, eps2, a, b, c, rotm, tran_vec, color,resolution=100):
    phi = np.linspace(0, np.pi / 2, resolution)
    theta = np.linspace(0, np.pi / 2, resolution)
    phi_grid, theta_grid = np.meshgrid(phi, theta)

    x = a * (np.sin(phi_grid) * np.cos(theta_grid)) ** eps2
    y = b * (np.sin(phi_grid) * np.sin(theta_grid)) ** eps2
    z = c * (np.cos(phi_grid)) ** eps1

    grid_transformation_elliptical_frustum(x, y, z, rotm, tran_vec, color)
    grid_transformation_elliptical_frustum(-x, y, z, rotm, tran_vec, color)
    grid_transformation_elliptical_frustum(-x, -y, z, rotm, tran_vec, color)
    grid_transformation_elliptical_frustum(x, -y, z, rotm, tran_vec, color)
    grid_transformation_elliptical_frustum(x, y, -z, rotm, tran_vec, color)
    grid_transformation_elliptical_frustum(-x, y, -z, rotm, tran_vec, color)
    grid_transformation_elliptical_frustum(-x, -y, -z, rotm, tran_vec, color)
    grid_transformation_elliptical_frustum(x, -y, -z, rotm, tran_vec, color)

def draw_frustum_pair(eps1, a, b, c, rotm, tran_vec, color, resolution=100):

    L_bottom, W_bottom = a, b

    landa = c-c * pow(0.9, 2/eps1)
    L_top = (landa ** 2 / (1+(b/a) ** 2)) ** 0.5
    W_top = (b/a) * L_top

    _draw_single_frustum(c, L_bottom, W_bottom, L_top, W_top, rotm, tran_vec, color, resolution)

    _draw_single_frustum(-c, L_bottom, W_bottom, L_top, W_top, rotm, tran_vec, color, resolution)

def _draw_single_frustum(h, L_bottom, W_bottom, L_top, W_top, rotm, tran_vec, color, resolution):

    x_top = np.linspace(-L_top, L_top, resolution)
    y_top = np.linspace(-W_top, W_top, resolution)
    X_top, Y_top = np.meshgrid(x_top, y_top)
    Z_top = np.full_like(X_top, h)

    grid_transformation_elliptical_frustum(X_top, Y_top, Z_top, rotm, tran_vec, color)

    u = np.linspace(0, 1, resolution)
    v = np.linspace(0, 1, resolution)
    U, V = np.meshgrid(u, v)

    X_front = (-L_bottom + U * L_bottom * 2) * (1 - V) + (-L_top + U * L_top * 2) * V
    Y_front = W_bottom * (1 - V) + W_top * V
    Z_front = h * V

    grid_transformation_elliptical_frustum(X_front, Y_front, Z_front, rotm, tran_vec, color)

    Y_back = -W_bottom * (1 - V) + -W_top * V
    grid_transformation_elliptical_frustum(X_front, Y_back, Z_front, rotm, tran_vec, color)

    X_right = L_bottom * (1 - V) + L_top * V
    Y_right = (-W_bottom + U * W_bottom * 2) * (1 - V) + (-W_top + U * W_top * 2) * V
    grid_transformation_elliptical_frustum(X_right, Y_right, Z_front, rotm, tran_vec, color)

    X_left = -L_bottom * (1 - V) + -L_top * V
    Y_left = (-W_bottom + U * W_bottom * 2) * (1 - V) + (-W_top + U * W_top * 2) * V
    grid_transformation_elliptical_frustum(X_left, Y_left, Z_front, rotm, tran_vec, color)

def superellipse_coords(theta, a, b, n):
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    r = 1.0 / (np.abs(cos_theta / a) ** n + np.abs(sin_theta / b) ** n) ** (1.0 / n)
    x = r * cos_theta
    y = r * sin_theta
    return x, y

def grid_transformation_elliptical_frustum(x, y, z, rotm, tran_vec, color):
    x, y, z = x.reshape(-1, 1), y.reshape(-1, 1), z.reshape(-1, 1)
    co_grid = np.concatenate((x, y, z), axis=1)
    tran_grid = rotm @ co_grid.T + tran_vec.reshape(-1, 1)
    x_grid, y_grid, z_grid = tran_grid[0], tran_grid[1], tran_grid[2]

    mlab.mesh(x_grid.reshape(100, -1), y_grid.reshape(100, -1), z_grid.reshape(100, -1), color=color)