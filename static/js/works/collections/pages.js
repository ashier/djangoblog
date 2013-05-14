define([
    'backbone',
    'works/models/page'
    ], function(Backbone, Page) {
        var Pages = Backbone.Collection.extend({
            model:Page
        });
        return Pages;
    }
);
