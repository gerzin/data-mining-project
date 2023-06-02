import pandas as pd

def get_subset_by_IQR(df,column, eps=1.5):
    """ returns a subset of the dataframe with the elements of column "between" the 1st and 3rd quantile.
    Parameters
    ----------
        df - Dataframe
        column - name of the column
        eps - epsilon value for increment or decrement the range of the quantiles
    Returns
    -------
        Subset of the original dataframe
    Example
    -------
        df = get_subset_by_IQR(df, "I", eps=1.7)
    """
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = (eps*df[column] > q1) & (df[column] < eps*q3)
    return df.loc[iqr]
