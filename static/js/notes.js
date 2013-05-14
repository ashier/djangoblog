/* */
define([
    'backbone',
    'notesrouter'
    ], function(Backbone, Router) {

        var initialize = function() {
            Router.initialize();
        };

        return {
            initialize: initialize
        };
    }
);
