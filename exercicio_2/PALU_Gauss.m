function [L, U, P] = PALU_Gauss(A)
    [m, n] = size(A);

    L = eye(m, n);
    U = A;
    P = eye(m, n);

    for k = 1:m-1
        % pivoting
        if (U(k,k) == 0)
            U(k:k+1,:) = U(k+1:-1:k,:);
            P(k:k+1,:) = P(k+1:-1:k,:);
        endif

        % eliminate the elements below the pivot
        for i = k+1:m
            L(i,k)=U(i,k)/U(k,k);
            U(i,:) = U(i,:) - U(k,:)*(U(i,k)/U(k,k));
        endfor
    endfor
end