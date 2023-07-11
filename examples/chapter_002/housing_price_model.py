from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder


# Step 2. Retrieving & Understanding the Data


def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        # Create 'datasets' if it does not exist
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))


def descriptive_statistics(data):
    print(data.head())
    print(data.info())
    print(data.describe())

    plt.rc('font', size=14)
    plt.rc('axes', labelsize=14, titlesize=14)
    plt.rc('legend', fontsize=14)
    plt.rc('xtick', labelsize=10)
    plt.rc('ytick', labelsize=10)
    data.hist(bins=50, figsize=(12, 8))
    plt.show()


def stratified_sampling(data):
    data["income_cat"] = pd.cut(data["median_income"],
                                bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                labels=[1, 2, 3, 4, 5])

    # data["income_cat"].value_counts().sort_index().plot.bar(rot=0, grid=True)
    # plt.xlabel("Income category")
    # plt.ylabel("Number of districts")
    # plt.show()

    strat_train_set, strat_test_set = train_test_split(
        housing, test_size=0.2, stratify=data["income_cat"], random_state=42)

    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)

    return strat_train_set, strat_test_set


def data_visualisation(data):
    data.plot(
        kind="scatter",
        x="longitude",
        y="latitude",
        grid=True,
        alpha=0.2)
    plt.show()

    data.plot(kind="scatter", x="longitude", y="latitude", grid=True,
              s=data["population"] / 100, label="population",
              c="median_house_value", cmap="jet", colorbar=True,
              legend=True, sharex=False, figsize=(10, 7))
    plt.show()


def data_correlations(data):
    data_num = data.select_dtypes(include=[np.number])
    corr_matrix = data_num.corr()
    print(corr_matrix["median_house_value"].sort_values(ascending=False))

    # "median_house_value", "median_income",
    # "total_rooms", "housing_median_age"
    # are promising attributes with high correlations

    attributes = ["median_house_value", "median_income", "total_rooms",
                  "housing_median_age"]
    scatter_matrix(data[attributes], figsize=(12, 8))
    plt.show()

    data.plot(kind="scatter", x="median_income", y="median_house_value",
              alpha=0.1, grid=True)
    plt.show()


# load the data
housing = load_housing_data()

housing["rooms_per_house"] = housing["total_rooms"] / housing["households"]
housing["bedrooms_ratio"] = housing["total_bedrooms"] / housing["total_rooms"]
housing["people_per_house"] = housing["population"] / housing["households"]

# understand the data
descriptive_statistics(housing)

# stratify into representative testing and training samples
strat_train_set, strat_test_set = stratified_sampling(housing)

# Visualising the data to gain insights
data_visualisation(housing)

# look for correlations
data_correlations(housing)

housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()
housing_num = housing.select_dtypes(include=[np.number])

imputer = SimpleImputer(strategy="median")
imputer.fit(housing_num)
X = imputer.transform(housing_num)

housing_tr = pd.DataFrame(X, columns=housing_num.columns,
                          index=housing_num.index)

# Categorical Data
housing_cat = housing[["ocean_proximity"]]
housing_cat.head(8)
cat_encoder = OneHotEncoder()
housing_cat_1hot = cat_encoder.fit_transform(housing_cat)
housing_cat_1hot = housing_cat_1hot.toarray()
print(housing_cat_1hot)
