A = [
    -3, 2, -6;
    5, 7, -5;
    1, 4, -2
];
b = [
    6; 6; 8
];
% solution to Ax=b is x=[-2,3,1]


[L, U, P] = PALU_Gauss(A)
% using Ly = Pb to obtain y
y = fw_sub(L, P*b)
% using Ux = y to obtain x
x = bw_sub(U, y)