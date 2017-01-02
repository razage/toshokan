define([
  'jquery',
  'backbone',
  'bootstrap'
], function($, Backbone) {
    var SidebarView = Backbone.View.extend({
        el: "ul.nav.nav-stacked",
        initialize: function() {
            console.log("Sidebar initialized");
        }
    });

    return SidebarView;
});