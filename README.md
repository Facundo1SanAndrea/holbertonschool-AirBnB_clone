## # AirBnB clone - The console
## Project Overview
Description of the project

The goal of the project is to deploy on a server a simple copy of the AirBnB website.

What you should learn from this project:

-   How to create a Python package
-   How to create a command interpreter in Python using the cmd module
-   What is Unit testing and how to implement it in a large project
-   How to serialize and deserialize a Class
-   How to write and read a JSON file
-   How to manage datetime
-   What is an UUID
-   What is *args and how to use it
-   What is **kwargs and how to use it
-   How to handle named arguments in a function
----
This Project Included the Following Tasks:
1. Be PEP8 compliant!
-   Write beautiful code that passes the PEP8 checks.
### [2. Unittests](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/tree/main/tests)
-   All your files, classes, functions must be tested with unit tests
### [3. BaseModel](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/models/base_model.py)

-   Write a class BaseModel that defines all common attributes/methods for other classes:
### [4. Create BaseModel from dictionary](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py)

-   Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

### [5. Store first object](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/console.py)

-   Now we can recreate a BaseModel from another one by using a dictionary representation:
### [6. Console 0.0.1](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/console.py)

-   Write a program called console.py that contains the entry point of the command interpreter:

### [7. Console 0.1](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/models/user.py)

-   Update your command interpreter console to have these commands
### [8. First User](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/models/state.py)

-   Write a class User that inherits from BaseModel:

### [9. More classes!](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/console.py)

-   Write all those classes that inherit from BaseModel:

### [10. Console 1.0](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/console.py)

-   Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

### [11. All instances by class name](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/console.py)

-   Update your command interpreter (console.py) to retrieve all instances of a class by using: .all().

### [12. Count instances](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/console.py)

-   Update your command interpreter (console.py) to retrieve the number of instances of a class: .count().

### [13. Show](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/console.py)

-   Update your command interpreter (console.py) to retrieve an instance based on its ID: .show().
### [14. Destroy](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/console.py)

-   Update your command interpreter (console.py) to destroy an instance based on his ID: .destroy().
### [15. Update](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/console.py)

-   Update your command interpreter (console.py) to update an instance based on his ID: .update(, , ).

### [16. Update from dictionary](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/console.py)

-   Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: .update(, ).
- ---
**Getting Started**
In this early stage of the package we made a console with custom commands to manipulate different objects and save them in json format.
																	
									**Clone the repository**
																	
		`git clone https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone`



-   Description of the command interpreter:

The command interpreter manipulates data without a visual interface, which eases developmentand debugging.

-   How to use it

The command interpreter can be used to create, manipulate, serialize/deserialize and destroy class objects (i.e. BaseModel, User, State, Amenity, City, Place, and Review - which allow for the management and maintenance of the objects that comprise the HBnB Database.
### ow to start console (launches the prompt)

```
./console.py

```

### [](https://github.com/tyedge/AirBnB_clone#how-to-create-a-user-object-prints-the-id-of-the-new-object)How to create a User Object (prints the id of the new object)

```
(hbnb) create User

```

### [](https://github.com/tyedge/AirBnB_clone#how-to-display-a-specific-object-displays-a-string-represntation-of)How to display a specific object (displays a string represntation of\

the object)

```
(hbnb) show User [object id]

```

### [](https://github.com/tyedge/AirBnB_clone#how-to-display-all-objects-or-all-object-of-a-specific-class-displays-list)How to display all objects or all object of a specific class (displays list)

```
(hbnb) all

```

or

```
(hbnb) all User

```

### [](https://github.com/tyedge/AirBnB_clone#how-to-destroy-a-user-object-deletes-object)How to destroy a User object (deletes object)

```
(hbnb) destroy User [object id]
```

##  Architecture

![Fredrik Norm??n - Using Web Services in a 3-tier architecture](https://aspblogs.blob.core.windows.net/media/fredriknormen/WindowsLiveWriter/UsingWebServicesina3tierarchitecture_134F6/3tier_2.jpg)
**Presentation Layer** - [console.py](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/console.py)
**Bussines Logic Layer** [models](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/tree/main/models)
**Data Acces Layer** [storage](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py)
--
in non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## Example
![examples](https://github.com/SchneiderSix/holbertonschool-AirBnB_clone/raw/main/images/cmdexamples.png)
--
**AUTHORS**

[Facundo San Andrea](https://github.com/Facundo1SanAndrea/holbertonschool-AirBnB_clone/blob/main/AUTHORS "AUTHORS") - [GITHUB](https://github.com/Facundo1SanAndrea?tab=repositories)
