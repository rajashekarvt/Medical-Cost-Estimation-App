from django.shortcuts import render, redirect
import pickle
import pandas as pd


def index_func(request):
    res = 0
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        sex = request.POST['sex']  # select
        bmi = request.POST['bmi']
        children = request.POST['children']
        smoker = request.POST['smoker']  # select
        region = request.POST['region']  # select

        if name != "":
            df = pd.DataFrame(
                columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
            df2 = {'age': int(age), 'sex': int(sex), 'bmi': float(bmi), 'children': int(
                children), 'smoker': int(smoker), 'region': int(region)}
            df = df.append(df2, ignore_index=True)

            filename = 'polls/model.pkl'
            model = pickle.load(open(filename, 'rb'))
            res = model.predict(df)
            print(res)
        else:
            return redirect('homepage')
    else:
        pass

    return render(request, 'index.html', {'response': res})
