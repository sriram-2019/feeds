from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from feed.models import Students
from feed.models import Entry
from django.db.models import Avg
from django.db.models import Sum, Count
import pandas as pd

# Create your views here.

from django.db import connection

# Your Django code here

# Display executed queries
queries = connection.queries
for query in queries:
    print(query)

def index(request):
    return render(request,"index.html")
def second_page(request):
    name=(request.POST.get("rollNumber"))
    request.session["name"]=name
    password=(request.POST.get("password"))
    if(password.lower()==name):
        data={'message':"success"}
    else:
        data={"message":"fail"}
    return JsonResponse(data)
def second_pages(request):
    name=request.session.get("name")
    save = Students.objects.filter(reg=f"{name}").values('reg', 'deptid',"name","yearid")
    
    reg=(save[0]['reg'])       # Access the 'reg' field for the first student
    dept=(save[0]['deptid'])
    year=save[0]["yearid"]
    if(int(dept)==1 ):
        dept="CSE"
    elif(int(dept)==2):
        dept="IT"  
    elif(int(dept)==3):
        dept="ECE"
    else:
        dept="-"  # Access the 'deptid' field for the first student
    name=(save[0]['name'])
    context = {
            'reg': reg,
            'dept': dept,
            'name': name,
            'year':year
        }
    return render(request,"second.html",context)
def surveypage(request):
    
    return JsonResponse({"message":"success"})
def surveypages(request):
    
    return render(request,"question.html")
def getdata(request):
    if request.method == "POST":
        name=request.session.get("name")
        name1=Students.objects.filter(reg=f"{name}").values('name')
        print(name1)
        save = Students.objects.filter(reg=f"{name}").values('reg', 'deptid',"name","yearid")
        reg=(save[0]['reg'])       # Access the 'reg' field for the first student
        dept=(save[0]['deptid'])
        year=save[0]["yearid"]
        if(int(dept)==1 ):
            dept="CSE"
        elif(int(dept)==2):
            dept="IT"  
        elif(int(dept)==3):
            dept="ECE"
        else:
            dept="-" 
        question1 = request.POST.get("question1")
        question2 = request.POST.get("question1")
        question3 = request.POST.get("question2")
        question4 = request.POST.get("question3")
        question5 = request.POST.get("question4")
        question6 = request.POST.get("question5")
        question7 = request.POST.get("question6")
        question8 = request.POST.get("question7")
        question9 = request.POST.get("question8")
        question10 = request.POST.get("question9")
        question11 = request.POST.get("question10")
        question12 = request.POST.get("question11")
        question13 = request.POST.get("question12")
        question14 = request.POST.get("question13")
        question15 = request.POST.get("question14")
        question16 = request.POST.get("question15")
        question17 = request.POST.get("question16")
        question18 = request.POST.get("question17")
        question19 = request.POST.get("question18")
        question20 = request.POST.get("question19")
        s=Entry(name=name1,reg=reg,dept=dept,year=year,question1=question1,question2=question2,question3=question3,question4=question4,question5=question5,question6=question6,question7=question7,question8=question8,question9=question9,question10=question10,question11=question11,question12=question12,question13=question13,question14=question14,question15=question15,question16=question16,question17=question17,question18=question18,question19=question19,question20=question20)
        s.save()
        response_data = {
            'message': 'Data received successfully',
        }
        return JsonResponse(response_data)
    else:
        # Handle GET request or other HTTP methods
        return JsonResponse({'error': 'Invalid request method'})
