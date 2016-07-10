# Personsearch

In compliance with the UK financial standards, we need to develop a OFAC list search tool, that looking for a match in our huge person database (25M).

So, because we don't have the server resources to do a search like this, we move to AWS, to schedule a monthly load, search and report.

This example shows partially the development that we did.

### Server

Amazon Web Services - Elastic Beanstalk 

### Tech

Personsearch uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps!
* [Angular Material] - great UI that use de Google Guidelines
* [python2] - evented I/O for the backend
* [Django] - fast high level Python Web framework


### Installation

Once you configure your [AWS account, credentials](https://aws.amazon.com/) and you have setup your [python environment](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-common-steps.html#python-common-prereq) you can setup your virtual environment.

```sh
virtualenv ps-virt
source ps-virt/bin/activate
pip install django
mkdir personsearch
cd personsearch
git clone https://github.com/DKbyo/personsearch.git
```

### Test

For local test, you can start the local server.

```sh
python manage.py runserver
```

### Deploy

For deploy the app on your own AWS environment.

```sh
eb init -p python2.7 personsearch
eb create ps_env
```

Once AWS has deployed the app you can test 

```sh
eb open
```

And you can update your changes

```sh
eb update
```
