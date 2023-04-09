A = [
    -3, 2, -6;
    5, 7, -5;
    1, 4, -2
];
b = [
    6; 6; 8
];
% solution to Ax=b is x=[-2,3,1]

aug_A = [A, b];
C = GEMP(aug_A)
D = C(:,1:3);
d = C(:,4);
bw_sub(D, d)