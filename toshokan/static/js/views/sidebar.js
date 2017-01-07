define([
  'jquery',
  'backbone',
  'bootstrap'
], function($, Backbone) {
    var SidebarView = Backbone.View.extend({
        el: "ul.nav.nav-stacked",

        events: {
            "click #library": "openLibrary"
        },

        initialize: function() {
            console.log("Sidebar initialized");
        },

        openLibrary: function(e) {
            e.preventDefault();
            Backbone.history.navigate("library", {trigger: true});
        }
    });

    return SidebarView;
});