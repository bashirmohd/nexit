import mysql.connector

def DataUpdate(First_name=" ",DateOfBirth=" ", PhoneNumber=" ", Email=" ",Gender=" ", MaritalStatus=" ", state_origin=" ", lga_origin=" ", state_residence=" ",
               lga_residence=" ", existing_bussiness=" ", sector=" ", participate=" ",job_after_exit=" ",
               job_type=" ", acquire_skill=" ", skill_type=" ",any_business=" ", business_venture=" ", need_loan=" "):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="rootroot",
      database="UserDetails"
    )

    mycursor = mydb.cursor()
    sql = "CREATE TABLE User_full_details (FirstName VARCHAR(255),DateOfBirth VARCHAR(255),PhoneNumber VARCHAR(255),Email VARCHAR(255),Gender VARCHAR(25),MaritalStatus VARCHAR(25), " \
          "state_origin VARCHAR(255),lga_origin VARCHAR(255),state_residence VARCHAR(255),lga_residence VARCHAR(255)," \
          "existing_bussiness VARCHAR(25),sector VARCHAR(255),participate VARCHAR(25),job_after_exit VARCHAR(25)," \
          "job_type VARCHAR(255),acquire_skill VARCHAR(25),skill_type VARCHAR(255),any_business VARCHAR(25)," \
          "business_venture VARCHAR(25),need_loan VARCHAR(25));"
    sql='INSERT INTO User_full_details (FirstName,DateOfBirth,Gender, MaritalStatus, state_origin, lga_origin, state_residence,lga_residence, existing_bussiness, sector, participate,job_after_exit, job_type, acquire_skill, skill_type,any_business, business_venture, need_loan) VALUES ("{0}","{1}", "{2}","{3}","{4}","{5}","{6}", "{7}","{8}","{9}","{10}","{11}", "{12}","{13}","{14}","{15}","{16}","{17}");'.format(First_name,DateOfBirth,Gender, MaritalStatus, state_origin, lga_origin, state_residence,lga_residence, existing_bussiness, sector, participate,job_after_exit,job_type, acquire_skill, skill_type,any_business, business_venture, need_loan)

    # sql="select {0} from FeedBack_rasa_date where Fees{1}{2};".format()
    mycursor.execute(sql)
    mydb.commit()
    # mydb.commit()
    # mydata=mycursor.fetchall()
    # print(mydata)
    # print(mycursor.rowcount, "record inserted.")
    # for i,j in mydata:
    #     print('''\
    #     First Name: {}
    #     Last Name: {}
    #     '''.format(i,j))

def DataExtract(column,more_less,fees):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="root",
      database="Rasa_feedback"
    )

    mycursor = mydb.cursor()

    # sql = "CREATE TABLE FeedBack_rasa_date (firstName VARCHAR(255),lastName VARCHAR(255),Date VARCHAR(255), Fees INT(10),feedback VARCHAR(255));"
    # sql='INSERT INTO FeedBack_rasa_date (firstName, lastName,Date,Fees, feedback) VALUES ("{0}","{1}", "{2}","{3}","{4}");'.format(FirstName,LastName,date,fee,Feedback)

    sql="select {0} from FeedBack_rasa_date where Fees{1}{2};".format(column,more_less,fees)
    mycursor.execute(sql)
    # mydb.commit()
    mydata=mycursor.fetchall()


    output=[i[0] for i in mydata]
    # mydb.commit()
    # mydata=mycursor.fetchall()
    # print(mydata)
    # print(mycursor.rowcount, "record inserted.")
    # for i,j in mydata:
    #     print('''\
    #     First Name: {}
    #     Last Name: {}
    #     '''.format(i,j))
    return output
#if __name__=="__main__":
    # print(DataExtract('firstName',">=","3000"))
    # DataUpdate("15-05-1995","Male","Unmarried","up","lko","hp","una","yes","I.C.T.","yes","yes","self-employed","yes","python","yes","yes","yes")
    #DataUpdate()
