"""`appengine_config` gets loaded when starting a new application instance."""
import vendor
# insert `lib` as a site directory so our `main` module can load
# third-party libraries, and override built-ins with newer
# versions.
vendor.add('lib')

appstats_CALC_RPC_COSTS = True
appstats_SHELL_OK = True

def webapp_add_wsgi_middleware(app):
  from google.appengine.ext.appstats import recording
  app = recording.appstats_wsgi_middleware(app)
  return app
