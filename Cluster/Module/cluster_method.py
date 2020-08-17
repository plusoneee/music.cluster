import pandas as pd
from sklearn import preprocessing
from sklearn import cluster

class KMeanClustering():

    def __init__(self):
        self.zscore = preprocessing.StandardScaler()
        self.frames = []
        self.csv_col_num = []
        self.real_label =[]

    def load_feature_csv_list(self, csv_list=None):
        if csv_list is None:
            csv_list = [
                './data/Dok2.csv', './data/SoftLipa.csv'
            ]
        for item_path in csv_list:
            df = pd.read_csv(item_path)
            self.csv_col_num.append(len(df))
            self.frames.append(df)
        
        self.frames = pd.concat(self.frames)
        
    def k_mean_analyzing(self, k, attr=[]):
        feature_df = self.frames[attr]
        data_zs = self.zscore.fit_transform(feature_df)
        kmeans_fit = cluster.KMeans(n_clusters = 2).fit(data_zs)
        cluster_labels = kmeans_fit.labels_
        print("Clustering Results：")
        print("K : ", k, " | Total : ", len(cluster_labels))
        print(list(cluster_labels))
    
        acurr = self.verification(k=k, cluster_labels=cluster_labels)
        return acurr

    def verification(self, k, cluster_labels):

        # create real label
        for kth in range(k):
            for num in range(self.csv_col_num[kth]):
                self.real_label.append(kth)

        def compute_score():
            scores = []
            score = 0
            length = sum(self.csv_col_num)
            for kth in range(k):
                for i in range(len(cluster_labels)):
                    if cluster_labels[i] == self.real_label[i]: 
                        score = score+1
                score = score/(length-1)
                scores.append(score)
                if score < 0.5:
                    for index in range(len(self.real_label)):
                        if self.real_label[index] == 0:
                            self.real_label[index] = 1
                        elif self.real_label[index] == 1:
                            self.real_label[index] = 0
            print(self.real_label)
            return max(scores)

        return compute_score()

