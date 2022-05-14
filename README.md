# ibuQa Test
## Description
A simple service that uses a REST API to register customers and their orders and sends an alert SMS to the customer confirming the order.

## Link to live site
* Copy and paste it in new window
[](link)

## Setup and Installation

To get the project;

##### Cloning the repository:

```bash
https://github.com/OwinoLucas/ibuQa_test.git
```

##### Navigate into the folder and install requirements

```bash
cd ibuQa_test pip install -r requirements.txt
```

##### Install and activate Virtual

```bash
- python3 -m virtualenv venv - source venv/bin/activate
```

##### Setup Database

SetUp your database User,Password, Host then make migrate

```bash
python manage.py makemigrations 
```

Now Migrate

```bash
python manage.py migrate
```

##### Run the application

```bash
python manage.py runserver
```

##### Testing the application

```bash
python manage.py test
```

Open the application on your browser `127.0.0.1:8000`.

## License
Copyright (c) [2020] [Lucas Otieno]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.