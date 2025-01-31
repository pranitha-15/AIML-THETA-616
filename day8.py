import pandas as pd
data = pd.DataFrame({'Brand':['BMW','BENZ','RANGE ROVER','ROYCE','BUGGATI','RANGE ROVER','BMW','TATA','KIA'],'Year':[2012,2014,2011,2015,2012,2016,2014,2018,2019],'Kms_driven':[50000,30000,60000,25000,10000,46000,31000,15000,12000],'City':['Hyderabad','Delhi','Mumbai','Delhi','Mumbai','Delhi','Mumbai','Hyderabad','Bengalore'],'Mileage':[28,27,29,45,46,38,29,41,48]})
print(data)#display(data)

"**************************************************"

import pandas as pd
sales_data = {
    'TransactionID' : [1, 2, 3, 4, 5],
    'CustomerID' : [101, 102, 103, 104, 105],
    'Amount':[250, 300, 400, 500, 600],
    'Date' : ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05']
}
customer_data = {
    'CustomerID' : [101, 102, 103, 104],
    'CustomerName' : ['John', 'Alice', 'Bob', 'Eve'],
    'Age' : [20,45, 30, 24],
    'City' : ['New York', 'Paris', 'London', 'Sydney']
}
sales_df = pd.DataFrame(sales_data)
customer_df = pd.DataFrame(customer_data)
print("Sales Data: ")
print(sales_df)
print("\nCustomer Data: ")
print(customer_df)