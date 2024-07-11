from django.shortcuts import render,redirect
import csv
import pandas as pd
import mysql.connector as con
import random
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

su=con.connect(host='localhost',user='root',password='pkroot',database='pkpay',auth_plugin='mysql_native_password')
cur=su.cursor()

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def clients(request):
    return render(request,"clients.html")

def contact(request):
    return render(request,"contact.html")

def invlg(request):
    return render(request,"invlg.html")


def signup(request):

    if request.method == 'POST':
        a=request.POST
        b=list(a.values())
        b.pop(0)
        idd=1
        print(b)
        cur.execute('select * from payments_signup')
        d=cur.fetchall()
        su.commit()
        e=[]
        for f in d:
            e.append(f)

        g=0
        for h in e:
            if h[1] in e:
                g=1
                break
            elif h[1] not in e:
                g=2     
        if g==2:
            cur.execute('select max(id) from payments_signup')
            i=cur.fetchall()
            su.commit()
            if i==():
                idd=0
            elif i!=():
                for j in i:
                    idd=j[0]     

            c="insert into payments_signup values({},'{}','{}','{}',{})".format(idd+1,b[0],b[1],b[2],int(b[3]))
            cur.execute(c)
            su.commit()
            return redirect('http://127.0.0.1:8000/index/login')
            

  
    return render(request,"signup.html")

def login(request):
    if request.method=='POST':
        lg1=request.POST
        lg2=list(lg1.values())
        print(lg2)
        cur.execute('select email,password,name1 from payments_signup')
        global ftch
        ftch=cur.fetchall()
        print(ftch)
        su.commit()
        global ep
        ep=[]

        for w in ftch:
            ep.append(w)
        for elm in ep:
            if (lg2[1] not in elm) and (lg2[2] not in elm):
                rlm=1
            elif (lg2[1] in elm) and (lg2[2] in elm):
                rlm=2
                break
        
        if rlm==1:
            return render(request,"invlg.html")
        elif rlm==2:
            ui='select id from payments_signup where email="{}"'.format(lg2[1])
            cur.execute(ui)
            global qw
            qw=cur.fetchall()
            su.commit()
            global kl
            kl=[]
            for hj in qw:
                for oi in hj:
                    kl.append(oi)


            global ty
            global flt
            flt=ep[kl[0]-1]
            ty={'name1':flt[2]}
            return redirect('http://127.0.0.1:8000/index/heyu')      
    
    return render(request,"login.html")



def mobile(request):
    if request.method=='POST':
        lk=request.POST
        global jh
        jh=list(lk.values())
        print(lk)
        jm=list(lk.keys())       
        jh.pop(0)
        print(jh)
        usa='select mob_num from ' + jh[1]
        global mer1
        mer1=jh[1]
        cur.execute(usa)
        vg=cur.fetchall()
        su.commit()
        mob=[]
        for i in vg:
            for k in i:
                mob.append(k)

        print(mob)

        m=10
        return redirect('http://127.0.0.1:8000/index/packs')

     
        
    return render(request,"mobile.html")

def money(request):
    return render(request,"money.html")
def heyu(request):

    return render(request,"heyu.html",ty)

def toll(request):
    if request.method=='POST':
        tq=request.POST
        print(tq)
        bt=list(tq.values())
        bt.pop(0)
        print(bt)
        st='select car_num from fastag'
        global mer1
        mer1='fastag'
        cur.execute(st)
        bz=cur.fetchall()
        su.commit()
        fas=[]
        for tol in bz:
            for pol in tol:
                fas.append(pol)
    
        print(fas)
        fy=bt[0].upper()
        if fy in fas:
            if int(bt[1])>100:
                uxe='select balance_amount from fastag where car_num="{}" '.format(bt[0])
                cur.execute(uxe)
                ah=cur.fetchall()
                su.commit()
                uxel=[]
                for mn in ah:
                    for kj in mn:
                        uxel.append(kj)
                
                print(uxel)
                upd1=float(uxel[0])+int(bt[1])
                gp='update fastag set balance_amount=' + str(upd1) +' where car_num="{}"'.format(bt[0])
                global rd
                rd=bt[1]
                cur.execute(gp)
                su.commit()
                if int(bt[1])>100:
                    return redirect('http://127.0.0.1:8000/index/paygate')



    return render(request,"toll.html")

def dth(request):
    if request.method=='POST':
        zi=request.POST
        print(zi)
        global qm
        qm=list(zi.values())
        qm.pop(0)
        print(qm)
        ao='select subscriber_id from ' + qm[1]
        global mer1
        mer1=qm[1]
        cur.execute(ao)
        zy=cur.fetchall()
        su.commit()
        cn=[]
        for fp in zy:
            for h in fp:
                cn.append(h)

        print(cn)
        return redirect('http://127.0.0.1:8000/index/amt')


    return render(request,"dth.html")

