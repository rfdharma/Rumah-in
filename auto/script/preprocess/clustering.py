import pickle

def labeling(df):
    df = df.rename(str,axis="columns") 
    df.drop(columns=['judul','link','images_link','kecamatan_1','latitude','longitude','label'],inplace=True)

    with open('../web/resource/scaler/scaler.pkl', 'rb') as sc:
        scal = pickle.load(sc)
        X = scal.transform(df)

    with open('../web/resource/clustermodel/kmeans_model.pkl', 'rb') as f:
        cluster = pickle.load(f)
        hasil = cluster.predict(X)

    return hasil