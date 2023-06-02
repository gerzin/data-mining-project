import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import time

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
    iqr = (df[column] > eps*q1) & (df[column] < eps*q3)
    return df.loc[iqr]
        

def print_metrics(X, kmeans):
    """print the metrics of the kmeans model.
    Parameters
    ----------
		X - normalized dataset
        kmeans - model.
    Prints
    ------
        K
        SSE
        Silhouette score
        Separation
    
    """
    print(f'K={len(kmeans.cluster_centers_)}')
    print('\tSSE:\t\t{}'.format(kmeans.inertia_))
    print('\tSilhouette:\t\t{}'.format(metrics.silhouette_score(X, kmeans.labels_)))
    print('\tDaviesBouldin score:\t\t{}'.format(metrics.davies_bouldin_score(X, kmeans.labels_)))
    
    
def run_kmeans(X, range_nclusters):
    '''runs kmeans for different values of k'''
    inertia, models = [], []
    for k in range_nclusters:
        k_means = KMeans(init='k-means++', n_clusters = k, n_init=20)
        model = k_means.fit(X) #returns fitted estimator
        models.append(model)
        inertia.append(k_means.inertia_)
    return inertia, models

def get_description_from_prodid(prodid, df):
    """returns the most probable description given the ProdID.
    Requires
    --------
        df to have a 'ProdID' and 'ProdDescr' column.
    """
    descrlist = df[df['ProdID'] == prodid ]['ProdDescr'].unique()
    return descrlist[0] if len(descrlist) > 0 else "NO DESCRIPTION AVAILBLE"

class Timer:
    def __init__(self):
        # name : time it took
        self.values = {}
        self. t = None
        self.name = None
    def start(self, name:str):
        self.name = name
        self.t = time.time()
    def stop(self):
        self.values[self.name] = (time.time() - self.t) * 1000
        self.t = None
        self.name = None
    def getValList(self):
        return list(self.values.items())

