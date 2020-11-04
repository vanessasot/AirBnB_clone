![](Image.png)

# AirBnB clone - The console :computer:


### Contents :book:

### Description :pencil2:

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration

Each task is linked and will help you to:

	* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances

	* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

	* create all classes used for AirBnB (User, State, City, Place) that inherit from BaseModel

	* create the first abstracted storage engine of the project: File storage.

	* create all unittests to validate all our classes and storage engine

This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

When you run the./console.py console on a terminal, A prompt (hbnb) will apear on your screem, in where you can type your command and when you hit enter it will run the command and do that you ask for displaying the output on the stdout(Standar Output) then it will be waiting for you to enter another command, all of this in interacive mode. But also it have a non-interactive mode in where you just tell what command to execute

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T143847Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ecde9d9aec7e5c6f2ce8ac7bf17e5bcc46c896e951eef2ddd1a0902142b4d0e5)

### Environment :robot:
* Language: Python3
* OS: Ubuntu 14.04 LTS
* Style guidelines: [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/) \|| [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/l\atest/example_google.html)

### Example :bulb:

This **AirBnb clone** works like this:

On **non-interactive mode:**

![non-interactive mode](https://user-images.githubusercontent.com/55112483/74885416-7a6b7b80-5343-11ea-91c4-0a57799f71c1.png)



On **interactive mode:**

![interactive mode](https://user-images.githubusercontent.com/55112483/74885336-4beda080-5343-11ea-9fdf-98763ecbc0a1.png)

### Usage :memo:

---
| **Function** | **Funcionality** | 
| -------------- | ----------------- | 
|create | Creates an new object or instance of BaseModel. |
|show | Prints and show the string of an instance based on the class name and id. | 
|destroy | Deletes an instance based on the class name and id. | 
|all | Prints and show all string of all instances| 
|destroy | Deletes an instance based on the class name and id. | 
|quit | Exit the program. |
|EOF | Exit the program. | 
|help | Help function. |
|update | Updates an instance. |

### How to Install :computer: :triangular_flag_on_post:

Clone the repositoy below:
```bash
git clone https://github.com/didierrevelo/AirBnB_clone/tree/main
```

## Authors :black_nib:

* [**Didier Revelo**](https://github.com/didierrevelo) :construction_worker:
* [**Vanessa Sotomayor**](https://github.com/vanessasot) :princess:
* [**Jhonnyer Otalvaro**](https://github.com/Jhonierk) :trollface:
