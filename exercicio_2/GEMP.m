function A = GEMP(A)
    [m, n] = size(A);

    for k = 1:m-1
        % pivoting
        if (A(k,k) == 0)
            A(k:k+1,:) = A(k+1:-1:k,:);
        endif

        % eliminate the elements below the pivot
        for i = k+1:m
            A(i,:) = A(i,:) - A(k,:)*(A(i,k)/A(k,k));
        endfor
    endfor
end