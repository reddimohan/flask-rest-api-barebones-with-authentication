[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/reddimohan/flask-rest-api-barebones-with-authentication">
  </a>

  <h3 align="center">Flask + Mongodb + REST API + JWT Authentication</h3>

  <p align="center">
    Boilerplate code for quick implimentation of REST API with JWT Authentication.
    <br />
    <br />
    <a href="https://github.com/reddimohan/flask-rest-api-barebones-with-authentication/issues">Report Bug</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

[![https://reddimohan.github.io][product-screenshot]]()

### Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x)
* [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable)
* [MongoDB](https://www.mongodb.com)
* [jwt](https://jwt.io)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python - I am using Anaconda distribution for easy installation of Python and pip
* Click [here](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-18-04) to Install Anaconda



### Installation

1. Clone the repo
```sh
git clone https://github.com/reddimohan/flask-rest-api-barebones-with-authentication.git
```
2. Create python environment so that we dont disturb other project versions
```sh
conda create --name rest_37 python=3.7
```
3. Activate the `rest_37` environment
```sh
conda activate rest_37
```
4. Install required python libs
```sh
pip install -r requirements.txt
```
5. Install Mongodb
6. Setup password for mongo
    * Go to mongo console by using `mongo`
    * Execure below queries
    ```sh
    use emr
    db.createUser(
        {
            user: "username",
            pwd: "password",
            roles: [ { role: "readWrite", db: "emr" } ]
        }
    )
    ```
    * Enable authentication in `/etc/mongodb.conf`
    * Restart mongodb service
    * To connect to mongodb from console, `use mongo emr -u admin -p` and then enter password when prompted
5. `export FLASK_ENV=development` in Linux and use set in windows
6. execute `flask run` to run the application
7. Start the application
```sh
python app.py 
or
flask run
```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/reddimohan/flask-rest-api-barebones-with-authentication/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Mohan - [LinkedIn](https://linkedin.com/in/reddimohan) - [Twitter](https://twitter.com/reddimohan)

Project Link: [https://github.com/reddimohan/flask-rest-api-barebones-with-authentication](https://github.com/reddimohan/flask-rest-api-barebones-with-authentication)







<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/reddimohan/flask-rest-api-barebones-with-authentication.svg?style=flat-square
[contributors-url]: https://github.com/reddimohan/flask-rest-api-barebones-with-authentication/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/reddimohan/flask-rest-api-barebones-with-authentication.svg?style=flat-square
[forks-url]: https://github.com/reddimohan/flask-rest-api-barebones-with-authentication/network/members
[stars-shield]: https://img.shields.io/github/stars/reddimohan/flask-rest-api-barebones-with-authentication.svg?style=flat-square
[stars-url]: https://github.com/reddimohan/flask-rest-api-barebones-with-authentication/stargazers
[issues-shield]: https://img.shields.io/github/issues/reddimohan/flask-rest-api-barebones-with-authentication.svg?style=flat-square
[issues-url]: https://github.com/reddimohan/flask-rest-api-barebones-with-authentication/issues
[license-shield]: https://img.shields.io/github/license/reddimohan/flask-rest-api-barebones-with-authentication.svg?style=flat-square
[license-url]: https://github.com/reddimohan/flask-rest-api-barebones-with-authentication/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/reddimohan
[product-screenshot]: apidocs.png








#### Flask + Mongodb + REST API + Authentication

##### Screenshot

![API docs Screenshot](apidocs.png)

```sh
$ python -V
Python 3.7.4
```

##### Setup
- Git clone <project_url>
<!-- - Install `sudo apt-get install libmysqlclient-dev` since `flask-mysqldb` package will be expecting mysql_config -->
- install requirements `pip install -r requirements.txt`
- `export FLASK_ENV=development` in Linux and use `set` in windows
- execute `flask run` to run the application


##### Features
1. User registration & Login
2. Token (JWT) based API calls
3. User delete
4. Get user profile
5. Delete user


```sh
# To see the no. of connections opened in MongoDB
db.serverStatus().connections
```