raw = """(  2.22; -5.56)  ( -8.08; -6.51)  ( -3.72; -5.78)  ( -8.26; -9.94)  ( -5.23; -7.20)  ( -4.70; -5.23)  ( -2.93; -3.33)  ( -0.51; -7.80)  
( -6.36; -5.18)  ( -5.78; -0.51)  (  0.65; -2.99)  ( -3.54; -7.15)  ( -0.87; -5.28)  ( -2.77; -5.36)  ( -2.20; -4.50)  ( -2.21;  1.05)  
( -2.26; -9.08)  (  1.60; -1.29)  ( -1.23; -5.65)  ( -5.20; -9.13)  ( -5.49; -6.35)  ( -1.06;  0.05)  (  1.14; -6.56)  ( -0.05; -5.08)  
( -7.45; -12.66)  ( -6.67; -7.20)  (  0.97;  2.01)  ( -8.90; -3.48)  ( -5.67; -5.92)  ( -7.20; -3.07)  ( -1.53; -0.88)  ( -2.53;  1.90)  
( -2.58;  0.09)  (  2.24;  0.95)  ( -0.57; -3.52)  ( -1.87; -7.97)  ( -2.72; -5.95)  ( -5.15; -8.38)  ( -5.24; -5.75)  (  0.75; -3.42)  
( -6.24; -1.24)  (  1.88; -0.62)  (  0.26; -4.86)  ( -1.83; -2.98)  ( -5.93;  0.86)  ( -2.21; -7.39)  ( -3.80; -5.08)  (  0.27;  2.10)  
( -4.10; -3.73)  ( -5.74; -4.92)"""
str_dim2 = raw.replace("\n", " ").replace("  ", " ").replace("( ", "(").replace(") ", "), ")
dim2 = [eval(el) for el in str_dim2.replace("), ", ") ").replace("; ", ",").split()]