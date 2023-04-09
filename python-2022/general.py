
def rel_err(x_1: float, x_0: float) -> float:
    """Relative error. Used to measure the precision between iterations.

    Parameters
    ----------
    x_1 : float
        _description_
    x_0 : float
        _description_

    Returns
    -------
    float
        _description_
    """
    return abs(x_1 - x_0)/abs(x_1)
