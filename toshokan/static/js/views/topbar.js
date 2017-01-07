define([
  'jquery',
  'backbone',
  'bootstrap'
], function($, Backbone) {
    var TopbarView = Backbone.View.extend({
        el: ".topbar ul.nav",

        events: {},

        initialize: function() {
            console.log("Topbar initialized");
        }
    });

    return TopbarView;
});