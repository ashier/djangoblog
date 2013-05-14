/* */
define([
    'backbone'
    ], function(Backbone) {
        var DjangoBlogRouter = Backbone.Router.extend({
            routes: {
                '':'works'
            }
        });

        var initialize = function() {
            // Initialize Application Router
            var router = new DjangoBlogRouter;

            // Handle Routes
            router.on('route:works', function() {
                console.log('works called');
            });

            // Start Backbone History
            Backbone.history.start();
        };

        return {
            initialize: initialize
        };
    }
);
