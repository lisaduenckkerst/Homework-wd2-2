# 1–What order (Invoice) was the most expensive? Which one was the cheapest?
# 2–Which city (BillingCity) has the most orders?
# 3–Calculate (or count) how many tracks have this MediaType: Protected AAC audio file.
# 4–Find out what Artist has the most albums? (hint: check ORDER BY)
# 5–What genre has the most tracks?
# 6–Which customer spent the most money so far?
# 7–What songs were bought with each order? (hint: here you have to do a many-to-many SQL query with three tables: Track, Invoice and InvoiceLine. You have to do two JOINS here)

from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")  # Relative Referenzierung || Pfadangabe = Absolute Referenzierung

# TASK 1 most expensive + cheapest invoice
db.pretty_print("SELECT MAX (Invoice.Total) FROM Invoice;")
db.pretty_print("SELECT MIN (Invoice.Total) FROM Invoice;")

# TASK 2 billing city w/ most orders
db.pretty_print("SELECT MAX (Invoice.BillingCity) FROM Invoice;")

# TASK 3 count tracks w/ mediatype protected aac audio file
db.pretty_print("SELECT COUNT (Track.MediaTypeID) FROM Track INNER JOIN MediaType ON MediaType.MediaTypeId WHERE "
				"MediaType.Name='Protected AAC audio file';")

# TASK 4 artist w/ most albums
db.pretty_print("SELECT Artist.Name, COUNT(*) AS Album_Numbers FROM Artist INNER JOIN Album ON "
				"Album.ArtistId=Artist.ArtistId GROUP BY Artist.ArtistId ORDER BY Album_Numbers DESC;")

# TASK 5 genre w/ most tracks
db.pretty_print("SELECT Genre.Name, COUNT(Track.GenreId) AS Genre_Numbers FROM Genre INNER JOIN Track ON "
				"Genre.GenreId=Track.GenreId GROUP BY Track.GenreId ORDER BY Genre_Numbers DESC;")

# TASK 6 customer who spent the most money
db.pretty_print("SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS Invoice_Sum FROM Invoice INNER JOIN "
				"Customer ON Invoice.CustomerId=Customer.CustomerId GROUP BY Customer.CustomerId ORDER BY Invoice_Sum "
				"DESC;")

# TASK 7 what songs were bought with each order?
db.pretty_print("SELECT Invoice.InvoiceId, Track.Name FROM Invoice JOIN InvoiceLine ON "
				"InvoiceLine.InvoiceLineId=Invoice.InvoiceId JOIN Track ON Track.TrackId=InvoiceLine.TrackId;")
