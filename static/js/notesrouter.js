/* */
define([
    'backbone'
    ], function(Backbone) {
        var DjangoBlogRouter = Backbone.Router.extend({
            routes: {
                '':'notes',
            }
        });

        var initialize = function() {
            // Initialize Application Router
            var router = new DjangoBlogRouter;

            // Handle Routes
            router.on('route:notes', function() {
                console.log('notes called');
            });

            // Start Backbone History
            Backbone.history.start();
        };

        return {
            initialize: initialize
        };
    }
);
