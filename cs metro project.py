import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",passwd="pawan",database="metroproject")
cur=connection.cursor()
q=0
lmfaoo=0
sos=0
while q <4:
    print("\n")
    print("--------------welcome to delhi metro---------------")
    print("\n")
    print("menu")
    print("\n")
    print("new user: press(1)")
    print("\n")
    print("existing user: press(2)")
    print("\n")
    print("admin: press(3)")
    print("\n")
    print("to terminate program: press(4)")
    print("\n")
    b=int(input("enter your input:"))
    if b==1:
        mdetails=[]
        f=0
        print("As a new user, You have to create an account first. Proceed further by providing us with your details. ")
        print('Please add all your Details Carefully without any Mistake')
        print('\n')
        name=input("please enter your full name")
        cellno=int(input("please enter your contact number"))
        while f<1:
            pass1=int(input("enter your 4 digit password"))
            print("\n")
            if len(str(pass1)) == 4:
                pass2=int(input("please re-enter your password"))
                if pass1==pass2:
                    mdetails.append(name)
                    mdetails.append(cellno)
                    mdetails.append(pass1)
                    mdetails.append(150)
                    cd=mdetails
                    cd=(cd)
                    comm1="insert into metro(name,cellno,passwd,balance)values (%s,%s,%s,%s)"
                    cur.execute(comm1,cd)
                    connection.commit()
                    f=1
                    print("welcome",name,"your account has been successfully created")
                    
                else:
                    print('Oops, We told you to be careful, Please give your full attention here for a minute.')
                    print("Passwords doesn't match, Please Retry and enter a combination of matching Passwords.")
                    print("\n")
            else:
                 print("invalid password length")
                 print("please enter a four digit password")

                              
    if b==2:
        r=0
        while r<1:
            cellno=int(input("please enter your phone(cell) number"))
            print("\n")
            pwd=int(input("please enter your password"))
            print("\n")
            commpas = " select passwd from metro where cellno = %s "
            commname = " select name from metro where cellno = %s "
            commbal = " select balance from metro where cellno = %s "
            cur.execute(commpas,(cellno,))
            f1=cur.fetchall()
            f12=f1[0]
            resultpas=f12[0]
            k=int(resultpas)
            cur.execute(commname,(cellno,))
            g1=cur.fetchall()
            g12=g1[0]
            resultname=g12[0]
            cur.execute(commbal,(cellno,))
            h1=cur.fetchall()
            h12=h1[0]
            resultbal=h12[0]
            if pwd == k :
                r=4
                d=0
                print("\t    Welcome",resultname,"Your Account Balance is",resultbal)
                while d<1:
                    print('\n')
                    print("For Travel : Press (1)")
                    print('\n')
                    print("For Recharge : Press (2)")
                    print('\n')
                    print('To See Metro Route Map :Press (3)')
                    print("For Information : Press (4)")
                    print('\n')
                    print("To Know about DMRC : Press (5)")
                    print('\n')
                    print("For Contact Details : Press (6)")
                    print('\n')
                    print("For Deactivation of your Account : Press (7)")
                    print('\n')
                    print("For Main Menu : Press (Any Other Number)")
                    print('\n')
                    print("For Help : Go to your nearest help desk or Contact Us")
                    p=int(input("please enter your choice"))
                    if p==2:
                        j1=int(input("please enter the amount to be added in your account"))
                        newbal=j1 + resultbal
                        commnbal="update metro set balance=%s where cellno=%s"
                        cur.execute(commnbal,(newbal,cellno,))
                        connection.commit()
                        print("Your balance has been updated succesfully. Your new balance is ",newbal)                                                                                        
                        print('\n')
                        commuptrans=" insert into rechargedetails (cellno,name,balance_before,recharge_amount,balance_after) values (%s,%s,%s,%s,%s)"
                        cur.execute(commuptrans,(cellno,resultname,resultbal,j1,newbal,))
                        connection.commit()
                        cedit="update metro set balance=%s where cellno=%s"
                        cur.execute(cedit,(newbal,cellno))
                        connection.commit()
                        resultbal=newbal
                    if  p==3:
                        k=open("D:\\metro.txt","r")
                        print(k.read())
                    
                    if p==4:
                        print( "Information")
                        print('\n')
                        print("Automatic Ticketing")
                        print('\n')
                        print("Delhi Metro has introduced, for the first time in the country, ticketing andpassenger control through a completely Automatic Fare Collection system. ")
                        print('\n')
                        print('''The ticket which could be a token or card is purchased from the Ticket Counter or Customer Care Centre. Subsequently,
                                    the passenger proceeds to one of several gates that separate the Paid Area from the Unpaid Area.
                                    Here, the passenger will hold the ticket close to the machine to the right of the gate.
                                    If valid, the gates will open automatically, and the passenger can pass to the Paid Area.
                                    If not valid, then the passenger will need to contact the Customer Care Staff.''')
                        print('\n')
                        print("Ticket Options")
                        print('\n')
                        print("(A) Smart Card :")
                        print("\n")
                        print('''It is the most convenient for frequent commuters.
                                     The minimum amount payable at the time of purchase of a new card would be Rs 150/- including refundable security of Rs. 50/-.
                                     Subsequent recharge of the card can be done at Customer Care Centers of any station with a minimum value of Rs. 200/- and up to Rs. 3000/-.''')
                        print('\n')
                        print("(B) Tourist Card :")
                        print('\n')
                        print('''Suitable for unlimited travel over short duration on all DMRC lines except Airport Line.
                                  Two types of tourist cards are presently available :•	One-Day Card : available at a cost of Rs 200/- (Rs 150 + Rs 50 refundable security).•
                                  Three-Day Card: at a cost of Rs 500/- (Rs. 450 + Rs 50 refundable security)''')
                        print('\n')
                        print("(C) Tokens :")
                        print('\n')
                        print("• Commuters can purchase single journey tokens from Ticket counters of all Stations and from TVMs of selected stations.")
                        print("•  Journey is permitted for one way only.")
                        print("• Tokens are valid only for the day of its purchase.")
                        print("• Minimum Fare is Rs. 10/- and maximum is Rs. 60/- (fares are subject to revision from time to time), (Rs 80/- including Rapid Metro).")
                        print("• A passenger can refund an unused token within 60 minutes of its issue at the same station.")
                    if p ==1:
                         y5=0
                         stlist=[]
                         comm123="select * from stationdetails"
                         cur.execute(comm123)
                         rows=cur.fetchall()
                         for row in rows :
                             stlist.append(row[0])
                         print("the stations where you can  go are :")
                         for x in stlist :
                             print(x)
                         while y5 < 1:
                             y4=0
                             jk=input("please enter your destination")
                             for x in stlist:
                                 if x==jk:
                                    y4=1
                             if jk not in stlist:
                                     print('''either you have entered a  station which is not on red
                                             line or you have entered wrong spellings
                                             please enter the spellings correctly''')
                             if y4==1:
                                 c12="select price from stationdetails where stationname= %s"
                                 cur.execute(c12,(jk,))
                                 a3=cur.fetchall()
                                 a34=a3[0][0]
                                 print("the cost of one ticket for",jk,"from shadara is Rs",a34)
                                 print("\n")
                                 q=int(input("how many tickets do you want ?"))
                                 a333=q*a34
                                 print("your final payable amount is Rs",(q*a34))
                                 print("\n")
                                 deductbal=resultbal-a333
                                 print("your final balance is:",deductbal)
                                 print("please collect tokens from cash counter")
                                 c234="update metro set balance=%s where cellno =%s"
                                 cur.execute(c234,(deductbal,cellno))
                                 connection.commit()
                                 commuptrans=" insert into rechargedetails (cellno,name,balance_before,balance_after) values (%s,%s,%s,%s)"
                                 cur.execute(commuptrans,(cellno,resultname,resultbal,deductbal))
                                 connection.commit()
                                 stlist.clear()
                                 resultbal=deductbal
                                 y5=1
                    if p== 5:
                            print('\n')
                            print('''The Delhi Metro has been instrumental in ushering in a new era in the sphere of mass urban transportation in India.
                                  The swanky and modern Metro system introduced comfortable, air conditioned and
                                  eco-friendly services for the first time in India and completely revolutionized the mass transportation scenario
                                  not only in the National Capital Region but the entire country.''')
                            print('\n')
                            print('''Having constructed a massive network of about 389 Km with 285 stations (including NOIDA-Greater NOIDA Corridor and Rapid Metro, Gurugram)
                                   in record time in Delhi, NCR, the DMRC today stands out as a shining example of how a mammoth technically complex infrastructure project can
                                   be completed before time and within budgeted cost by a Government agency.
                                   Corporation Limited (DMRC) was registered on 3rd May 1995 under the Companies Act, 1956 with equal equity participation of the''')
                            print('\n')
                            print('''The Delhi Metro Rail Government of the National Capital Territory of Delhi (GNCTD) and the Central Government to implement
                                  the dream of construction and operation of a world- class Mass Rapid Transport System (MRTS).''')
                            print('\n')
                            print('''The DMRC opened its first corridor between Shahdara and Tis Hazari on 25th December, 2002.
                                  Subsequently, the first phase of construction worth 65 kilometres of Metro lines was finished two years and nine months ahead of schedule in 2005.
                                  Since then the DMRC has also completed the construction of another 125 kilometres of Metro corridors under
                                  the second phase in only four and a half years. ''')
                            print('\n')
                            print('''Presently, the Delhi Metro network consists of about 389 Km with 285 stations.
                                  The network has now crossed the boundaries of Delhi to reach NOIDA and Ghaziabad in Uttar Pradesh, Gurgaon, Faridabad,
                                  Bahadurgarh and Ballabhgarh in Haryana. With the opening of the Majlis Park to Shiv Vihar and Janakpuri West - Botanical Garden Sections,
                                  new age trains equipped with the Unattended Train Operation (UTO) technology have been introduced.
                                  These trains operate with the Communication Based Train Control(CBTC) signaling technology which facilitate movement of trains
                                  in very short frequencies. This network also includes the NOIDA - Greater NOIDA Aqua Line.
                                  The Aqua Line has been constructed by DMRC on behalf of the NOIDA Metro Rail Corporation and is also being operated by DMRC currently.
                                  In addition, the 11.6 kilometre long Rapid Metro also connects with the Delhi Metro network at Sikanderpur station of Yellow Line.
                                  The Rapid Metro provides connectivity within the satellite city of Gurugram.''')
                            print('\n')
                            print('''The Airport Express link between the Indira Gandhi International Airport and
                                  New Delhi has now propelled Delhi to the league of global cities which have high
                                  speed rail connectivity between the city and the airport.
                                  The DMRC today has over 300 train sets of four, six and eight coaches. ''')
                            print('\n')
                            print('''The Delhi Metro has also contributed tremendously on the environment
                                  front by becoming the first ever railway project in the world to claim carbon credits for regenerative braking.
                                  DMRC has also been certified by the United Nations (UN) as the first Metro Rail and Rail based system in the world
                                  to get carbon Credits for reducing Green House gas emissions as it has helped to reduce pollution levels in the city
                                  by 6.3 lakh tons every year thus helping in reducing global warming.''')
                            print('\n')
                            print('''It has also set up roof top solar power plants at many of its stations.
                                  All stations of the presently under construction corridors are being constructed as green buildings.
                                  In the present phase of Delhi Metro’s construction, the DMRC has completed 160 kilometres of Metro lines which has woven a web
                                  of Metro corridors along the city’s Ring Road besides connecting with many other localities in NOIDA, Ghaziabad, Bahadurgarh and Ballabhgarh.''')
                            print('\n')
                            print('''Apart from providing Delhites with a comfortable public transport option,
                                  the Delhi Metro is also contributing significantly towards controlling pollution as well as reducing vehicular congestion on the roads''')
                    if p==6:
                            print("                                                                  Contact Details :")
                            print('\n')
                            print("Metro Bhawan")
                            print("The address of office of the Claims Commisioner")    
                            print('\n')
                            print("Claims Commisioner, Delhi Fire Brigade Lane, Barakhamba Road,")
                            print("New Delhi - 110001, India")
                            print("Board No. - 23417910/12")
                            print("Fax No. - 23417921")
                            print('''Nearest Metro Station to reach Metro Bhawan is Barakhama Road Metro Station on blue line
                                  of the Dwarka-Noida city center/ Vaishali corridor (Line 3 and 4).''')
                            print('\n')                                
                            print("Metro Rail Corporation Limited,")
                            print("Room No.1, Block B, Ground Floor,")
                            print("Delhi Metro IT Park, East Approach Road,")
                            print("Shastri Park, Delhi-110053.")

                    if p==7:
                            print("If you deleted/deactivated this account, you have to make a new account in order to use the services of Delhi Metro")
                            print("All the balance in the account can be withdrawn from the Cashier after deactivation of account")
                            print('\n')
                            mn=1
                            while mn<2:
                                deactpas=input("Please enter your password again to confirm deactivation :")
                                print('\n')
                                if deactpas==resultpas :
                                    commdeact = " Delete from metro where Cellno = %s "
                                    cur.execute ( commdeact , ( cellno, ) )
                                    connection.commit ()
                                    print ( "Your account has been deactivated succesfully. ")
                                    r=1
                                    mn=3
                                else :
                                    print("You entered a wrong password.")
                                    ascc=eval(input( "Press 1 to Retry or Press  to go back to your Account's Home :"))
                                    print('\n')
                                    if ascc==1:
                                        mn=2
                    if p >7 :
                         d=8
            if pwd!=k :
                  print("please enter correct password")

                               
    
    if b==3 :
         nota=0
         while nota<1:
              uyo=input("Enter Admin ID :")
              if uyo=="10P21PI1679":
                  nota=1
                  print('\n')
                  print("1. Add a station")
                  print('\n')
                  print('2. Change rate of ticket to a station')
                  print('\n')
                  print('3. Remove a station')
                  print('\n')
                  print('4. View all the recharge history')
                  print('\n')
                  poker=eval(input("Enter Your Choice :"))
                  print('\n')
                  if poker==1:
                      hjl=input("Enter name of station :")
                      print('\n')
                      lhj=eval(input("Enter the cost of ticket from Pratap nagar :"))
                      print('\n')
                      coooc="Insert into stationdetails (stationname,price) values (%s,%s)"
                      cur.execute( coooc,(hjl,lhj))
                      connection.commit()
                  elif poker==2 :
                      comm2 = " select * from stationdetails "
                      cur.execute ( comm2 )
                      result1 = cur.fetchall ()
                      for row in result1 :
                       sttps.append(row[0])
                       while lmfaoo<1:
                              stn=input("Enter Name of the Station :")
                              print('\n')
                              for x in sttps:
                                  if x==stn:
                                      sos=1
                                  else:
                                      sos=sos+0
                              if sos==1:
                                  praicy=eval(input("Enter the new Price from Pratap Nagar:"))
                                  comm223 = " update stationdetails set price=%s where stationname=%s"
                                  cur.execute ( comm223, (praicy,stn,) )
                                  connection.commit()
                                  print("Succesfully Updated Information")
                                  sttps.clear()
                                  lmfaoo=1
                              else :
                                                        print("Please Enter the Name of Station Correctly. You have probably done some spelling mistake")
                                                        print('\n')



                  elif poker==4:
                       abc="select* from rechargedetails where cellno=%s"
                       ac="select name from rechargedetails where cellno=%s"
                       a=eval(input("Enter user's cell no:"))
                       cur.execute( abc, (a,))
                       result=cur.fetchall()
                       for x in result :
                           a=x
                           c=(a)
                           cellno,balancebefore ,name ,rechargeamount,balanceafter = c
                           print('''Recharge history:''')
                           print('name of user:',name)
                           print("balance before:",balancebefore,"rechargeamount:",rechargeamount,"balance after:",balanceafter)
                       
                  elif poker==3:
                       hjl=input("Enter name of station :")
                       print('\n')
                       coooc="delete from stationdetails where stationname=%s"
                       cur.execute( coooc,(hjl,))
                       connection.commit()
                       print("\t     station succesfully removed!")
                       


                      
              else:
                  print("Admin Code is incorrect ")
                  print('\n')
                  codtrb=eval(input("To retry press 1 or For Main Menu press any other key"))
                  if codtrb==1 :
                        nota=0
                  else :
                        nota=1



    if b==4:
         q=5
         print("terminating the program!!!!")
                        



lmfaoo=0
sos=0
                                  
                              
                            
                         
                            
                            

                                        
                            
                       
                
                 
            
                   
                   

               

               
