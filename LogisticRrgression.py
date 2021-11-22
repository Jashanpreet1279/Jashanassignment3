import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score


def evaluate(X, y, X_test):
    st.subheader('Evaluting Data with Logistic Regrassion')
    model = LogisticRegression(C=0.10, max_iter=100)
    model.fit(X, y)
    return model.predict(X_test)

def analyse(X_train, X_test, y_train, y_test, class_names, plot_metrics):
    st.sidebar.subheader('Model Hyperparameters')
    c = st.sidebar.number_input('c (Regularization parameter)', 0.01, 10.0, step=0.01, key='c_LR')
    max_iter = st.sidebar.slider('Maximum Number of Iterations', 100, 500, key='max_iter')


    metrics = st.sidebar.multiselect('What metrics to plot?', 
                                    ('Select All', 'Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'), default=['Select All'])
    if 'Select All' in metrics:
        metrics = ['Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve']
            

    if st.sidebar.button('Classify', key='classify'):
        st.subheader('Logistic Regrassion Results')
        model = LogisticRegression(C=c, max_iter=max_iter)
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)
        y_pred = model.predict(X_test)
        st.write('Accuracy: ', accuracy.round(2))
        st.write('Precision: ', precision_score(y_test, y_pred, labels=class_names).round(2))
        st.write('Recall: ', recall_score(y_test, y_pred, labels=class_names).round(2))
        plot_metrics(metrics, model)
