# CalenderManagementApi in djangoframework
This project contains api's for user registration,user authentication and calendermanagement.

Instructions Of using Link

1.when you put http://127.0.0.1:8000/registration/ using local host you will see post method along with all registered

User Only When You Are Authenticated into djangoadmin.

2.In order to do registration you have to put text in box above post method in json format like this

Ex:- {
        "Name": "xyz",
        
        "Email": "xyz@gmail.com",
         
         "Date":"02/12/20",
        
        "Title": "Event meeting",
        
        "Description": "I have to take all of my important file for that."
        }
3. when you want to see your details of events then you just need to add your email id like this http://127.0.0.1:8000/registration/email//.

4. when you want to edit or delete event than you can add your id of that event into link like this http://127.0.0.1:8000/id/.

5. for edit just write like this above put box

Ex:-{    
        "id":"2",
        
        "Name": "xyz",
        
        "Email": "xyz@gmail.com",
         
         "Date":"02/12/20",
        
        "Title": "Event meeting",
        
        "Description": "I have to take all of my important file for that."
        }

6.For delete just click on delete button.
