# Personsearch

In compliance with the UK financial standards, we need to develop a OFAC list search tool, that looking for a match in our huge person database (25M).

So, because we don't have the server resources to do a search like this, we move to AWS, to schedule a monthly load, search and report.

This example shows partially the development that we did.

### Server

Amazon Web Services - Elastic Beanstalk 

### Tech

Personsearch uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps
* [Angular Material] - great UI that use Google Guidelines
* [Angular Resources]- great API call manager
* [python2] - evented I/O for the backend
* [Django] - fast high level Python Web framework
* [Django RestFramework] - Django plugin for REST API with web console
* [Django RestFramework Filters] - Django plugin for Search API

### Example

You can test the app in

#### Amazon

* [Amazon Web Service People Search](http://django-peoplesearch.szymaphwz3.us-west-2.elasticbeanstalk.com)
* [Amazon Web Service People API](http://django-peoplesearch.szymaphwz3.us-west-2.elasticbeanstalk.com/api/people/)
* [Amazon Web Service People Upload API](http://django-peoplesearch.szymaphwz3.us-west-2.elasticbeanstalk.com/api/people/upload/)
* [Amazon Web Service People All API](http://django-peoplesearch.szymaphwz3.us-west-2.elasticbeanstalk.com/api/people/all/)

#### Heroku

* [Heroku People Search](https://django-peoplesearch.herokuapp.com)
* [Heroku People API](https://django-peoplesearch.herokuapp.com/api/people/)
* [Heroku People People Upload API](https://django-peoplesearch.herokuapp.com/api/people/upload/)
* [Heroku People People All API](https://django-peoplesearch.herokuapp.com/api/people/all/)


For upload you can generate a random database with this [awesome app](https://www.mockaroo.com/c54629c0) and paste the contents in the web UI People Upload REST API.


### Installation

Once you configure your [AWS account, credentials](https://aws.amazon.com/) and you have setup your [python environment](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-common-steps.html#python-common-prereq) you can setup your virtual environment.

```sh
virtualenv ps-virt
source ps-virt/bin/activate
pip install django
pip install djangorestframework
pip install django-filter
mkdir peoplesearch
cd peoplesearch
git clone https://github.com/DKbyo/peoplesearch.git
python manage.py collectstatic
```

### Test

For local test, you can start the local server.

```sh
python manage.py runserver
```

### Deploy

For deploy the app on your own AWS environment.

```sh
eb init -p python2.7 peoplesearch
eb create ps_env
```

Once AWS has deployed the app you can test 

```sh
eb open
```

And you can update your changes

```sh
python manage.py collectstatic
eb deploy
```
