/* This is a bundle that uses RequireJS to pull in dependencies.
   These dependencies are defined in the registry.xml file */


/* do not include jquery multiple times */
if(window.jQuery){
  define('jquery', [], function(){
    return window.jQuery;
  });
}

require([
  'jquery',
  'example-dependency1',
  'example-dependency2',
  'pat-logger'
], function($, dep1, dep2, logger){
  'use strict';
  var log = logger.getLogger('example');
  log.warn('loaded dependency 1 value: ' + dep1);
  log.warn('loaded dependency 2 value: ' + dep2);

  $(document).ready(function(){
    $('body').append('<p class="example-element">Added by example bundle</p>');
  });
});
