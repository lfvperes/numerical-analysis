clear all
clc
A = [   8, 1, -1;
        2, 1, 9;
        1, -7, 2    ];
b = [   5;
        25;
        -10     ];

% a) Ax = b
disp("a)");
tStart_a = tic;
% Gauss Elimination Method w/ pivoting after concatenating A and b
C = GEMP([A, b])
% separating A_n and b_n after GEM
A_n = C(:,1:3);
b_n = C(:,4);
% using backward substitution to solve
x = bw_sub(A_n, b_n)
% stop measuring time
tEnd_a = toc(tStart_a);
% comparing Ax and b
printf("A.x =\n\n");
disp(A*x);
clear x;

% b) PA = LU, Ly = Pb, Ux = y
disp("b)");
tStart_b = tic;
% find L, U and P
[L, U, P] = PALU_Gauss(A)
% using Ly = Pb with forward substitution
% (mirrored backward subtitution)
y = fw_sub(L, P*b)
% using Ux = y with backward substitution
x = bw_sub(U, y)
% stop measuring time
tEnd_b = toc(tStart_b);
% comparing Ax and b
printf("A.x =\n\n");
disp(A*x);
% comparing PA and LU
printf("P.A =\n\n");
disp(P*A);
printf("L.U =\n\n");
disp(L*U);

% c) time comparison
disp("c)");
printf("Codigo a) levou %f s\n", tEnd_a);
printf("Codigo b) levou %f s\n", tEnd_b);

% d)
disp("d)");
tStart_d = tic;
x_comp = A \ b;
tEnd_d = toc(tStart_d);
x
printf("A.x =\n\n");
disp(A*x);
printf("Codigo d) levou %f s\n", tEnd_d);