def bars(request):
    quet1=[]
    quet2=[]
    quet3=[]
    quet4=[]
    quet5=[]
    quet6=[]
    quet7=[]
    quet8=[]
    quet9=[]
    quet10=[]
    quet11=[]
    quet12=[]
    quet13=[]
    quet14=[]
    quet15=[]
    quet16=[]
    quet17=[]
    quet18=[]
    quet19=[]
    quet20=[]
    total_students1 = Entry.objects.count()
    total_cse=Entry.objects.filter(dept="CSE").count()
    total_it=Entry.objects.filter(dept="IT").count()
    total_ece=Entry.objects.filter(dept="ECE").count()
    total_students=total_students1*5
    total_question1 = Entry.objects.aggregate(sum_question1=Sum('question1'))['sum_question1']
    total_question2 = Entry.objects.aggregate(sum_question1=Sum('question2'))['sum_question1']
    total_question3 = Entry.objects.aggregate(sum_question1=Sum('question3'))['sum_question1']
    total_question4 = Entry.objects.aggregate(sum_question1=Sum('question4'))['sum_question1']
    total_question5 = Entry.objects.aggregate(sum_question1=Sum('question5'))['sum_question1']
    total_question6 = Entry.objects.aggregate(sum_question1=Sum('question6'))['sum_question1']
    total_question7 = Entry.objects.aggregate(sum_question1=Sum('question7'))['sum_question1']
    total_question8 = Entry.objects.aggregate(sum_question1=Sum('question8'))['sum_question1']
    total_question9 = Entry.objects.aggregate(sum_question1=Sum('question9'))['sum_question1']
    total_question10 = Entry.objects.aggregate(sum_question1=Sum('question10'))['sum_question1']
    total_question11= Entry.objects.aggregate(sum_question1=Sum('question11'))['sum_question1']
    total_question12= Entry.objects.aggregate(sum_question1=Sum('question12'))['sum_question1']
    total_question13= Entry.objects.aggregate(sum_question1=Sum('question13'))['sum_question1']
    total_question14= Entry.objects.aggregate(sum_question1=Sum('question14'))['sum_question1']
    total_question15= Entry.objects.aggregate(sum_question1=Sum('question15'))['sum_question1']
    total_question16= Entry.objects.aggregate(sum_question1=Sum('question16'))['sum_question1']
    total_question17= Entry.objects.aggregate(sum_question1=Sum('question17'))['sum_question1']
    total_question18= Entry.objects.aggregate(sum_question1=Sum('question18'))['sum_question1']
    total_question19= Entry.objects.aggregate(sum_question1=Sum('question19'))['sum_question1']
    total_question20= Entry.objects.aggregate(sum_question1=Sum('question20'))['sum_question1']
    average_question1 = (total_question1 / total_students)*100
    average_question2 = (total_question2 / total_students)*100
    average_question3 = (total_question3 / total_students)*100
    average_question4 = (total_question4 / total_students)*100
    average_question5 = (total_question5 / total_students)*100
    average_question6 = (total_question6 / total_students)*100
    average_question7= (total_question7 / total_students)*100
    average_question8 = (total_question8 / total_students)*100
    average_question9 = (total_question9 / total_students)*100
    average_question10 = (total_question10 / total_students)*100
    average_question11 = (total_question11/ total_students)*100
    average_question12 = (total_question12 / total_students)*100
    average_question13 = (total_question13 / total_students)*100
    average_question14 = (total_question14 / total_students)*100
    average_question15 = (total_question15 / total_students)*100
    average_question16 = (total_question16 / total_students)*100
    average_question17 = (total_question17 / total_students)*100
    average_question18 = (total_question18 / total_students)*100
    average_question19 = (total_question19 / total_students)*100
    average_question20= (total_question20 / total_students)*100
# Calculate the average for question1 based on the total and number of entries


# Append the result to the quet1 list   
    quet1.append(average_question1)
    quet2.append(average_question2)
    quet3.append(average_question3)
    quet4.append(average_question4)
    quet5.append(average_question5)
    quet6.append(average_question6)
    quet7.append(average_question7)
    quet8.append(average_question8)
    quet9.append(average_question9)
    quet10.append(average_question10)
    quet11.append(average_question11)
    quet12.append(average_question12)
    quet13.append(average_question13)
    quet14.append(average_question14)
    quet15.append(average_question15)
    quet16.append(average_question16)
    quet17.append(average_question17)
    quet18.append(average_question18)
    quet19.append(average_question19)
    quet20.append(average_question20)
    context={
        "totalcse":total_cse,
        "totalit":total_it,
        "totalece":total_ece,
        "mes":quet1,
        "mes1":quet2,
        "mes3":quet3,
        "mes4":quet4,
        "mes5":quet5,
        "mes6":quet6,
        "mes7":quet7,
        "mes8":quet8,
        "mes9":quet9,
        "mes10":quet10,
        "mes11":quet11,
        "mes12":quet12,
        "mes13":quet13,
        "mes14":quet14,
        "mes15":quet15,
        "mes16":quet16,
        "mes17":quet17,
        "mes18":quet18,
        "mes19":quet19,
        "mes20":quet20,
    }
    return render(request,"bar.html",context)
