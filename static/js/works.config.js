
/**/
requirejs.config({
    baseUrl:'/static/js',
    paths:{
        handlebars:'libs/handlebars',
        jquery:'libs/jquery',
        underscore:'libs/underscore',
        backbone:'libs/backbone'
    },
    shim: {
        backbone: {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        }
    }
});

require([
    'works'
    ], function(App) {
        console.log("Works Application Initialized...");
        App.initialize();
    }
);
