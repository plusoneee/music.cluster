from Module import ClusterMethod



if __name__ == '__main__':
    csv_list = ['data/Dok2.csv', 'data/SoftLipa.csv']
    obj = ClusterMethod.KMeanClustering()
    obj.load_feature_csv_list(csv_list=csv_list)
    results = obj.k_mean_analyzing(k= 2, attr=['valence', 'speechiness'])
    print('Accuracy of Clustering:', results)
