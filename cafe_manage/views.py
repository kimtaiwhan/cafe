from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
import random

config = {
    "apiKey": "AIzaSyCjrDy4XEJyLEIY2jIdkgeHGKGEH8yXHY8",
    "authDomain": "cafe-2bd41.firebaseapp.com",
    "databaseURL": "https://cafe-2bd41-default-rtdb.firebaseio.com",
    "projectId": "cafe-2bd41",
    "storageBucket": "cafe-2bd41.appspot.com",
    "messagingSenderId": "638931578152",
    "appId": "1:638931578152:web:71907b37bfc07cc84b341d",
    "measurementId": "G-7GSXPMHLG8"
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

def main(request):
    return render(request, 'cafe_manage/main.html', {
                                                        "address" : '울산광역시 남구 대학로 93',
                                                        "시" : '울산광역시',
                                                        "구" : '남구',
                                                        "도로명" : '대학로 93',
                                                        "지번" : '무거동 665',
                                                        "우편번호" : '44610',
                                                        "phone" : '(052) 277-3101'
                                                    })

def signIn(request):
    return render(request, 'cafe_manage/signIn.html')

def postsignIn(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        user = auth.sign_in_with_email_and_password(email, pasw)
    except:
        message = "Invalid Credentals!!Please Cheack your Data"
        return render(request, 'cafe_manage/signIn.html', {"message" : message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, 'cafe_manage/main.html', {  
                                                        "email" : email,
                                                        "address" : '울산광역시 남구 대학로 93',
                                                        "시" : '울산광역시',
                                                        "구" : '남구',
                                                        "도로명" : '대학로 93',
                                                        "지번" : '무거동 665',
                                                        "우편번호" : '44610',
                                                        "phone" : '(052) 277-3101'
                                                    })

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, 'cafe_manage/signIn.html')

def signUp(request):
    return render(request, 'cafe_manage/signUp.html')

def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    try:
        user = auth.create_user_with_email_and_password(email, passs)
        uid = user['localID']
        idtoken = request.session['uid']
        print(uid)
    except:
        return render(request, 'cafe_manage/signUp.html')
    return render(request, 'cafe_manage/signIn.html')

def chart(request):
    #b = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    #avg_stay = {"9" : 0, "10" : 0, "11" : 0, "12" : 0, "13" : 0, "14" : 0, "15" : 0, "16" : 0, "17" : 0, "18" : 0, "19" : 0, "20" : 0, "21" : 0}
    #
    #count = 0
    #temp_stay = 0
#
    #for i in range (0, 13):
    #    data = datas.find({"hour" : b[i]})
#
    #    for cnpz in data:
    #        #year = cnpz["year"]
    #        #month = cnpz["month"]
    #        #day = cnpz["day"]
    #        #week = cnpz["요일"]
    #        #hour = cnpz["hour"]
    #        #temp_enter = cnpz["total_enter"]
    #        #temp_exit = cnpz["total_exit"]
    #        temp_stay += cnpz["total_stay"]
#
    #        count += 1
#
    #    avg_stay[str(b[i])] = temp_stay // count
#
    #    temp_stay = 0
    #    count = 0

    return render(request, 'cafe_manage/chart.html', {
                                                        "time_9" : random.randrange(20, 50),
                                                        "time_10" : random.randrange(20, 50),
                                                        "time_11" : random.randrange(20, 50),
                                                        "time_12" : random.randrange(20, 50),
                                                        "time_13" : random.randrange(20, 50),
                                                        "time_14" : random.randrange(20, 50),
                                                        "time_15" : random.randrange(20, 50),
                                                        "time_16" : random.randrange(20, 50),
                                                        "time_17" : random.randrange(20, 50),
                                                        "time_18" : random.randrange(20, 50),
                                                        "time_19" : random.randrange(20, 50),
                                                        "time_20" : random.randrange(20, 50),
                                                        "time_21" : random.randrange(20, 50)})

def review(request):
    return render(request, 'cafe_manage/review.html')

def test(request):
    return render(request, 'cafe_manage/test.html')