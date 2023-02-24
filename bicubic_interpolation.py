import numpy as np

def enlarge_image(t):
    height = len(t)
    width = len(t[0])
    new_height = height*2
    new_width = width*2
    m = [[[0,0,0] for i in range(new_width)] for j in range(new_height)]
    for i in range(0,new_height,2):
        for j in range(0,new_width,2):
            m[i][j] = t[i//2][j//2]
    return m

def find_voisins(t, x, y):
    height = len(t)
    width = len(t)
    voisins_r = [[[0,0,0] for i in range(4)] for i in range(4)]
    voisins_g = [[[0,0,0] for i in range(4)] for i in range(4)]
    voisins_b = [[[0,0,0] for i in range(4)] for i in range(4)]
    for i in range(-1, 3):
        for j in range(-1, 3):
            if x+1<0:
                px = -x
            elif x+i>=width:
                px = 2*width - x - i - 2
            else:
                px = x+1
            if y+j<0:
                py=-y
            elif y+j >= height:
                py = 2*width - y - j - 2
            else:
                py = y+j
            voisins_r[j+1][i+1] = t[py][px][0]
            voisins_g[j+1][i+1] = t[py][px][1]
            voisins_b[j+1][i+1] = t[py][px][2]
    return voisins_r, voisins_g, voisins_b
    
def bicubic_coeffs(voisins_r, voisins_g, voisins_b):
    A = np.zeros((16,16))
    B_r = np.zeros((16,1))
    B_g = np.zeros((16,1))
    B_b = np.zeros((16,1))
    for i in range(4):
        for j in range(4):
            x = i - 1
            y = j - 1
            A[i*4+j] = [x**3, x**2*y, x*y**2, y**3, x**2, x*y, y**2, x, y, 1, 0, 0, 0, 0, 0, 0]
            B_r[i*4+j] = voisins_r[j][i]
            B_g[i*4+j] = voisins_g[j][i]
            B_b[i*4+j] = voisins_b[j][i]
    a_r = np.linalg.solve(A, B_r)
    a_g = np.linalg.solve(A, B_g)
    a_b = np.linalg.solve(A, B_b)
    return a_r, a_g, a_b

def bicubic_interpolate(voisins_r, voisins_g, voisins_b, x, y):
    a_r, a_g, a_b  = bicubic_coeffs(voisins_r, voisins_g, voisins_b)
    px = np.array([x**3, x**2*y, x*y**2, y**3, x**2, x*y, y**2, x, y, 1, 0, 0, 0, 0, 0, 0])
    r_r = np.dot(px, a_r)
    r_g = np.dot(px, a_g)
    r_b = np.dot(px, a_b)
    return r_r[0], r_g[0], r_b[0]

def bicubic_interpolation(t):
    enlarged_image = enlarge_image(t)
    new_height = len(enlarged_image)
    new_width = len(enlarged_image[0])
    for y in range(new_height):
        if y%2==0:
            for x in range(0,new_width, 2):
                orig_x = x//2
                orig_y = y//2
                voisins_r, voisins_g, voisins_b = find_voisins(t, orig_x, orig_y)
                pxl_value_r, pxl_value_g, pxl_value_b = bicubic_interpolate(voisins_r, voisins_g, voisins_b, orig_x, orig_y)
                enlarged_image[y][x] = [pxl_value_r, pxl_value_g, pxl_value_b]
        else:
            for x in range(new_width):
                orig_x = x//2
                orig_y = y//2
                voisins_r, voisins_g, voisins_b = find_voisins(t, orig_x, orig_y)
                pxl_value_r, pxl_value_g, pxl_value_b = bicubic_interpolate(voisins_r, voisins_g, voisins_b, orig_x, orig_y)
                enlarged_image[y][x] = [pxl_value_r, pxl_value_g, pxl_value_b]
    return enlarged_image
        