def amt(request):
    if request.method=='POST':
        nr=request.POST
        print(nr)
        an=list(nr.values())
        an.pop(0)
        print(an)
        if int(an[0])>100:
            wer='select balance_amt from '+qm[1]
            cur.execute(wer)
            vft=cur.fetchall()
            su.commit()
            qwe=[]
            for co in vft:
                for er in co:
                    qwe.append(er)
            print(qwe)
            upd=int(qwe[0])+int(an[0])
            zm='update '+ qm[1] + ' set balance_amt ={}'.format(upd)
            global rd
            rd=an[0]
            cur.execute(zm)
            su.commit()
            if int(an[0])>100:
                return redirect('http://127.0.0.1:8000/index/paygate')



    return render(request,"amt.html")

def packs(request):
        if request.method=='POST':
            gp=request.POST
            print(gp)
            aw=list(gp.values())
            aw.pop(0)
            print(aw)
            uk='update '+jh[1] + ' set present_pack="{}"'.format(aw[0])
            cur.execute(uk)
            su.commit()
            global rd
            rd=0
            if aw[0]=='Rs.999/3GB':
                rd=999
            elif aw[0]=='Rs.399/1.5GB':
                rd=399
            elif aw[0]=='Rs.499/2GB':
                rd=499

            return redirect('http://127.0.0.1:8000/index/paygate')
            




        return render(request,"packs.html")

def paygate(request):

    if request.method=='POST':
        ka=request.POST
        print(ka)
        global sg
        sg=list(ka.values())
        sg.pop(0)
        print(sg)
        jn='select * from '+ sg[4]
        print(sg[4])
        global crno
        crno=sg[0]
        cur.execute(jn)
        bx=cur.fetchall()
        su.commit
        global we
        we=list(bx[0])
        we.pop(0)
        print(we)
        global otp
        global email
        if (int(sg[0])==we[0]) and (sg[1]== we[1]) and (int(sg[2])== we[2]) and (sg[3]==we[3]):
            if sg[4]=='indusind':
                otp=random.randint(100000,999999)
                email=we[4]
                send_mail(
                            'Indusind bank payment OTP ',
                            str(otp) + ' is the OTP for your indusind bank payment. Please do not share this OTP with others ',
                            'pkpay.pkindustries@gmail.com',
                            [email]
                          )
        
                return redirect('http://127.0.0.1:8000/index/dybank')
            if sg[4]=='hdfc':
                otp=random.randint(100000,999999)
                email=we[4]
                send_mail(
                            'HDFC bank payment OTP ',
                            str(otp) + ' is the OTP for your hdfc bank payment.Please do not share this OTP with others ',
                            'pkpay.pkindustries@gmail.com',
                            [email]
                         )


                return redirect('http://127.0.0.1:8000/index/dybank2')
            if sg[4]=='axis':
                otp=random.randint(100000,999999)
                email=we[4]
                send_mail(
                            'Axis bank payment OTP ',
                            str(otp) + ' is the OTP for your axis bank payment.Please do not share this OTP with others ',
                            'pkpay.pkindustries@gmail.com',
                            [email]
                        )

                return redirect('http://127.0.0.1:8000/index/dybank3')

           

         
    return render(request,"paygate.html")


def chbank(request):
    return render(request,"chbank.html")



def dybank(request):
    
    if request.method=='POST':
        xz=request.POST
        print(xz)
        al=list(xz.values())
        al.pop(0)
        print(al)
        if al[0]==str(otp):
            send_mail(
                        'Thanks for choosing PKPay ',
                        'Your payment for Rs.' + str(rd) + ' at ' + mer1 + ' is successfull ',
                        'pkpay.pkindustries@gmail.com',
                        [email]
                    )

            cb='select current_balance_rs from ' +sg[4]
            cur.execute(cb)
            ab=cur.fetchall()
            su.commit()
            curb=[]
            
            for dl in ab:
                for cl in dl:
                    curb.append(cl)

        
            print(curb)
            if curb[0]>=int(rd):
                net=curb[0]-int(rd)
                print(net)
                netup='update '+sg[4] +' set current_balance_rs=' +str(net)+' where id=1'
                cur.execute(netup)
                su.commit()
                send_mail(
                        'Thanks for choosing PKPay ',
                        ' Your current balance is Rs.'+str(net),
                        'pkpay.pkindustries@gmail.com',
                        [email]
                    )

            return redirect('http://127.0.0.1:8000/index/paysuccess')
            if curb[0]<int(rd):
                send_mail(
                        'Thanks for choosing PKPay ',
                        ' Your current balance is not sufficient to make payments.Update your balance and try again'
                        'pkpay.pkindustries@gmail.com',
                        [email]
                    )

                return redirect('http://127.0.0.1:8000/index/payfail')


        if al[0]!=str(otp):
            send_mail(
                        'Thanks for choosing PKPay ',
                        'Your payment for Rs.' + str(rd) + ' at ' + mer1 + ' failed.Try again',
                        'pkpay.pkindustries@gmail.com',
                        [email]
                    )
            return redirect('http://127.0.0.1:8000/index/payfail')



    dk={'mer':mer1,'crd':crno,'oamt':rd}
    return render(request,"dybank.html",dk)


