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

          OR
* You can download python from https://www.python.org/downloads/ and install



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
5. Install Mongodb in local machine OR You can create the database in the MongoCloud for free, click [here][mongo-cloud] to get free account
    `Note: If you have installed MongoDB locally you can follow 6th step otherwise ignore`
6. Setup password for mongo
    * Go to mongo console by using `mongo`
    * Execute below queries
    ```sh
    use library
    db.createUser(
        {
            user: "username",
            pwd: "password",
            roles: [ { role: "readWrite", db: "library" } ]
        }
    )
    ```
    * Enable authentication in `/etc/mongodb.conf`
    * Restart mongodb service
    * To connect to mongodb from console, `use mongo library -u admin -p` and then enter password when prompted
7. Configure database.yml by following steps
    * rename `main/database.yml_sample` to `main/database.yml`
    * update DB_NAME, MONGO_USER, MONGO_PASS, HOST (You should have aquired this information from 5th or 6th step)
8. `export FLASK_ENV=development` in Linux and use set in windows
9. execute `flask run` to run the application
10. Start the application
```sh
python app.py 
or
flask run
```

```sh
# To see the no. of connections opened in MongoDB useful command
db.serverStatus().connections
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
[mongo-cloud]: https://www.mongodb.com/cloud/atlas/lp/try2-in?utm_source=google&utm_campaign=gs_apac_india_search_brand_atlas_desktop&utm_term=mongo%20db%20cloud&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=6501677905&gclid=EAIaIQobChMImuqyp9v_7QIVljArCh0yBA62EAAYASAAEgJ5ZvD_BwE
[product-screenshot]: apidocs.png
