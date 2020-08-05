# Download this database: Chinook.sqlite
from smartninja_sql.sqlite import SQLiteDatabase


chinook = SQLiteDatabase("Chinook_Sqlite.sqlite")


chinook.pretty_print("""
                        SELECT * FROM Artist
                        limit 10 ;
                        """)

chinook.pretty_print("""
                        SELECT * FROM Customer
                        limit 10 ;
                        """)

chinook.pretty_print("""
                    SELECT Customer.FirstName, SUM(Invoice.Total)
                    FROM Invoice INNER JOIN Customer
                    ON Invoice.CustomerID = Customer.CustomerID
                    GROUP BY Invoice.CustomerID
                    limit 10;
                    """)

chinook.pretty_print("""
                    SELECT Invoice.CustomerId, Invoice.BillingCity, Customer.FirstName, Customer.LastName, Invoice.Total
                    FROM Invoice
                    INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
                    WHERE Invoice.BillingCity='Stockholm';
                    """)

chinook.pretty_print("""
                    SELECT SUM(Invoice.Total)
                    FROM Invoice
                    INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
                    GROUP BY Invoice.CustomerId;
                    """)

chinook.pretty_print("""
                    SELECT Professor.First_name, Professor.Last_name,Course.Title
                    FROM Professor
                    FULL JOIN Course
                    ON Professor.ID = Course.ProfessorID
                    """)



