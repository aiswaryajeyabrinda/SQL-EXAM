#!/usr/bin/env python
# coding: utf-8

# # 1

# In[ ]:


SELECT customer.cust_name AS "Customer",
customer.grade AS "Grade",orders.ord_no AS "Order No."
FROM orders, salesman, customer
WHERE orders.customer_id = customer.customer_id
AND orders.salesman_id = salesman.salesman_id
AND salesman.city IS NOT NULL
AND customer.grade IS NOT NULL;


# # 2

# In[ ]:


SELECT ord_no, purch_amt, ord_date, salesman_id 
FROM orders 
WHERE salesman_id IN( SELECT salesman_id FROM salesman WHERE commision = (SELECT MAX(commision) FROM salesman));


# # 3

# In[ ]:


SELECT ord_no, purch_amt, ord_date, salesman_id
FROM orders
WHERE salesman_id IN
    (SELECT salesman_id 
     FROM salesman 
     WHERE city='nagpur');


# # 4

# In[ ]:


SELECT ord_date, SUM(purch_amt), 
SUM(purch_amt)*.15 
FROM orders 
GROUP BY ord_date 
ORDER BY ord_date ASC;


# # 5

# In[ ]:


SELECT ord_no, purch_amt, ord_date, salesman_id
FROM orders
WHERE purch_amt >(SELECT  AVG(purch_amt) FROM orders );


# # 6

# In[ ]:


select * from orders ORDER BY purch_amt desc limit 4,1;


# # 7

# In[ ]:


Select Customer_id , ba.Account_Number,
Case when ifnull(Balance_amount,0) = 0 then   Transaction_amount else Balance_amount end  as Balance_amount
from bank_account_details ba  
inner join
bank_account_transaction bat
on ba.Account_Number = bat.Account_Number
and Account_type = "Credit Card";


# # 9

# In[ ]:


Select ba.Customer_id, ba.Account_Number, Balance_amount, Transaction_amount, Transaction_Date
from bank_account_details ba  
inner join
bank_account_transaction bat
on ba.Account_Number = bat.Account_Number
And ( Transaction_Date between "2020-03-01" and "2020-04-30");


# # 10

# In[ ]:


Select ba.Customer_id, ba.Account_Number, Balance_amount, Transaction_amount, Transaction_Date
from bank_account_details ba   
Left join bank_account_transaction bat
on ba.Account_Number = bat.Account_Number
And NOT (Transaction_Date between "2020-03-01" and "2020-03-31")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




