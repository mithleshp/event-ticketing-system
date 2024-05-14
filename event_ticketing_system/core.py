import mysql.connector,csv

class evntDatabase():
     
    def __init__(self):
       connection = None
       
    def get_db_connection(self):   
        try:
            self.connection = mysql.connector.connect(user="root",
            password="dev123",
            host='localhost',
            port='3306',
            database='event_db')
        except Exception as error:
            print("Error while connecting to database for job tracker", error)
        return self.connection

    def load_third_party(self, file_path_csv):
        print(self.connection)
        cursor = self.connection.cursor()
        with open(file_path_csv) as file_obj: 
            reader_obj = csv.reader(file_obj) 
            for row in reader_obj: 
                print(row)
                 
                sql_statement = "insert into event_db.sales(ticket_id,trans_date,event_id,event_name,event_date,event_type,event_city,customer_id,price,num_tickets) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql_statement,row)
        self.connection.commit()
        cursor.close()
        return
    
    def query_popular_tickets(self):
        # Get the top 3 most popular tickets ..Not doing for past month since no data
        sql_statement = "select event_name from event_db.sales order by num_tickets desc limit 3"
        cursor = self.connection.cursor()
        cursor.execute(sql_statement)
        records = cursor.fetchall()
        cursor.close()
        return records

def main():
    event_db = evntDatabase()
    conn = event_db.get_db_connection()
    #event_db.load_third_party("resources\third_party_sales_1.csv")
    top_three_popular_evnt = event_db.query_popular_tickets()
    print(f"Here are the most popular tickets in the past month:")
    for event in top_three_popular_evnt:
        print(f"- ",event[0])

if __name__ == '__main__':
    main()





