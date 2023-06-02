import os
import pandas as pd
import pathlib

_THIS_MODULE_PARENT_FOLDER=pathlib.Path(__file__).parent.parent
DOWNLOAD_ROOT="http://didawiki.di.unipi.it/lib/exe/fetch.php/magistraleinformatica/dmi/"

CUSTOMER_PATH= os.path.join(_THIS_MODULE_PARENT_FOLDER, "datasets", "customer")
CUSTOMER_URL=DOWNLOAD_ROOT + "customer_supermarket.csv.zip"
CUSTOMER_DATASET_NAME="customer_supermarket.csv"
PREPROCESSED_DATASET_NAME=CUSTOMER_DATASET_NAME.replace(".csv","_preprocessed.csv" )
CLEAN_DATASET_NAME=CUSTOMER_DATASET_NAME.replace(".csv", "_clean.csv")
CUSTOMER_PROFILE_DATASET_NAME="customer_profile.csv"
CLUSTER_PROFILE_DATASET_NAME="customer_cluster.csv" 
ANNOTATED_CUSTOMER_PROFILE ="annotated_customer_profile.csv"
RFM_TIMESERIES_NAME_TEMPLATE="timeseries_{}.csv"
RFM_SCORE_TIMESERIES_NAME="rfmscoretimeseries.csv"
def fetch_customer_data(customer_url=CUSTOMER_URL, customer_path=CUSTOMER_PATH, dataset_name=CUSTOMER_DATASET_NAME, remove_zip=False):
    """downloads the customer_supermarket dataset if not already present.
    Parameters
    ----------
        customer_url - url of the dataset.
        customer_path - where to put the dataset.
        dataset_name - name of the dataset.
        remove_zip - set to True if you want to delete the downloaded zip archive.
    """
    os.makedirs(customer_path, exist_ok=True)
    if not os.path.isfile(customer_path + dataset_name):
        print("downloading the dataset")
        import urllib
        import zipfile
        zip_path=os.path.join(customer_path, dataset_name+".zip")
        urllib.request.urlretrieve(customer_url, zip_path)
        print("extracting "+str(zip_path))
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(path=customer_path)
        
        if remove_zip and os.path.isfile(zip_path):
            os.remove(zip_path)
            print("deleting " + str(zip_path))
            

        
        
def load_customer_data(dataset_name=CUSTOMER_DATASET_NAME, customer_path=CUSTOMER_PATH, convert_date=True):
    """loads the customer_supermarket dataset.
    Parameters
    ----------
        customer_path - path of the customer_supermarket.csv dataset.
        convert_date - set to True if you want to cast the BasketDate column to datetime.
    Returns
    -------
        DataFrame
    """
    csv_path= os.path.join(customer_path, dataset_name)
    tmp = pd.read_csv(csv_path, sep='\t', index_col=[0], skipinitialspace=True)
    try:
        # convert the date only if there's such a column and the flag is set
        if convert_date:
            tmp['BasketDate'] = pd.to_datetime(tmp['BasketDate'], dayfirst=True, infer_datetime_format=True)
    except:
        pass
    return tmp

def save_customer_dataset(dataset, file_name=PREPROCESSED_DATASET_NAME, dataset_path=CUSTOMER_PATH):
    """saves the dataset as a csv file.
    Parameters
    ----------
        dataset - DataFrame to save.
        dataset_path - path of the dataset.
        file_name - name of the file.
    """
    p = os.path.join(dataset_path, file_name)
    print(f"dataset saved to {p}")
    dataset.to_csv(p, sep='\t')

def save_rfm_timeseries(rec, freq, mv, name_template=RFM_TIMESERIES_NAME_TEMPLATE, dataset_path=CUSTOMER_PATH):
    """saves the recency, frequency and monetaryvalue datasets as three csv files."""
    rec_name = os.path.join(dataset_path, name_template.format("recency"))
    freq_name = os.path.join(dataset_path, name_template.format("frequency"))
    mv_name = os.path.join(dataset_path, name_template.format("monval"))

    rec.to_csv(rec_name, sep='\t')
    print(f"recency saved to {rec_name}")
    freq.to_csv(freq_name, sep='\t')
    print(f"frequency saved to {freq_name}")
    mv.to_csv(mv_name, sep='\t')
    print(f"monetary value saved to {mv_name}")

def load_rfm_timeseries(dataset_path=CUSTOMER_PATH, name_template=RFM_TIMESERIES_NAME_TEMPLATE):
    "loads the rfm datasets from the default location"
    rec_name = os.path.join(dataset_path, name_template.format("recency"))
    freq_name = os.path.join(dataset_path, name_template.format("frequency"))
    mv_name = os.path.join(dataset_path, name_template.format("monval"))

    rec = pd.read_csv(rec_name, index_col=[0], sep='\t')
    freq = pd.read_csv(freq_name, index_col=[0], sep='\t')
    mv = pd.read_csv(mv_name, index_col=[0], sep='\t')

    return rec, freq, mv

def save_rfmscore_timeseries(df, dataset_path=CUSTOMER_PATH, name=RFM_SCORE_TIMESERIES_NAME):
    """saves the rfmscore timeseries."""
    p = os.path.join(dataset_path, name)
    df.to_csv(p, sep='\t')

def load_rfmscore_timeseries(dataset_path=CUSTOMER_PATH, name=RFM_SCORE_TIMESERIES_NAME):
    """loads the rfm timeseries"""
    return pd.read_csv(os.path.join(dataset_path, name), index_col=[0], sep='\t')


