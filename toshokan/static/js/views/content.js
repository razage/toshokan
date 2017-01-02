define([
  'jquery',
  'backbone',
  'bootstrap',
  'slimscroll'
], function($, Backbone) {
    var ContentView = Backbone.View.extend({
        el: ".content",

        events: {
            "click .chapter": "openChapter",
            "click .series": "openSeries",
            "click .volume": "openVolume"
        },

        initialize: function() {
            console.log("Content initialized");
        },

        openChapter: function(e) {
            var $target = $(e.currentTarget);

            location.href = "/series/" + $target.data("sid") + "/" + $target.data("vid") + "/chapters/" + $target.data("cid");
        },

        openSeries: function(e) {
            location.href = "/series/" + $(e.currentTarget).data("sid");
        },

        openVolume: function(e) {
            var $target = $(e.currentTarget);

            location.href = "/series/" + $target.data("sid") + "/" + $target.data("vid") + "/chapters";
        }
    });

    return ContentView;
});