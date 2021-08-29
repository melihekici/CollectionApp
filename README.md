# Install Requirements  
`pip install django`    
`pip install djangorestframework`    
`pip install django-cors-headers`    
`sudo apt install sqlite3`   
  
# Run Server  
`python manage.py runserver`   

# Models
![Alt text](./erd.png?raw=true "Entity Relationship Diagram")
## Bin Model  
Bin model has three fields.  
 
id: Primary Key 
latitude: FloatField  
longitude: FloatField  

### End Points

GET "/bins"
* Returns the list of bins.  
  
POST "/bins"  
body: {latitude: float, longitude: float}  
* Adds a bin record to the database.  

PUT "/bins"  
body: {"id": bin id, "latitude": float, "longitude": float}  
* Update an existing bin.  

DELETE "/bin/{id}"  
* Removes the bin record from database.  
* When bin is removed, associated collection records will be removed as well.  


## Operation Model  
Operation model has two fields.  

id: Primary Key  
name: CharField   
  
### End Points  
  
GET "/operations"  
* Returns the list of operation records.  
  
POST "/operations"  
body: {"name": str}    
* Adds an operation record to the database.  

PUT "/operations"  
body: {"id": operation id, "name": str}  
* Update an operation record.  
  
DELETE "/operations/{id}"  
* Removes the operation record from database.  

## Collection Model
Collection model has five fields.  

id: Primary Key   
bin: Foreign Key  
operation: Foreign Key  
collection_frequency: IntegerField  
last_collection: DateTimeField  
  
### End Points  
  
GET "/collections"  
* Returns the list of list of collection_frequency and last_collection values for all Bin-Operation pairs. 
  
POST "/collections"  
body: {"bin": bin id, "operation": operation id, "collection_frequency": Integer, "last_collection": Datetime("2021-08-30 13:51:25")}    
* Adds a collection record to the database.  
  
PUT "/collections"  
body: {"id": collection id, "bin": bin id, "operation": operation id, "collection_frequency": Integer, "last_collection": Datetime("2021-09-30 14:26:33")}  
* Update a collection record.  
   
DELETE "/collections/{id}"  
* Removes the collection record from database. 

