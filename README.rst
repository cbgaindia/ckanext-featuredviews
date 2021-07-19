=============
ckanext-featuredviews
=============

Display select resource views on dataset and home pages.

By default, CKAN only shows Resource Views on the resource page, but has no
mechanism for showing users which resources have visualizations, and where the
good ones are.

This extension lets you mark Resource Views as featured so they show up right
on your dataset pages or even on the CKAN front page.

Usage
=============
**For Ckan < 2.9 checkout master branch** ::

    git clone https://github.com/cbgaindia/ckanext-d3view.git
    python setup.py develop
   
Add to the list of plugins: ::

    ckan.plugins = ... featuredviews
    
Run the migrations: ::

    paster --plugin=ckanext-featuredviews featured migrate
    
**For Ckan 2.9 checkout dev branch** ::

    git clone https://github.com/cbgaindia/ckanext-d3view.git
    git checkout dev
    python setup.py develop
   
Add to the list of plugins: ::

    ckan.plugins = ... featuredviews
    
Run the migrations: ::

    ckan -c /etc/ckan/default/ckan.ini featured initdb