def dybank2(request):

    if request.method=='POST':
        xz=request.POST
        print(xz)
        al=list(xz.values())
        al.pop(0)
        print(al)
        if al[0]==str(otp):
            send_mail(
                        'Thanks for choosing PKPay ',
                        'Your payment for Rs.' +str(rd)+ ' at'+ mer1 +' is successfull ',
                        'pkpay.pkindustries@gmail.com',
                        [email]
                    )
            cb='select current_balance_rs from ' +sg[4]
            cur.execute(cb)
            ab=cur.fetchall()
            su.commit()
            curb=[]
            
            for dl in ab:
                for cl in dl:
                    curb.append(cl)

            
            print(curb)
            if curb[0]>=int(rd):
                net=curb[0]-int(rd)
                print(net)
                netup='update '+sg[4] +' set current_balance_rs=' +str(net)+' where id=1'
                cur.execute(netup)
                su.commit()
                send_mail(
                        'Thanks for choosing PKPay ',
                        ' Your current balance is Rs.'+str(net),
                        'pkpay.pkindustries@gmail.com',
                        [email]
                    )

            return redirect('http://127.0.0.1:8000/index/paysuccess')
            if curb[0]<int(rd):
                send_mail(
                        'Thanks for choosing PKPay ',
                        ' Your current balance is not sufficient to make payments.Update your balance and try again'
                        'pkpay.pkindustries@gmail.com',
                        [email]
                    )

                return redirect('http://127.0.0.1:8000/index/payfail')
        if al[0]!=str(otp):
                send_mail(
                            'Thanks for choosing PKPay ',
                            'Your payment for Rs.' + str(rd) + ' at ' + mer1 + ' failed.Try again',
                            'pkpay.pkindustries@gmail.com',
                            [email]
                        )
                return redirect('http://127.0.0.1:8000/index/payfail')


    dk={'mer':mer1,'crd':crno,'oamt':rd}
    return render(request,"dybank2.html",dk)

def dybank3(request):
    if request.method=='POST':
        xz=request.POST
        print(xz)
        al=list(xz.values())
        al.pop(0)
        print(al)
        if al[0]==str(otp):
            send_mail(
                        'Thanks for choosing PKPay ',
                        'Your payment for Rs.'+str(rd)+' at '+ mer1 +'is successfull ',
                        'pkpay.pkindustries@gmail.com',
                        [email]
                    )
            cb='select current_balance_rs from ' +sg[4]
            cur.execute(cb)
            ab=cur.fetchall()
            su.commit()
            curb=[]
            
            for dl in ab:
                for cl in dl:
                    curb.append(cl)

            print(curb)
            print(rd)
            if curb[0]>=int(rd):
                net=curb[0]-int(rd)
                print(net)
                netup='update '+sg[4] +' set current_balance_rs=' +str(net)+' where id=1'
                cur.execute(netup)
                su.commit()
                send_mail(
                        'Thanks for choosing PKPay ',
                        ' Your current balance is Rs.'+str(net),
                        'pkpay.pkindustries@gmail.com',
                        [email]
                    )

            return redirect('http://127.0.0.1:8000/index/paysuccess')
            if curb[0]<int(rd):
                send_mail(
                        'Thanks for choosing PKPay ',
                        ' Your current balance is not sufficient to make payments.Update your balance and try again'
                        'pkpay.pkindustries@gmail.com',
                        [email]
                    )

                return redirect('http://127.0.0.1:8000/index/payfail')
        if al[0]!=str(otp):
                send_mail(
                            'Thanks for choosing PKPay ',
                            'Your payment for Rs.' + str(rd) + ' at ' + mer1 + ' failed.Try again',
                            'pkpay.pkindustries@gmail.com',
                            [email]
                        )
                return redirect('http://127.0.0.1:8000/index/payfail')


    dk={'mer':mer1,'crd':crno,'oamt':rd}
    return render(request,"dybank3.html",dk)

def paysuccess(request):
    return render(request,"paysuccess.html")

def payfail(request):
    return render(request,"payfail.html")

