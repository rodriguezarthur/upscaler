import numpy as np

def enlarge_image(t, scale_factor):
    height = len(t)
    width = len(t[0])
    new_height = (height - 1)*(scale_factor - 1) + height
    new_width = (width - 1)*(scale_factor - 1) + width
    m = [[[0,0,0] for i in range(new_width)] for j in range(new_height)]
    for i in range(0,new_height,scale_factor):
        for j in range(0,new_width,scale_factor):
            m[i][j] = t[i//scale_factor][j//scale_factor]
    return m

def bilinear_interpolation(t, scale_factor):
    enlarged_t = enlarge_image(t, scale_factor)
    for i in range(len(enlarged_t)):
        if i%scale_factor==0:
            for j in range(1,len(enlarged_t[0]),scale_factor):
                for k in range(1, scale_factor):
                    r_value = (enlarged_t[i][j-1][0]*(scale_factor-k) + enlarged_t[i][j+(scale_factor-1)][0]*k)//scale_factor
                    g_value = (enlarged_t[i][j-1][1]*(scale_factor-k) + enlarged_t[i][j+(scale_factor-1)][1]*k)//scale_factor
                    b_value = (enlarged_t[i][j-1][2]*(scale_factor-k) + enlarged_t[i][j+(scale_factor-1)][2]*k)//scale_factor
                    enlarged_t[i][j+k-1] = [r_value, g_value, b_value]
        else:
            for j in range(len(enlarged_t[0])):
                if j%scale_factor==0:
                    d_up = i%scale_factor
                    d_bot = scale_factor - d_up
                    r_value = (enlarged_t[i-d_up][j][0]*d_bot + enlarged_t[i+d_bot][j][0]*d_up)//scale_factor
                    g_value = (enlarged_t[i-d_up][j][1]*d_bot + enlarged_t[i+d_bot][j][1]*d_up)//scale_factor
                    b_value = (enlarged_t[i-d_up][j][2]*d_bot + enlarged_t[i+d_bot][j][2]*d_up)//scale_factor
            
                else:
                    d_up = i%scale_factor
                    d_bot = scale_factor - d_up
                    d_left = j%scale_factor
                    d_right = scale_factor - d_left
                    
                    r_value_up = (enlarged_t[i-d_up][j-d_left][0]*d_right + enlarged_t[i-d_up][j+d_right][0]*d_left)//scale_factor
                    g_value_up = (enlarged_t[i-d_up][j-d_left][1]*d_right + enlarged_t[i-d_up][j+d_right][1]*d_left)//scale_factor
                    b_value_up = (enlarged_t[i-d_up][j-d_left][2]*d_right + enlarged_t[i-d_up][j+d_right][2]*d_left)//scale_factor
                    
                    r_value_bot = (enlarged_t[i+d_bot][j-d_left][0]*d_right + enlarged_t[i+d_bot][j+d_right][0]*d_left)//scale_factor
                    g_value_bot = (enlarged_t[i+d_bot][j-d_left][1]*d_right + enlarged_t[i+d_bot][j+d_right][1]*d_left)//scale_factor
                    b_value_bot = (enlarged_t[i+d_bot][j-d_left][2]*d_right + enlarged_t[i+d_bot][j+d_right][2]*d_left)//scale_factor
                    
                    r_value = (r_value_up*d_bot + r_value_bot*d_up)//scale_factor
                    g_value = (g_value_up*d_bot + g_value_bot*d_up)//scale_factor
                    b_value = (b_value_up*d_bot + b_value_bot*d_up)//scale_factor
                    
                enlarged_t[i][j] = [r_value, g_value, b_value]
    return enlarged_t
    