def logout(request):
    return render(request,"index.html")
def disp(request):
    return render(request,"but.html")
def display(request):
    return render(request,"button.html")
def display1(request):
    
    request.session["dept"]="CSE"
    get_name=Entry.objects.filter(dept="CSE").values("name","reg","dept","year","question1","question2","question3","question4","question5","question6","question7","question8","question9","question10","question11","question12","question13","question14","question15","question16","question17","question18","question19","question20")
   
    averages = get_name.aggregate(
        avg_question1=Avg("question1"),
        avg_question2=Avg("question2"),
        avg_question3=Avg("question3"),
        avg_question4=Avg("question4"),
        avg_question5=Avg("question5"),
        avg_question6=Avg("question6"),
        avg_question7=Avg("question7"),
        avg_question8=Avg("question8"),
        avg_question9=Avg("question9"),
        avg_question10=Avg("question10"),
        avg_question11=Avg("question11"),
        avg_question12=Avg("question12"),
        avg_question13=Avg("question13"),
        avg_question14=Avg("question14"),
        avg_question15=Avg("question15"),
        avg_question16=Avg("question16"),
        avg_question17=Avg("question17"),
        avg_question18=Avg("question18"),
        avg_question19=Avg("question19"),
        avg_question20=Avg("question20")
    )
    
    c = {
        "name": get_name,
        "averages": averages  # Pass the calculated averages to the template
    }
    return render(request,"display.html",c)
def display2(request):
    request.session["dept"]="IT"
    
    get_name=Entry.objects.filter(dept="IT").values("name","reg","dept","year","question1","question2","question3","question4","question5","question6","question7","question8","question9","question10","question11","question12","question13","question14","question15","question16","question17","question18","question19","question20")
   
    c={
        "name":get_name
    }
    return render(request,"display.html",c)
def display3(request):
    request.session["dept"]="ECE"
    get_name=Entry.objects.filter(dept="ECE").values("name","reg","dept","year","question1","question2","question3","question4","question5","question6","question7","question8","question9","question10","question11","question12","question13","question14","question15","question16","question17","question18","question19","question20")
   
    c={
        "name":get_name
    }
    return render(request,"display.html",c)
def display4(request):
    request.session["dept"]="EEE"
    get_name=Entry.objects.filter(dept="EEE").values("name","reg","dept","year","question1","question2","question3","question4","question5","question6","question7","question8","question9","question10","question11","question12","question13","question14","question15","question16","question17","question18","question19","question20")
   
    c={
        "name":get_name
    }
    return render(request,"display.html",c)
def dipslayo(request):
    return render(request,"bar.html")
def excel(request):
    dept=request.session.get("dept")
    
    download=Entry.objects.filter(dept=dept).values("name","reg","dept","year","question1","question2","question3","question4","question5","question6","question7","question8","question9","question10","question11","question12","question13","question14","question15","question16","question17","question18","question19","question20")
    df = pd.DataFrame(download)
    df = df.rename(columns={
        "name": "Name",
        "reg": "reg",
        "dept": "Dept",
        "year": "Year",
        "question1": "Q1",
        "question2": "Q2",
        "question3": "Q3",
        "question4": "Q4",
        "question5": "Q5",
        "question6": "Q6",
        "question7": "Q7",
        "question8": "Q8",
        "question9": "Q9",
        "question10": "Q10",
        "question11": "Q11",
        "question12": "Q12",
        "question13": "Q13",
        "question14": "Q14",
        "question15": "Q15",
        "question16": "Q16",
        "question17": "Q17",
        "question18": "Q18",
        "question19": "Q19",
        "question20": "Q20"
    })
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    # Write the DataFrame to the response as an Excel file
    df.to_excel(response, index=False,engine='openpyxl')
    return response