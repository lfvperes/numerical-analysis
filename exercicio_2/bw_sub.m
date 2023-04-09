function x = bw_sub(A, b)
    N = size(A)(1);
    % garantee b is vertical
    if (size(b)(1) == 1)
        b = b';
    endif

    % backward subtitution
    x = zeros(N, 1);
    for i = N:-1:1
        x(i) = (b(i) - A(i,i+1:N)*x(i+1:N)) / A(i, i);
    endfor
end