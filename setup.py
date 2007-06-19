from setuptools import setup, find_packages

name = "plone.recipe.zope2instance"
version = '0.4'

setup(
    name = name,
    version = version,
    author = "Hanno Schlichting",
    author_email = "plone@hannosch.info",
    description = "ZC Buildout recipe for installing a Zope 2 instance",
          long_description="""\
This recipe creates and configures a Zope 2 instance in parts. It also
installs a control script, which is like zopectl, in the bin/ directory.
The name of the control script is the the name of the part in buildout.

You can use it with a part like this::

  [instance]
  recipe = plone.recipe.zope2instance
  zope2-location = /path/to/zope2/install
  user = admin:admin
  http-server = 8080
  eggs = ${buildout:eggs} my.package
  products = ${buildout:directory}/products
  zcml = my.package

The available options are:

 zope2-location -- The path where Zope 2 is installed. If you are also
  using the plone.recipe.zope2install recipe, and you have that configured
  as a part called 'zope2' prior to the zope2instance part, you can use
  ${zope2:location} for this parameter.
  
 zope-conf -- A relative or absolute path to a zope.conf file. If this is
  not given, a zope.conf will be generated based on the the options below.
  
The following options all affect the generated zope.conf.
  
 products -- A list of paths where Zope 2 products are installed. The first
  path takes precedence in case the same product is found in more than one
  directory.
  
 zcml -- Install ZCML slugs for the packages listed, separated by whitespace.
  
 debug-mode -- Set to 'on' to turn on debug mode in Zope. Defaults to 'off'.
 
 verbose-security -- Set to 'on' to turn on verbose security (and switch to
  the Python security implementation). Defaults to 'off' (and the C security
  implementation).
  
 http-address -- Give a port for the HTTP server. Defaults to 8080.
  
 event-log -- The filename of the event log. Defaults to 
  var/log/${partname}.log
 
 z2-log -- The filename for the Z2 access log. Defaults to 
  var/log/${partname}-Z2.log.
  
 file-storage -- The filename where the ZODB data file will be stored. 
  Defaults to var/filestorage/Data.fs.
  
 zeo-client -- Set to 'on' to make this instance a ZEO client. In this case,
  setting the zeo-address option is required, and the file-storage option has
  no effect. To set up a ZEO server, you can use the 
  plone.recipe.zope2zeoserver recipe. Defaults to 'off'.
 
 zeo-address -- Set the address of the ZEO server. Defaults to 8100.
 
 zodb-cache-size -- Set the ZODB cache size, i.e. the number of objects which
  the ZODB cache will try to hold. This is currently only set for ZEO 
  storages. Defaults to 2000.
 
 zeo-client-cache-size -- Set the size of the ZEO client cache. Defaults to
  '30MB'.
  
 zope-conf-additional -- Give additional lines to zope.conf. Make sure you
  indent any lines aftter the one with the parameter. 


""",
    license = "ZPL 2.1",
    keywords = "zope2 buildout",
    url='http://svn.plone.org/svn/collective/buildout/'+name,
    classifiers=[
      "License :: OSI Approved :: Zope Public License",
      "Framework :: Buildout",
      "Framework :: Plone",
      "Framework :: Zope2",
      "Programming Language :: Python",
      ],
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    namespace_packages = ['plone', 'plone.recipe'],
    install_requires = ['zc.buildout', 'setuptools', 'zc.recipe.egg'],
    dependency_links = ['http://download.zope.org/distribution/'],
    zip_safe=False,
    entry_points = {'zc.buildout': ['default = %s:Recipe' % name]},
    )