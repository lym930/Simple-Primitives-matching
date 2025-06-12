from algorithm.draw_primitives import *

def Distinguish_Type_of_Primitive(eps1, eps2, a, b, c, euler_vec, tran_vec):

    # from euler angles to rotation matrix (ZYX_intrinsic)
    rotm = euler2rotm(euler_vec)

    color = (0.933, 0.8667, 0.510)

    # 柱体
    if 0 < eps1 < 0.5 and 0 < eps2 <= 0.5:
        draw_rectangular_prism(a, b, c, rotm, tran_vec, color)
        return None

    elif 0 < eps1 < 0.5 and 0.5 < eps2 < 2:
        draw_superellipse_prism(eps2, a, b, c, rotm, tran_vec, color, resolution=100)
        return None

    elif 0 < eps1 < 0.5 and eps2 >= 2:
        plot_starry_cylinder(eps2, a, b, c, rotm, tran_vec, color)
        return None

    # 台体
    elif 0.5 <= eps1 <= 2 and 0 < eps2 <= 0.5:
        draw_rectangular_cube(eps1, a, b, c, rotm, tran_vec, color, resolution=100)
        return None


    elif 0.5 <= eps1 <= 2 and 0.5 < eps2 < 2:
        draw_superellipse_frustum_pair(eps1, eps2, a, b, c, rotm, tran_vec, color, resolution=100)
        return None

    elif 0.5 <= eps1 <= 2 and eps2 >= 2:
        draw_star_frustum_pair(eps1, eps2, a, b, c, rotm, tran_vec, color, resolution=100)
        return None

    # 锥体
    elif eps1 > 2 and 0 < eps2 <= 0.5:
        draw_frustum_pair(eps1, a, b, c, rotm, tran_vec, color, resolution=100)
        return None

    elif eps1 > 2 and 0.5 < eps2 < 2:
        draw_superellipse_frustum_pair(eps1, eps2, a, b, c, rotm, tran_vec, color, resolution=100)
        return None

    elif eps1 > 2 and eps2 >= 2:
        draw_star_frustum_pair(eps1, eps2, a, b, c, rotm, tran_vec, color, resolution=100)
        return None

    else:
        return None
