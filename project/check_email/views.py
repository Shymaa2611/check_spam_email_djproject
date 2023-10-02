from django.shortcuts import render
from .forms import emailForm
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split


def check_email(request,email):
    data=pd.read_csv('check_email//smsspamcollection.tsv',sep='\t')
    x=data['message']
    y=data['label']
    x_train,x_test,y_train,y_test= train_test_split(x, y, test_size=0.25, random_state=42)
    text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                     ('clf', LinearSVC()),])
    text_clf.fit(x_train, y_train) 
    predict=text_clf.predict([email])
    return predict

def index(request):
    predict=None
    if request.method=='POST':
        form=emailForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data['email']
            predict=check_email(request,email)
    else:
        form=emailForm()
    context={
        'form':form,
        'predict':predict
    }
    return render(request,'index.html',context)



     

