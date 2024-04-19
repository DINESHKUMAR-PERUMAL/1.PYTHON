class multiplefunctions():
    def Subfields():
            print("Sub-fields in AI are:")
            list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
            for i in list:
                print(i)
    def OddEven():
            num=int(input("Enter a number:"))
            if num%2==0:
                print(num,"is Even number")
                message="Even number"
            else:
                print(num,"is odd number")
                message="odd number"
                return message 
    def Elegible():
            gender=input("Your Gender:")
            age=int(input("Your Age:"))
            if(age>=21):
                 print("ELEGIBLE") 
                 cate="ELEGIBLE"
            else:
                print("NOT ELEGIBLE")
                cate="NOT ELEGIBLE"
                return cate
    def percentage():
            m1=int(input("subject1="))
            m2=int(input("subject2="))      
            m3=int(input("subject3="))
            m4=int(input("subject4="))
            m5=int(input("subject5="))
            Total=(m1+m2+m3+m4+m5)
            print("Total:",Total)
            message="Total"
            percentage=(Total/5)
            print("Percentage:",percentage)
            message="percentage"
            return message
    def triangle():
            Height=int(input("Height:"))
            Breadth=int(input("Breadth:"))
            print("Area formula:(Height*Breadth)/2")
            area=((Height*Breadth)/2)
            print("Area of triangle:",area)
            Height1=int(input("Height1:"))
            Height2=int(input("Height2:"))
            Breadth=int(input("Breadth:"))
            print("Perimeter formula:Height1+Height2+Breadth")
            Perimeter=(Height1+Height2+Breadth)
            print("Perimeter Triangle:",Perimeter)
        
    
                        
                
         
            
